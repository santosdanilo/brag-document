## Velozient — Senior Full Stack Software Engineer

- **Company:** Velozient; client name undisclosed
- **Position:** Senior Full Stack Software Engineer (React / Python / Go / Node.js or Java)
- **Registered:** 2026-10-30
- **Status:** Opportunity received; application materials prepared
- **Last update:** 2026-10-30

### Process Summary

- **Recruiter:** Camilo Rincon, as identified by the user
- **Source/application:** https://apply.velozient.com/j/93454334/camilo
- **Initial contact:** User received the job description from Camilo; original message, contact date, and communication channel were not provided.
- **Application stage:** Pre-vetting form available; no submission or interview confirmed.

### Job Posting Details

- Remote, full-time; 6+ years software engineering.
- React Frontend; Go primary Backend, with Python/Node.js/Java candidates accepted and expected to learn Go.
- Small agile teams reporting directly to the CTO, collaborating with AI engineers, security leaders, and Product.
- Build AI-native services for a utilities operating system; modernize legacy workflows.
- Geography, time-zone overlap, compensation, contract type, and exact team size are not specified.
- Full captured landing-page text: [job-description.md](job-description.md).

### Company Information

Velozient is the recruiting contact for an unnamed client. According to the posting, the client is building an AI-centric operating system for utilities, covering customer experience, power optimization, grid health, and flexibility. The posting describes backing from a strategic industry partner and a Groupon founder. These are posting statements, not independently verified company facts. Culture signals include startup-speed delivery, ownership, small teams, and direct CTO collaboration.

### Job Requirements

- React; Python, Go, Node.js, or Java; adoption of Go.
- APIs, services, distributed architectures, SQL/NoSQL, message queues, cloud-native engineering.
- AI APIs, embeddings, model/agent-service integration, and production readiness.
- Legacy modernization, secure coding, utility-sector compliance.
- English communication, cross-functional collaboration, rapid delivery, accountability.
- Degree or equivalent experience; ERP or power-utilities experience desirable.

### Confirmed Clarifications

Confirmed directly by the user during registration:

- **React:** 2 years. This supersedes the earlier request to use 3 years.
- **Broader Frontend experience:** 8+ years; do not present this as 8+ years of React or Backend development.
- **Backend scope:** User described Backend work as only at GasHub. Earlier “8+” in response to a Node.js question is not treated as confirmed Backend-language duration after this clarification.
- **GasHub work split:** 60% Frontend / 40% Backend, correcting the earlier reversed interpretation.
- **Five-year split:** Approximately 89% Frontend / 11% Backend, agreed in conversation. Estimate uses roughly 17 months at GasHub × 40% Backend over 60 months; it assumes the remaining period was Frontend and is not a timesheet-derived measure.
- **Go:** No experience; willing to learn and adopt it as primary Backend language.
- **AI integration:** Personally implemented `sec-filings-rag-app` during the AI course: https://github.com/santosdanilo/ai-specialization. Repository-reviewed Groq API calls, hybrid Qdrant retrieval, embeddings, RRF, and ColBERT reranking support a Yes to basic AI tooling integration.
- **Historical scope to reconcile:** Canonical work history also records a GreenAnt AWS Lambda microservice and Finatec Java EE work. Do not delete those facts or silently infer their duration. Clarify their relationship to “Backend only at GasHub” before supplying per-language professional years.

### Profile Match Analysis

The strongest positioning is a Frontend-focused Full Stack Engineer with energy-sector context, recent Backend delivery, and concrete personal AI integration experience.

- **React and performance:** Two years confirmed; GasHub virtualization and profiler-led refactors reduced initial mount time by 97% (E-004, E-021). Added loading-redesign evidence shows a 78.2% smaller initial JavaScript entry through shell-first rendering, intent-aware preloading, and Vite code splitting (E-022); this result is featured in the updated resume.
- **Recent Backend delivery:** GasHub transaction support, Deno/Drizzle architecture, validation, repositories, Unit of Work, and API warm-latency reduction of 95.7% (E-003, E-006).
- **Modernization:** MyTime business-critical payments and GreenAnt energy-dashboard migrations (E-010, E-013).
- **Energy domain:** Natural gas sales, electric-energy dashboards, and enterprise consumption analytics; relevant adjacent domain, without claiming grid operations or utility regulation expertise.
- **AI:** Python personal/course RAG project directly supports the basic AI API requirement, without implying production AI ownership (E-020).
- **Delivery and communication:** Under-three-week prototype, automated tests, onboarding, and Product collaboration (E-002, E-007–E-009); English documented as Full Professional.
- **Gaps:** Go ramp-up, message queues, production distributed-system scale, production AI evaluation/operations, utility compliance, and exact professional Backend-language durations.

