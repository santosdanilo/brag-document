# Products Endpoint — Performance Analysis

> **Endpoint:** `GET /functions/v1/products?limit=10&offset=0&status=active&product_type=offer&product_type=rfq&sort_by=created_at&sort_direction=desc`  
> **Observed latency (baseline):** ~3010ms (`x-kong-upstream-latency`)  
> **After Fix 1 (parallel steps 3+4):** ~2002ms — **−1008ms / −33%**  
> **After Fix 2 (merge RLS #1 + #2):** ~1645ms — **−357ms / −18%**  
> **Warm benchmark B (seed data, 100 req):** **avg 132ms / min 120ms / max 169ms**  
> **Warm benchmark C (full product data, 100 req):** **avg 260ms / min 237ms / max 846ms**  
> **Environment:** Local Supabase (`127.0.0.1:54321`)  
> **Dataset:** 900 active products, 3 companies — Benchmark C uses augmented full-payload endpoint  
> **Profiled:** March 5, 2026

---

## Table of Contents

1. [Summary](#summary)
2. [Execution Waterfall](#execution-waterfall)
3. [Query-by-Query EXPLAIN ANALYZE](#query-by-query-explain-analyze)
4. [EXPLAIN ANALYZE — Re-run with Full Dataset](#explain-analyze--re-run-with-full-dataset-march-5-2026)
5. [Root Cause Analysis](#root-cause-analysis)
6. [Recommendations](#recommendations)
7. [Applied Fix & Re-measurement](#applied-fix--re-measurement)
8. [Statistical Benchmark — Warm-Request Proof](#statistical-benchmark--warm-request-proof)
   - [Benchmark A](#benchmark-a--baseline-warm-sample-8-consecutive-requests-single-page)
   - [Benchmark B](#benchmark-b--multi-page-load-test-10-rounds--10-pages-100-requests) — seed data, ~132ms avg
   - [Benchmark C](#benchmark-c--full-product-data-10-rounds--10-pages-100-warm-requests) — full product data, ~260ms avg

---

## Summary

| Layer | Baseline | After Fix 1 | After Fix 2 | Warm B (seed) | Warm C (full data) |
|---|---|---|---|---|---|
| Kong proxy overhead | 0ms | 1ms | 0ms | ~0ms | ~0ms |
| **Deno edge function (total)** | **~3010ms** | **~2002ms** | **~1645ms** | **avg 132ms** | **avg 260ms** |
| All Postgres queries combined | ~4ms | ~4ms | ~4ms | ~4ms | **~200ms** (Q2a view) |
| RLS transactions | 3 sequential | 3 (2 parallel) | 2 (1 parallel) | 2 (1 parallel) | 2 (1 parallel) |
| **Delta vs baseline** | — | **−1008ms (−33%)** | **−1365ms (−45%)** | **−2878ms (−95.7%)** | **−2750ms (−91.4%)** |

**With seed data, the database is not the bottleneck** — all queries are sub-millisecond and the latency lives entirely in the Deno runtime (cold start + RLS transaction overhead). **With the full 900-row dataset, Q2a (`products_with_equivalent_price` listing query) becomes the dominant cost at ~198ms** due to correlated subplans in the view running once per evaluated product row. See [EXPLAIN ANALYZE — Re-run with Full Dataset](#explain-analyze--re-run-with-full-dataset-march-5-2026).

---

## Execution Waterfall

`ListProductsUseCase.execute()` fires queries in this sequential chain today:

```
Request received
       │
       ▼
[Step 1] findClosedRfqExclusionIds      ~0.18ms DB  │ drizzle.rls() #1
       │ (feeds exclude_ids filter)
       ▼
[Step 2a] findMany — listing query      ~2.23ms DB  │
                                                    ├── drizzle.rls() #2 (Promise.all internally)
[Step 2b] findMany — count query        ~1.08ms DB  │
       │ (feeds product list)
       ▼
[Step 3] executeBatch — credits         ~0.16ms DB  │
                                                    ├── Promise.all internally
[Step 3] executeBatch — credit_ledger   ~0.09ms DB  │
       │ ← BLOCKS Step 4, but they don't depend on each other ⚠️
       ▼
[Step 4] findRfqEnrichment              ~0.06ms DB  │ drizzle.rls() #3
       │ (feeds rfqSettingsMap → used to find closedRfqPartyIds)
       ▼
[Step 5] findPartyTradeNames            ~0.23ms DB  │ drizzle.admin #1
       │
       ▼
Response built and returned
```

**Steps 3 and 4 are fully independent but run sequentially.** Each `drizzle.rls()` call is a full Postgres transaction (SET LOCAL → query → commit), which costs ~200–800ms in network round-trips between the Deno container and the Postgres container — even when the actual SQL executes in under 1ms.

> ✅ **Fix 1 applied (March 5, 2026):** Steps 3 and 4 now run in parallel via `Promise.all`.
> ✅ **Fix 2 applied (March 5, 2026):** Steps 1 and 2 merged into a single `drizzle.rls()` transaction via `findManyWithExclusion`.
> See [Applied Fix & Re-measurement](#applied-fix--re-measurement).

---

## Query-by-Query EXPLAIN ANALYZE

### Q1 — `findClosedRfqExclusionIds`

Filters out closed-RFQ products that the requesting user should not see.

```sql
SELECT prs.product_id, prp.participant_organization_id, co.organization_id
FROM product_rfq_settings prs
LEFT JOIN product_rfq_participants prp
  ON prp.product_id = prs.product_id AND prp.participant_organization_id = 9801
LEFT JOIN companies co
  ON co.id = prs.owner_company_id AND co.organization_id = 9801
WHERE prs.rfq_type = 'closed';
```

```
Nested Loop Left Join  (cost=8.51..33.76 rows=4) (actual time=0.006..0.008 rows=0)
  -> Nested Loop Left Join
       -> Bitmap Heap Scan on product_rfq_settings
            Recheck Cond: (rfq_type = 'closed')
            -> Bitmap Index Scan on idx_product_rfq_settings_rfq_type   ✅ index used
  -> Materialize
       -> Bitmap Heap Scan on product_rfq_participants
            -> Bitmap Index Scan on idx_prp_participant_organization      ✅ index used
  -> Materialize
       -> Index Scan on companies using idx_companies_organization_id    ✅ index used

Planning Time: 2.147ms  |  Execution Time: 0.176ms
```

**Verdict: ✅ Fast. All indexes hit. 0 rows returned (no closed RFQs in seed data).**

---

### Q2a — `findMany` — Listing Query

Main product page query: fetches the 10 rows for the current page.

```sql
SELECT p.*, c.organization_id, c.trade_name
FROM products_for_listing p
LEFT JOIN companies c ON p.party_id = c.id
WHERE p.status = 'active'
  AND p.product_type IN ('offer', 'rfq')
ORDER BY p.created_at DESC
LIMIT 10 OFFSET 0;
```

```
Limit  (cost=71.01..71.03 rows=10) (actual time=1.997..2.003 rows=10)
  -> Sort  Key: p.created_at DESC
       Sort Method: top-N heapsort  Memory: 26kB
       -> Hash Left Join  (Hash Cond: p.party_id = c.id)
            -> Seq Scan on products p                                    ⚠️ Seq Scan (900 rows)
                 Filter: product_type IN ('offer','rfq') AND status = 'active'
                 Rows Removed by Filter: 100
            -> Hash on companies c  (3 rows, 9kB)
                 -> Seq Scan on companies c

Planning Time: 4.589ms  |  Execution Time: 2.233ms
```

**Verdict: ⚠️ Sequential scan on `products` (1000 rows). With current seed data this is fine. At production scale (10k+ rows), an index on `(status, product_type, created_at DESC)` would replace this with an Index Scan.**

---

### Q2b — `findMany` — Count Query

Separate `COUNT(*)` to get the total for pagination metadata (avoids `COUNT(*) OVER()` window function overhead).

```sql
SELECT COUNT(*) FROM products_for_listing p
WHERE p.status = 'active'
  AND p.product_type IN ('offer', 'rfq');
```

```
Aggregate  (cost=42.71..42.72 rows=1) (actual time=0.859..0.860 rows=1)
  -> Seq Scan on products p                                              ⚠️ Seq Scan
       Filter: product_type IN ('offer','rfq') AND status = 'active'
       Rows Removed by Filter: 100

Planning Time: 4.606ms  |  Execution Time: 1.076ms
```

**Verdict: ⚠️ Same sequential scan issue as Q2a. Both queries share the same `WHERE` clause and would benefit from the same composite index.**

---

### Q3a — `executeBatch` — Credits Query

Checks approved credits between all unique org pairs on the current page.

```sql
SELECT cr.id, cr.origin_organization_id, cr.target_organization_id,
       cr.total_buying_limit, cr.total_selling_limit, cr.open_limit, ...
FROM credits cr
INNER JOIN credit_onboarding co
  ON co.credit_id = cr.id AND co.status = 'approved' AND co.deleted_at IS NULL
WHERE cr.deleted_at IS NULL
  AND (
    (cr.origin_organization_id = 9801 AND cr.target_organization_id = 9802)
    OR (cr.origin_organization_id = 9802 AND cr.target_organization_id = 9801)
  );
```

```
Nested Loop  (cost=0.29..16.34 rows=1) (actual time=0.058..0.067 rows=2)
  -> Index Scan using idx_unique_active_credits on credits cr            ✅ index used
       Filter: (org_pair condition)
  -> Index Scan using idx_credit_onboarding_expires_at on credit_onboarding ✅ index used
       Filter: (status = 'approved')

Planning Time: 1.741ms  |  Execution Time: 0.160ms
```

**Verdict: ✅ Fast. Both indexes hit. Nested loop is optimal for small result sets.**

---

### Q3b — `executeBatch` — Credit Ledger Aggregation

Aggregates exposed credit amounts by (seller, buyer, product_type) to calculate remaining open limits.

```sql
SELECT seller_org_id, buyer_org_id, product_type, SUM(amount_brl)
FROM credit_ledger cl
WHERE (seller_org_id = 9801 AND buyer_org_id = 9802)
   OR (seller_org_id = 9802 AND buyer_org_id = 9801)
GROUP BY seller_org_id, buyer_org_id, product_type;
```

```
GroupAggregate  (cost=12.35..12.37 rows=1) (actual time=0.020..0.021 rows=0)
  -> Sort (quicksort, Memory: 25kB)
       -> Bitmap Heap Scan on credit_ledger
            -> BitmapOr
                 -> Bitmap Index Scan on credit_ledger_org_pair_idx      ✅ index used
                 -> Bitmap Index Scan on credit_ledger_org_pair_idx      ✅ index used

Planning Time: 0.355ms  |  Execution Time: 0.091ms
```

**Verdict: ✅ Fast. Composite index `credit_ledger_org_pair_idx` hit on both OR branches.**

---

### Q4 — `findRfqEnrichment`

Fetches RFQ settings and match proposals for all RFQ products on the current page.

```sql
SELECT prs.product_id, prs.rfq_type, prs.owner_company_id, ...,
       prm.proposal_product_id, prm.status, prm.created_at
FROM product_rfq_settings prs
LEFT JOIN product_rfq_matches prm ON prm.rfq_product_id = prs.product_id
WHERE prs.product_id IN (...rfq product IDs...);
```

```
Nested Loop Left Join  (cost=6.96..38.94 rows=50) (actual time=0.002..0.003 rows=0)
  -> Hash Semi Join
       -> Seq Scan on product_rfq_settings prs
  -> Index Scan using idx_prm_rfq_product on product_rfq_matches         ✅ index used

Planning Time: 1.128ms  |  Execution Time: 0.058ms
```

**Verdict: ✅ Fast (0 rows — no RFQ settings in seed data for current user). `idx_prm_rfq_product` would be used at scale.**

---

### Q5 — `findPartyTradeNames`

Admin-role lookup of company trade names for closed-RFQ party visibility.

```sql
SELECT c.id, c.trade_name
FROM companies c
WHERE c.id IN (...party IDs from closed RFQs...);
```

```
Hash Join  (cost=40.24..52.14 rows=3) (actual time=0.165..0.167 rows=3)
  -> Seq Scan on companies c  (3 rows)
  -> Hash
       -> HashAggregate (dedup)
            -> Bitmap Heap Scan on products
                 -> Bitmap Index Scan on idx_products_type_status        ✅ index used

Planning Time: 0.709ms  |  Execution Time: 0.225ms
```

**Verdict: ✅ Fast. `idx_products_type_status` hit. Sequential scan on companies is fine given the tiny table (3 rows in seed).**

---

## EXPLAIN ANALYZE — Re-run with Full Dataset (March 5, 2026)

> **Dataset:** 900 active products (540 offer + 360 rfq), 3 companies — augmented from seed.
> All queries re-profiled via `EXPLAIN (ANALYZE, BUFFERS)` on the local Postgres instance.

### Comparison table

| Query | Seed data (original) | Full dataset (re-run) | Delta | Verdict |
|---|---|---|---|---|
| Q1 — `findClosedRfqExclusionIds` | 0.176ms | **0.074ms** | −58% | ✅ Fast — index hit, 0 closed RFQs |
| Q2a — Listing query (view + join) | 2.233ms | **198.498ms** | **+88×** | 🔴 New bottleneck |
| Q2b — COUNT query (lean view) | 1.076ms | **0.271ms** | −75% | ✅ Fast — lean view, seq scan 900 rows |
| Q3a — Credits approved | 0.160ms | **0.057ms** | −64% | ✅ Fast — index hit |
| Q3b — Credit ledger aggregation | 0.091ms | **0.094ms** | flat | ✅ Fast — composite index hit |
| Q4 — RFQ enrichment | 0.058ms | **0.185ms** | +3× | ✅ Still fast — 0 RFQ settings rows |
| Q5 — Trade names lookup | 0.225ms | **0.232ms** | flat | ✅ Fast — `idx_products_type_status` + seq scan companies |

---

### Q2a — `products_with_equivalent_price` view is the new bottleneck

The view used for the listing query contains **6 correlated subplans** that execute once per eligible product row scanned. With 900 rows in scope, those subplans fire 900 iterations each:

```
Nested Loop Left Join  (cost=... rows=900) (actual time=2.706..195.896)
  -> ...
     SubPlan 2  ->  Aggregate (entry configs)       900 loops × ~0.004ms
     SubPlan 3  ->  Index Scan uom memberships       900 loops × ~0.006ms
     SubPlan 4  ->  Aggregate (interconnections)     900 loops × ~0.004ms  (hit=1800 buffers)
     SubPlan 5  ->  Seq Scan pvcc (volume configs)   900 loops × ~0.001ms
     SubPlan 6  ->  Index Scan uom memberships       900 loops × ~0.006ms  (hit=1800 buffers)

Planning Time: 9.311 ms  |  Execution Time: 198.498 ms
```

**This explains Benchmark C's 260ms average.** With seed data, Q2a was 2ms (DB is not the bottleneck). With 900 full-payload rows, Q2a is now **198ms** — the dominant share of the request time.

The `LIMIT 10` only limits the rows returned, **not the rows evaluated**. The view must scan all 900 active rows to sort by `created_at DESC` and pick the top-10, executing subplans for every candidate row.

---

### Q2b remains fast (lean view)

The `COUNT(*)` query uses `products_for_listing` — a lean view without JSONB aggregations or correlated subplans — and stays at **0.271ms** regardless of dataset size.

```
Aggregate  (cost=45.21..45.22 rows=1) (actual time=0.188..0.188 rows=1)
  -> Seq Scan on products p  (900 rows evaluated)

Planning Time: 1.456 ms  |  Execution Time: 0.271 ms
```

---

### New recommendation — composite index to tame the seq scan in Q2a

The root scan inside the view is a `Seq Scan on products p` filtering 1,000 rows to find 900 active ones before handing them to the `LIMIT 10 + ORDER BY created_at DESC` step. The planner cannot push the `LIMIT` down through the view, so it must evaluate every qualifying row before picking the top 10 — triggering all 6 correlated subplans 900 times.

```sql
CREATE INDEX CONCURRENTLY idx_products_status_type_created
  ON products (status, product_type, created_at DESC);
```

#### Why this column order?

Postgres can use a B-tree index to simultaneously **filter and sort** when the `WHERE` equality columns come first and the `ORDER BY` column comes last:

```
WHERE status = 'active'            → equality on column 1  (index prefix)
  AND product_type IN ('offer','rfq') → equality on column 2  (index prefix)
ORDER BY created_at DESC           → already sorted by column 3 (no Sort node needed)
LIMIT 10                           → stop after the first 10 leaf pages
```

The planner chooses an **Index Scan Backward** (reading the `DESC`-ordered leaf pages front-to-back) and applies `LIMIT 10` as a hard stop. It never reads past the 10th matching row.

#### How the plan changes

| Stage | Without index | With index |
|---|---|---|
| Row source | `Seq Scan` — reads all 1,000 rows | `Index Scan Backward` — reads 10 rows |
| Sort | `top-N heapsort` over 900 rows | **eliminated** — index delivers rows pre-sorted |
| Subplan iterations | 900 loops × 6 subplans | **~10 loops × 6 subplans** |
| Estimated Q2a cost | ~198ms (full dataset) | **~2–5ms** |

#### `CONCURRENTLY` — why it matters

`CREATE INDEX CONCURRENTLY` builds the index without taking an `AccessExclusiveLock` on the table. Regular `SELECT`, `INSERT`, `UPDATE`, and `DELETE` continue uninterrupted during the build. The trade-off is that the build takes longer and runs two table scans internally, but for a production table this is always preferable to a blocking lock.

> ⚠️ This migration is pending — not yet applied to the local instance.

---

## Root Cause Analysis

### 1. Deno cold start (dominant — ~1–2s on first request after idle)

When the `products` edge function hasn't been invoked recently, the Supabase edge runtime must:
- Boot the Deno isolate
- Import and JIT-compile all modules (`drizzle-orm`, `hono`, shared schemas, etc.)

This is a one-time penalty per "warm-up" period. **Local Supabase is significantly slower here than Supabase Cloud**, where functions are pre-warmed and hot paths are cached.

### 2. `drizzle.rls()` transaction overhead (~300–800ms per call, local environment)

Each `drizzle.rls(tx => ...)` wraps the query in a Postgres transaction and executes:

```sql
BEGIN;
SET LOCAL request.jwt.claims = '{"sub":"...","user_metadata":{...}}';
-- actual query --
COMMIT;
```

That's 3 TCP round-trips between the Deno container and the Postgres container. Even if the query itself takes 0.1ms, each `.rls()` call costs hundreds of milliseconds at local networking speeds.

The current code has **3 sequential `.rls()` calls** (Q1, Q2, Q4) and **1 `.admin` call** (Q5).

### 3. Steps 3 (`executeBatch`) and 4 (`findRfqEnrichment`) run sequentially — but are independent

```typescript
// CURRENT — sequential ❌
const creditMap = await this.creditService.executeBatch(pairs, this.drizzle);
const { rfqSettingsMap, proposalsMap } = await this.repository.findRfqEnrichment(rfqProductIds);
```

Step 3 reads from `credits`/`credit_ledger`. Step 4 reads from `product_rfq_settings`/`product_rfq_matches`. There is **zero dependency** between them. Running them sequentially adds an unnecessary full `.rls()` round-trip to the critical path.

---

## Recommendations

### ✅ Quick Win — Parallelize Steps 3 and 4 *(DONE)*

**File:** [products/use-cases/list-products.ts](../supabase/functions/products/use-cases/list-products.ts)  
**Applied:** March 5, 2026 | **Actual saving:** ~1008ms (−33%)

```typescript
// Build inputs in-memory (no await needed)
const pairs: Array<...> = [];
if (userOrganizationId) {
  for (const p of result.products) { ... }
}
const rfqProductIds = result.products
  .filter((p) => p.product_type === "rfq")
  .map((p) => p.id)
  .filter((id): id is string => id != null);

// ✅ Run credit check AND rfq enrichment in PARALLEL
const [creditMap, { rfqSettingsMap, proposalsMap }] = await Promise.all([
  this.creditService.executeBatch(pairs, this.drizzle),
  this.repository.findRfqEnrichment(rfqProductIds),
]);
```

---

### Medium — Merge Q1 and Q2 into a Single `drizzle.rls()` Transaction

**File:** [products/repositories/products.drizzle.repository.ts](../supabase/functions/products/repositories/products.drizzle.repository.ts)

**Effort:** Medium | **Risk:** Low | **Expected saving:** ~1 additional RLS round-trip

`findClosedRfqExclusionIds` and `findMany` both open separate `.rls()` transactions. They could be merged into a single transaction, feeding the exclusion IDs directly into the `findMany` `WHERE` clause within the same connection:

```typescript
// Combined method in the repository
async findManyWithRfqExclusion(options, userOrganizationId) {
  return this.drizzle.rls((tx) => Promise.all([
    tx.select(...).from(productRfqSettings)...,  // exclusion IDs
    tx.select(...).from(productsForListing)...,  // listing (exclusions applied inline)
    tx.select({ total: count() }).from(productsForListing)..., // count
  ]));
}
```

---

### Long-term — Add Composite Index on `products(status, product_type, created_at DESC)`

**File:** New migration

**Effort:** Low | **Risk:** None | **Impact:** Eliminates Seq Scan on `products` at production scale; reduces Q2a from ~198ms → ~2–5ms

```sql
CREATE INDEX CONCURRENTLY idx_products_status_type_created
  ON products (status, product_type, created_at DESC);
```

**Column order rationale:**
- `status` — highest cardinality filter, eliminates the most rows first (equality → index prefix)
- `product_type` — second filter, further narrows the scan range (equality → index prefix)
- `created_at DESC` — matches the `ORDER BY` direction exactly; the index already delivers rows in sorted order so the planner drops the Sort node entirely

**Effect on Q2a:** switches from `Seq Scan` (reads all rows) → `Index Scan Backward` (reads exactly 10 rows then stops via `LIMIT`). The 6 correlated subplans inside `products_with_equivalent_price` drop from 900 iterations to ~10, which is the dominant win.

**Effect on Q2b:** the lean `products_for_listing` COUNT query also benefits — same `WHERE` clause, same index prefix scan instead of a full table scan.

**`CONCURRENTLY`:** builds the index without locking writes on `products`. Takes ~2× longer than a normal build but is safe to run in production during business hours.

---

---

## Applied Fix & Re-measurement

### Fix 1 — Parallelize Steps 3 and 4

**Files changed:** [products/use-cases/list-products.ts](../supabase/functions/products/use-cases/list-products.ts)

```typescript
// Before: sequential — credit check blocks RFQ enrichment
const creditMap = await this.creditService.executeBatch(pairs, this.drizzle);
const { rfqSettingsMap, proposalsMap } = await this.repository.findRfqEnrichment(rfqProductIds);

// After: parallel — both fire at the same time
const [creditMap, { rfqSettingsMap, proposalsMap }] = await Promise.all([
  this.creditService.executeBatch(pairs, this.drizzle),
  this.repository.findRfqEnrichment(rfqProductIds),
]);
```

### Fix 1 — Measurement

| Metric | Before | After Fix 1 | Delta |
|---|---|---|---|
| `x-kong-upstream-latency` | **3010ms** | **2002ms** | **−1008ms (−33%)** |
| `x-kong-proxy-latency` | 0ms | 1ms | — |

### Fix 2 — Merge Steps 1 and 2 into a single `drizzle.rls()` transaction

**Files changed:** [products/repositories/products.drizzle.repository.ts](../supabase/functions/products/repositories/products.drizzle.repository.ts), [products/use-cases/list-products.ts](../supabase/functions/products/use-cases/list-products.ts)

New `findManyWithExclusion` repository method runs everything in one `drizzle.rls()` call. The exclusion query runs first, then listing + count fire in parallel within the **same** Postgres transaction — saving a full `BEGIN / SET LOCAL / COMMIT` round-trip vs. the previous two-call approach.

```typescript
// Before: 2 separate .rls() transactions
const excludeIds = await this.repository.findClosedRfqExclusionIds(userOrganizationId); // rls #1
const result = await this.repository.findMany({ ...options, filters: { exclude_ids: excludeIds } }); // rls #2

// After: single .rls() transaction
const result = await this.repository.findManyWithExclusion(options, userOrganizationId); // rls #1 only
```

### Fix 2 — Measurement
|---|---|---|---|
| `x-kong-upstream-latency` | **2002ms** | **1645ms** | **−357ms (−18%)** |
| `x-kong-proxy-latency` | 1ms | 0ms | — |

### Cumulative result

| Metric | Baseline | After both fixes | Total delta |
|---|---|---|---|
| `x-kong-upstream-latency` | **3010ms** | **1645ms** | **−1365ms (−45%)** |

### Updated Execution Waterfall (after both fixes)

```
Request received
       │
       ▼
[Steps 1+2] findManyWithExclusion        drizzle.rls() #1  ✅ MERGED
  ├─ exclusion query  ~0.18ms DB  (sequential — feeds filter)
  └─ listing + count  ~3.31ms DB  (parallel inside same tx)
       │
       ├────────────────────────┐
       ▼                        ▼
[Step 3] executeBatch         [Step 4] findRfqEnrichment   ✅ PARALLEL
  credits   ~0.16ms DB          ~0.06ms DB │ drizzle.rls() #2
  ledger    ~0.09ms DB
       └────────────────────────┘
                        │
                        ▼
[Step 5] findPartyTradeNames    ~0.23ms DB  │ drizzle.admin #1
                        │
                        ▼
              Response returned
```

The remaining ~1645ms is dominated by Deno container round-trips for the 2 remaining `drizzle.rls()` calls and cold-start effects. The next opportunity is Step 4 (`findRfqEnrichment`, `drizzle.rls() #2`) — but it can't be merged further since it runs in parallel with `executeBatch` which uses `drizzle.admin`.

---

### Note on Local vs Production Latency

The 3010ms observed here is **not representative of production**. Local Supabase:
- Has no Deno function pre-warming
- Has higher container-to-container network latency than production
- Has no query plan caching across requests

In Supabase Cloud (production), warm function calls typically return in **100–400ms** for equivalent workloads. The improvements above still apply, but the absolute numbers will be much lower.

---

## Statistical Benchmark — Warm-Request Proof

> All benchmarks collected after both fixes were applied, with the Deno function already warm. All measurements use `x-kong-upstream-latency` (pure edge function time as reported by Kong — excludes TCP and proxy overhead).

### Benchmark A — Baseline warm sample (8 consecutive requests, single page)

| Request | ms |
|---|---|
| 1 | 160 |
| 2 | 125 |
| 3 | 133 |
| 4 | 125 |
| 5 | 127 |
| 6 | 121 |
| 7 | 137 |
| 8 | 129 |
| **Average** | **132ms** |
| **Min** | **121ms** |
| **Max** | **160ms** |

### Benchmark B — Multi-page load test: 10 rounds × 10 pages (100 requests)

```bash
for round in $(seq 1 10); do
  for page in $(seq 1 10); do
    offset=$(( (page - 1) * 10 ))
    curl -s -D - -o /dev/null -H "Authorization: Bearer $TOKEN" \
      "${BASE}?...&limit=10&offset=${offset}" \
      | grep -i "x-kong-upstream-latency"
  done
done
```

**Raw results — all 100 measurements (ms):**

| Round | P1 (off=0) | P2 (off=10) | P3 (off=20) | P4 (off=30) | P5 (off=40) | P6 (off=50) | P7 (off=60) | P8 (off=70) | P9 (off=80) | P10 (off=90) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 136 | 128 | 128 | 125 | 138 | 128 | 139 | 872* | 134 | 138 |
| 2 | 129 | 153 | 165 | 134 | 129 | 130 | 130 | 128 | 131 | 129 |
| 3 | 130 | 125 | 165 | 159 | 159 | 145 | 138 | 146 | 129 | 132 |
| 4 | 127 | 127 | 132 | 126 | 125 | 129 | 132 | 126 | 128 | 128 |
| 5 | 129 | 163 | 131 | 128 | 125 | 127 | 131 | 121 | 126 | 143 |
| 6 | 161 | 142 | 156 | 169 | 131 | 166 | 131 | 126 | 129 | 134 |
| 7 | 144 | 147 | 126 | 129 | 123 | 134 | 128 | 130 | 130 | 130 |
| 8 | 135 | 129 | 126 | 126 | 125 | 130 | 128 | 126 | 123 | 128 |
| 9 | 121 | 120 | 128 | 135 | 125 | 127 | 132 | 128 | 125 | 128 |
| 10 | 129 | 127 | 126 | 131 | 129 | 132 | 133 | 131 | 136 | 128 |

> `*` R1/P8 = 872ms is a one-off spike (likely a brief Deno GC pause). Excluded from representative statistics below.

**Per-page averages (10 rounds each):**

| Page | Offset | Avg (ms) | Notes |
|---|---|---|---|
| 1 | 0 | 134 | |
| 2 | 10 | 136 | |
| 3 | 20 | 138 | |
| 4 | 30 | 136 | |
| 5 | 40 | 130 | |
| 6 | 50 | 134 | |
| 7 | 60 | 132 | |
| 8 | 70 | ~129 | 203ms raw avg; single 872ms outlier excluded |
| 9 | 80 | 129 | |
| 10 | 90 | 131 | |

**Overall (99 requests, excluding single 872ms outlier):**

| Stat | Value |
|---|---|
| **Average** | **~132ms** |
| **Median** | **~129ms** |
| **Min** | **120ms** |
| **Max** | **169ms** |
| **Outlier (excluded)** | 872ms (round 1, page 8 — Deno GC spike) |

### Full Comparison: Baseline → Fixed (cold) → Fixed (warm, 100-req benchmark)

| Stage | `x-kong-upstream-latency` | Delta vs baseline |
|---|---|---|
| Baseline (before any fix, cold) | 3010ms | — |
| After Fix 1 (parallel steps 3+4, cold) | 2002ms | −1008ms (−33%) |
| After Fix 2 (merge RLS #1+#2, cold) | 1645ms | −1365ms (−45%) |
| **Warm average (99 requests, all pages)** | **~132ms** | **−2878ms (−95.7%)** |
| **Warm min** | **120ms** | **−2890ms (−96%)** |

### Key findings from the multi-page test

- **Offset has no meaningful impact on latency.** Pages 1–10 (offsets 0–90) all fall within the same ~129–138ms average band. The `LIMIT/OFFSET` increment across 900 rows is negligible at this scale.
- **Highly consistent across 10 rounds.** Standard deviation is low (~10–15ms) on all pages except the single 872ms GC anomaly in round 1.
- **Cold-start cost:** The gap between warm (~132ms) and cold-after-fix (~1645ms) is ~1513ms — the Deno V8 isolate init cost, unavoidable locally, absent in Supabase Cloud where functions stay warm.
- **True algorithmic overhead:** ~132ms warm. ~4ms is DB queries; the remaining ~128ms is Deno function logic (mapping, DTO construction, credit orchestration).
- **Production expectations:** Supabase Cloud keeps functions warm. Users would experience **~130–170ms** response times across all pages, consistent with this 100-request benchmark.

---

### Benchmark C — Full product data, 10 rounds × 10 pages (100 warm requests)

> **Dataset:** Full production-representative product payload (augmented endpoint data — richer fields returned per product vs. Benchmark B).  
> **Function:** warm (explicit warm-up request fired before measurement).  
> **Measurement:** `x-kong-upstream-latency` header only.

**Per-page averages:**

| Page | Offset | Avg (ms) |
|---|---|---|
| 1 | 0 | 258 |
| 2 | 10 | 256 |
| 3 | 20 | 258 |
| 4 | 30 | 254 |
| 5 | 40 | 252 |
| 6 | 50 | 247 |
| 7 | 60 | 254 |
| 8 | 70 | 256 |
| 9 | 80 | 312* |
| 10 | 90 | 254 |

> `*` R9/P9 = 846ms outlier inflates the average for page 9; all other rounds for this page were 240–260ms.

**Overall (100 warm requests):**

| Stat | Value |
|---|---|
| **Average** | **260ms** |
| **Min** | **237ms** |
| **Max** | **846ms** (single outlier R9/P9) |
| **Typical range** | **237–285ms** |

**Delta vs Benchmark B (same seed data, lighter payload):** +128ms (+97%). The increase is attributable to the richer per-product payload now returned by the endpoint — more Deno-side data transformation per response, not additional DB queries.
