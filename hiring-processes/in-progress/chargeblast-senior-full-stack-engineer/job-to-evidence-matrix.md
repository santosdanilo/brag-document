# Job-to-Evidence Matrix

## Process

- **Company:** Chargeblast
- **Position:** Senior Full Stack Engineer
- **Source job description:** [Amplify IT careers listing](https://www.amplifyit.io/careers/chargeblast/full-stack-engineer), supplied on 2026-09-05
- **Last reviewed:** 2026-09-05
- **Status:** Ready for resume

## Requirement Mapping

| ID | Requirement or responsibility | Priority | Evidence IDs / source paths | Match | Claim status | Resume treatment or gap | Recruiter question |
|---|---|---|---|---|---|---|---|
| R-001 | Build robust web applications for payment and chargeback operations | High | E-010; `source-of-truth/work-experience.md` - GasHub | Partial | confirmed | Lead with the business-critical payment-system modernization; describe trading workflows without claiming chargeback experience. | Does the role focus more on merchant-facing workflows, internal operations, or both? |
| R-002 | Own features end to end across APIs, data layers, and user interfaces | High | E-002, E-005, E-006, E-007; `source-of-truth/work-experience.md` - GasHub | Strong | confirmed | Emphasize end-to-end prototype delivery, API integration, layered data access, atomic operations, and automated tests. | How are responsibilities split between product, frontend, and backend engineers? |
| R-003 | Build high-performance, data-rich dashboards and tools for large datasets | High | E-003, E-004; `source-of-truth/work-experience.md` - Gera Energia Brasil, Universidade de Brasília | Strong | confirmed | Highlight virtualized, filtered, infinite-scroll trading views and measured API/rendering performance improvements. Do not claim exports unless confirmed. | What are the largest datasets and performance targets for the dashboards? |
| R-004 | Automate complex manual financial workflows | High | E-006, E-010, E-014 | Partial | confirmed | Show atomic multi-step payment operations and decoupled invoice PDF generation; keep chargeback workflow automation as a gap. | Which manual financial workflows are the first automation priorities? |
| R-005 | Production backend engineering with Go and/or Node.js, APIs, services, and background processing | High | E-005, E-006, E-014; `source-of-truth/work-experience.md` - GasHub stack | Strong for Node.js; none for Go | confirmed | Position Node.js/Deno backend architecture, API integration, AWS Lambda, and transaction boundaries. Do not claim Go or background-processing ownership. | How is backend work divided between Go and Node.js, and how much background processing is involved? |
| R-006 | 3+ years of full-stack development on complex tools or operational dashboards | High | E-001, E-002, E-003, E-004, E-006; `source-of-truth/work-experience.md` | Partial | confirmed | State 7+ years building web applications and emphasize recent end-to-end full-stack ownership; do not state 3+ years of full-stack experience. | How is the team defining full-stack scope for this position? |
| R-007 | Strong TypeScript and Angular or similar modern frontend framework experience | High | E-001, E-002, E-010, E-013; `source-of-truth/personal-professional-profile.md` | Strong | confirmed | Put TypeScript and Angular in the title, summary, selected roles, and skills; retain React as recent full-stack experience. |  |
| R-008 | PostgreSQL, schema design, optimized queries, and data management | High | E-003, E-006; `source-of-truth/work-experience.md` - GasHub | Strong for query optimization and data access; partial for schema design | confirmed | Highlight PostgreSQL profiling, `EXPLAIN ANALYZE`, query parallelization, transaction consolidation, and layered repositories. Do not claim broad schema ownership. | How much ownership does this role have over schema design, migrations, and production database operations? |
| R-009 | Financial correctness and data integrity | High | E-006, E-010; `source-of-truth/storytellings.md` - Modernizing a Backend Architecture to Enable Transactions | Partial | confirmed | Emphasize atomic multi-step operations and stable payment workflows; do not claim chargeback reconciliation or financial-controls ownership. | What correctness, reconciliation, idempotency, and audit requirements govern the payment workflows? |
| R-010 | Redis | Medium | No documented evidence | None | do not claim | Keep Redis out of the resume. | How central is Redis to caching, queues, or workflow coordination? |
| R-011 | AWS | Medium | E-014; `source-of-truth/personal-professional-profile.md` - Skills | Partial | confirmed | Include AWS Lambda, Amazon S3, and serverless deployment experience; do not imply broad AWS platform ownership. | Which AWS services and deployment responsibilities are in scope? |
| R-012 | Remote work eligibility for the United States | High | No professional evidence required | None | needs confirmation | Keep location and work authorization out of the resume; confirm directly before applying. | What location, work authorization, and time-zone requirements apply to remote candidates? |

## Completion Checklist

- [x] All requirements and major responsibilities are represented.
- [x] Evidence points to the ledger or a canonical source file.
- [x] Every high-priority requirement has a treatment, gap, or question.
- [x] `needs confirmation` and `do not claim` items are excluded from resume claims.
- [x] Resume claims were reviewed against `guidelines/resume-tone-rubric.md`.