Detailed mapping: [job-to-evidence-matrix.md](job-to-evidence-matrix.md).

### Interview Preparation

#### Key Talking Points

1. **GasHub prototype (STAR):** Business needed market validation; deliver core sales workflows quickly; built React/Supabase workflows with AI-assisted development; prototype ready in under three weeks.
2. **Backend integrity (STAR):** Supabase client lacked transactions; enable atomic operations; migrated to Drizzle/Deno with Zod, repositories, use cases, and Unit of Work; enabled atomic multi-step trading operations.
3. **API performance (STAR):** Slow product listing; diagnose latency; profile waterfall, queries, and RLS round trips, parallelize independent work and consolidate transactions; warm latency reduced 95.7%, cold latency 45%. Keep cold and warm results distinct.
4. **Modernization:** Explain incremental migration strategy, production continuity, and testing at MyTime and GreenAnt using `source-of-truth/storytellings.md`.
5. **Personal RAG implementation:** Walk through query embeddings → dense/sparse retrieval → RRF → ColBERT reranking → contextual prompt → Groq answer and retrieval metadata. Discuss evaluation and failure handling as next steps, not completed results.
6. **Go transition:** Be direct about no Go experience and explain transferable API, transaction, testing, and architecture experience.
7. **Loading strategy (STAR):** Large initial entry; prioritize essential UI and defer heavier content; redesigned shell/lazy boundaries and intent/network-aware preloading, extracted reusable React infrastructure, and added production-build asset checks; initial entry shrank 78.2% (75.9% gzip). A 240-reload staging comparison observed median Contracts/Products readiness improve 44.4%/33.2% on cold-cache Slow 4G with CPU 4×. Explain the trade-off: total raw JavaScript increased 2.5%, some scenarios regressed, and Backend dependencies influenced readiness. Image-loading follow-up has no quantified LCP/CLS gain. Evidence: `source-of-truth/evidence/gashub/gbdev-230-frontend-optimization-brag.md`, E-022–E-024.

#### Topics and References

- React render behavior, memoization tradeoffs, virtualization, and automated testing.
- PostgreSQL EXPLAIN ANALYZE, RLS, transaction boundaries, indexes, and latency measurement.
- Go basics: types, interfaces, errors, context cancellation, goroutines/channels, HTTP services, testing.
- Hybrid search, reranking, grounded generation, prompt injection, retrieval evaluation, and API failures. Course reference: `knowledge-base/courses/especializacao-em-engenharia-de-ia/notes/fundamentos-rag.md` (currently a notes placeholder; use project code for implementation detail).
- Queues, retries, idempotency, consistency, and service boundaries: `knowledge-base/system-design-interview/` and `interview-preparation/training-interviews-hard-skills.md`.
- Behavioral narratives: `interview-preparation/training-interviews-soft-skills.md` and `source-of-truth/storytellings.md`.

#### Potential Questions

- How do you choose between dense retrieval, BM25, and hybrid retrieval?
- How would you evaluate RAG answers before exposing them to enterprise customers?
- How did you introduce transactions while preserving ongoing product delivery?
- How would you modernize a utility workflow while maintaining reliability?
- How would you approach your first Go service and its tests?
- Where does your recent Full Stack experience differ from your longer Frontend background?

### Questions to Ask

- What is the expected Frontend/Backend split, and how much independent Backend ownership is required initially?
- What Go onboarding and mentorship are available?
- Which queues, databases, cloud services, and operational responsibilities are in scope?
- Who owns AI evaluation, guardrails, observability, and production model failures?
- Which utility regulations and security controls apply?
- What is the client name, team size, product stage, and current deployment scale?
- Can Brazil-based candidates be hired, and what are the time-zone overlap, contract terms, and compensation range?
- What are the interview stages and the first 90-day expectations?

### Interview Process

No stages or dates confirmed yet.

### Application Materials

- [Job description](job-description.md)
- [Job-to-evidence matrix](job-to-evidence-matrix.md)
- [Screening answers](screening-answers.md)
- [Resume YAML](resume.yaml)
- [Resume PDF](resume.pdf)
- [Recruiter response draft](recruiter-response.md)
