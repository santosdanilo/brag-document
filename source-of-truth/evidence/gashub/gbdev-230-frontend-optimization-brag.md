# Frontend loading optimization

**GBDEV-230 · PR #1654 · Merged October 23, 2026**

## Brag document summary

I redesigned the marketplace frontend’s loading strategy, reducing the initial JavaScript entry bundle by **78.2%**, from **2.75 MB to 598 KB**, with a **75.9% reduction in gzip size**. I separated lightweight page shells from heavy content, introduced route- and interaction-aware preloading, and reorganized action bundles around actual usage and dependency boundaries. I also extracted a reusable React preloading library and added production-build E2E coverage to verify that preloaded assets actually reached the browser.

A before/after evaluation covering **240 reloads across six routes** showed improvements particularly under constrained network and CPU conditions: median Contracts readiness improved by **44.4% on cold-cache Slow 4G** and Products by **33.2%** under the same conditions. These were staging measurements; end-to-end timings included backend dependencies and gains varied by scenario.

## Work done and strategies used

The implementation points below are **[FATO]**, supported by the merged PR and its versioned `docs/FRONTEND_LOADING_STRATEGY.md`.

| Area | Work and strategy | Value demonstrated |
|---|---|---|
| Critical-path loading | Kept navigation, authentication gates, page titles, and essential controls eager; split heavier page bodies behind lazy-loading boundaries across products, contracts, credit management, reports, settings, and forward curves. | Prioritized useful initial UI while removing nonessential code from startup. |
| Predictive preloading | Started loading the initial destination before React mounted; warmed other primary routes during idle time and targeted routes on navigation hover/focus. | Moved code fetching ahead of likely navigation without making every route eager. |
| Network-aware scheduling | Skipped speculative idle warming for Save-Data and slow 2G connections; retained immediate warming for the prominent Standard Order action. | Balanced responsiveness, bandwidth use, and action priority. |
| Reusable loading infrastructure | Extracted `@gashub/react-preload`, sharing pending imports and resolved components between preloading and rendering, with cancellation and failure handling. Completed preloads could render synchronously. | Established a consistent pattern and addressed the subtle case where a downloaded module can still briefly suspend on its first React render. |
| Dependency-graph optimization | Grouped related product actions and helpers into usage-aligned Vite chunks; isolated shared helpers and prevented action roots from entering the eager dependency graph. | Reduced fragmentation within the action graph while avoiding emitted chunk cycles. |
| On-demand action composition | Deferred product and contract action surfaces and RFQ-specific detail composition; preserved stacked history/detail drawers and started detail queries only on opening. | Separated code warming from component mounting and unnecessary data requests. |
| Additional startup work | Optimized initial CSS/font discovery, deferred offscreen chart renderer startup, and deferred metadata queries for closed dashboard filters. | Addressed startup cost beyond JavaScript file size alone. |
| Regression protection | Added production-build Playwright checks for successful route/action asset responses, plus focused tests for shared imports, cold/warm loading, cancellation, failure recovery, and state retention. | Verified actual browser behavior and protected the loading architecture against regressions. |

## Measured results

**[FATO — results recorded in the card’s performance comment; measurements from homolog/staging.]**

| Metric / scenario | Before → After | Improvement |
|---|---|---|
| Initial JS entry, minified | 2,746,031 → 598,272 bytes | **78.2% smaller** |
| Initial JS entry, gzip | 705,349 → 170,120 bytes | **75.9% smaller** |
| Initial JS entry, Brotli | 530,038 → 138,852 bytes | **73.8% smaller** |
| Contracts readiness — Slow 4G, cold cache, CPU 4× | 34.46 → 19.17 s | **44.37% faster** |
| Contracts readiness — Slow 4G, warm cache, CPU 4× | 27.16 → 14.92 s | **45.04% faster** |
| Products readiness — Slow 4G, cold cache, CPU 4× | 12.59 → 8.41 s | **33.18% faster** |
| Login readiness — normal network, cold cache | 1.03 → 0.69 s | **32.59% faster** |

**Measurement strategy:** six routes × two network/CPU conditions × cold/warm cache × five runs = **120 reloads per version**, comparing median custom route-readiness timings.

