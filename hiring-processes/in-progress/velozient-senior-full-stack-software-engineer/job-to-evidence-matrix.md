## Job-to-Evidence Matrix

### Process

- **Company:** Velozient; end client undisclosed
- **Position:** Senior Full Stack Software Engineer
- **Source job description:** [job-description.md](job-description.md)
- **Last reviewed:** 2026-10-30
- **Status:** Ready for resume; screening durations still need clarification

### Requirement Mapping

| ID | Requirement or responsibility | Priority | Evidence IDs / source paths | Match | Claim status | Resume treatment or gap | Recruiter question |
|---|---|---|---|---|---|---|---|
| R-001 | 6+ years in software engineering, SaaS/enterprise | High | E-001, E-021; `source-of-truth/work-experience.md` | Strong | confirmed | 8+ years Frontend; MyTime global scheduling/POS and energy enterprise products | — |
| R-002 | Strong React; build and maintain Frontend | High | E-002, E-004, E-007, E-021, E-022 | Strong | confirmed | Two years React; initial JS entry reduction of 78.2% through loading redesign; automated tests | — |
| R-003 | Python, Go, Node.js, or Java Backend proficiency | High | E-006; `source-of-truth/personal-professional-profile.md` Primary Stack; GasHub in `work-experience.md` | Partial | confirmed | Node.js/NestJS listed skills; recent Backend results specifically use Deno/Drizzle. Python project work explicitly labeled personal. No 8-year Backend claim | What Backend depth is expected at entry? |
| R-004 | Adopt Go as primary Backend technology | High | Process Confirmed Clarifications | Partial | confirmed | No Go experience; willingness recorded in screening answers, not as a skill | What onboarding and Go ramp-up support are available? |
| R-005 | Design APIs and services; system design fundamentals | High | E-003, E-005, E-006, E-012 | Strong | confirmed | API latency, transactions, repositories/use cases, Unit of Work | — |
| R-006 | Basic AI tooling/API integration and embeddings | High | E-020; `source-of-truth/personal-projects.md` | Strong | confirmed | Explicit personal/course SEC-filings RAG entry: Groq, Qdrant, embeddings, RRF, ColBERT | — |
| R-007 | Production-ready AI and agent services | High | E-020 | Partial | do not claim | Personal RAG implementation only; production AI operations and agent-service ownership remain gaps | Who owns evaluation, guardrails, and production AI monitoring? |
| R-008 | SQL and NoSQL databases | High | E-003, E-006, E-020 | Partial | confirmed | PostgreSQL professionally; Qdrant vector database in personal project. No general NoSQL operations claim | Which databases are in production? |
| R-009 | Message queues and distributed architectures | High | E-006, E-014; `source-of-truth/work-experience.md` | Partial | do not claim | Layered architecture/serverless evidence is related; no message-queue or large distributed-system ownership claim | Which queues and distributed-system responsibilities are in scope? |
| R-010 | AWS/Azure/GCP cloud-native engineering | High | E-014, E-018 | Partial | confirmed | AWS Lambda microservice; personal AWS deployment not portrayed as professional platform ownership | Which cloud services and operational responsibilities are required? |
| R-011 | Legacy modernization | High | E-010, E-013, E-017 | Strong | confirmed | MyTime payment migration and GreenAnt energy-dashboard migration | — |
| R-012 | Security and utility-sector compliance | High | E-006; `source-of-truth/relevant-experiences.md` onboarding/RLS | Partial | do not claim | Transaction integrity and validation are supported; no utility regulatory compliance expertise claimed | Which regulations and security practices must engineers already know? |
| R-013 | Fast delivery, quality, startup ownership | High | E-002, E-007, E-008, E-009 | Strong | confirmed | Under-three-week prototype, testing, Product collaboration, onboarding | — |
| R-014 | Excellent English; cross-functional communication | High | `source-of-truth/personal-professional-profile.md` Languages; E-008, E-009 | Strong | confirmed | English Full Professional in screening answers; collaboration evidence in experience | — |
| R-015 | University degree | Medium | `source-of-truth/personal-professional-profile.md` Education | Strong | confirmed | B.S. Computer Science, Universidade de Brasília | — |
| R-016 | ERP or power utilities industry | Medium | `source-of-truth/work-experience.md` GreenAnt, Gera Energia Brasil, GasHub | Partial | confirmed | Energy analytics, electric-energy dashboard, natural gas trading; no ERP or grid operations expertise claimed | How much utility operations knowledge is expected? |

### Resume Claim Traceability

- **Summary:** E-021; GasHub role and energy-sector companies in `work-experience.md`; E-002, E-003, E-020.
- **GasHub bullets:** E-002, E-003, E-006, E-022, E-007 respectively. E-022 is initial-entry size reduction, not total code or page-speed reduction; staging readiness results (E-023) are retained in interview preparation with scenario limits.
- **MyTime bullets:** E-010; NgRx in `work-experience.md`.
- **Twenty20 bullets:** E-012.
- **GreenAnt bullet:** E-013. The Lambda microservice is omitted from this resume pending reconciliation with the user's statement that Backend work was only at GasHub.
- **Universidade de Brasília/Gera Energia/Finatec bullets:** Corresponding sections of `work-experience.md`. Finatec customization uses only the Angular SPA, pending clarification of historical Java Backend scope.
- **Personal SEC-filings RAG bullets:** E-020; all explicitly personal/course work, dates unspecified.
- **Skills:** `personal-professional-profile.md`, `work-experience.md`, E-006, E-007, E-020. Python and Qdrant are explicitly marked personal-project experience. Go is not listed as an existing skill.

### Completion Checklist

- [x] All requirements and major responsibilities are represented.
- [x] Evidence points to the ledger or a canonical source file.
- [x] Every high-priority requirement has a treatment, gap, or question.
- [x] No unsupported requirement is used as a resume claim.
- [x] Selected resume claims reviewed against `guidelines/resume-tone-rubric.md`: Pass.