## Engineering judgment

- **Optimized loading priority rather than just splitting files.** Used three explicit tiers: eager essentials, immediate/intent-driven lazy loading, and idle speculative warming.
- **Examined the complete dependency graph.** An intermediate action-bundling comparison reduced additional JS files from **41 to 34**, with nearly unchanged action bytes. This is separate from the overall before/after application chunk count.
- **Made the trade-off visible.** The full build moved from **20 to 179 JS chunks**, and total emitted JS increased **2.5% raw**. The strongest result is a much smaller initial entry, not a reduction in all application code. Compressed sizes are calculated per asset, not measured network transfer totals.
- **Used evidence carefully.** Some normal-network/cache scenarios regressed, and backend responses influenced readiness. Five runs per scenario describe observed variation, not statistical significance. Lighthouse scores were measured only after the change, so they do not establish a before/after score improvement.

## Short version

Delivered a frontend loading redesign that cut the initial JavaScript entry by **78.2%** (**75.9% gzip**) through shell-first rendering, intent-aware preloading, and dependency-aligned code splitting. Built reusable React preloading infrastructure and production-asset E2E checks. Across a **240-reload staging comparison**, observed **44.4% faster Contracts readiness** and **33.2% faster Products readiness** on cold-cache Slow 4G with CPU throttling.

## Follow-up: image loading and presentation optimization

**[PR #1692](https://github.com/GasHub-Brasil/gashub/pull/1692) · Merged October 28, 2026**

**[FATO — verified against the merged PR diff.]** As part of the Lighthouse remediation work, I also optimized image discovery, loading priority, and sizing:

- **Earlier logo discovery:** added HTML image preload hints for the four SVG logo variants (light/dark and expanded/collapsed), allowing the browser to discover these assets before React renders their consumers.
- **Explicit authentication-image priority:** configured the authentication background pattern with `loading="eager"` and `fetchPriority="high"` so the browser treats it as an immediate image request.
- **Intrinsic image sizing:** specified the pattern’s `1142 × 442` intrinsic dimensions, providing aspect-ratio information before the image loads. Added `w-auto` to the shared themed logo to preserve proportional width alongside its configured height.
- **Accessible decoration:** marked the authentication pattern as decorative with empty alternative text and `aria-hidden="true"`.
- **Regression coverage:** added an authentication-container test asserting the image’s intrinsic dimensions, eager loading, high fetch priority, and decorative semantics.

**Strategy:** complement JavaScript optimization with browser-native resource hints and explicit image sizing/priority. These changes addressed image scheduling and presentation; the PR does not establish image compression, format-conversion savings, or a quantified before/after LCP or CLS improvement attributable to these changes. Preloading all four logo variants also favors early availability over selectively fetching only the active variant.

### Combined short version

Delivered a frontend loading redesign that cut the initial JavaScript entry by **78.2%** (**75.9% gzip**) through shell-first rendering, intent-aware preloading, and dependency-aligned code splitting. Built reusable React preloading infrastructure and production-asset E2E checks. Extended the work with **SVG logo preloading, explicit authentication-image loading priority, intrinsic image sizing, and regression coverage**. Across a **240-reload staging comparison of the earlier loading refactor**, observed **44.4% faster Contracts readiness** and **33.2% faster Products readiness** on cold-cache Slow 4G with CPU throttling.

## Sources

- [GBDEV-230 — card and performance measurement comment](https://app.plane.so/gashub-brasil/browse/GBDEV-230/)
- [PR #1654 — perf(frontend): warm route and product action bundles](https://github.com/GasHub-Brasil/gashub/pull/1654)
- [PR #1692 — Lighthouse remediation, including image loading and sizing changes](https://github.com/GasHub-Brasil/gashub/pull/1692)
- [Frontend loading strategy at the PR’s final commit](https://github.com/GasHub-Brasil/gashub/blob/61bb25055b52afa7b850b88af4c68cc355e58ad7/docs/FRONTEND_LOADING_STRATEGY.md)

The implementation summary was checked against PR metadata, commit history, and the versioned loading strategy. Performance figures are attributed to the existing card comment; the original measurement artifacts were not independently rerun for this summary.
