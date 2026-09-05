# Evidence Ledger

This is a reusable index of career claims that may be used in resumes, cover letters, hiring-process analyses, and interview preparation.

The canonical source remains the files in `source-of-truth/`. This ledger improves traceability; it does not replace those files. When a conflict exists, the canonical source wins.

## Claim Status

- **confirmed**: Directly supported by the source-of-truth files or explicitly confirmed by Danilo.
- **needs confirmation**: Plausible based on available context, but missing an important detail such as scope, ownership, or result.
- **do not claim**: Unsupported, contradicted, or too vague to use professionally.

## Reusable Claims

| ID | Claim | Status | Source | Evidence and limits | Approved resume wording |
|---|---|---|---|---|---|
| E-001 | 7+ years building web and mobile applications | confirmed | `source-of-truth/personal-professional-profile.md` - Summary; `source-of-truth/work-experience.md` | Work history spans May 2017 to present. | Full Stack Engineer with 7+ years of experience building web applications. |
| E-002 | GasHub trading prototype delivered under three weeks | confirmed | `source-of-truth/relevant-experiences.md` - Rapid Prototype Delivery for Market Validation; `source-of-truth/storytellings.md` | React prototype covered real-time matching, notifications, and core trading workflows. | Delivered a real-time trading platform prototype in under 3 weeks using React and Supabase. |
| E-003 | GasHub Products API performance improved | confirmed | `source-of-truth/relevant-experiences.md` - Products API Performance Optimization; `source-of-truth/storytellings.md` | Warm latency reached approximately 132 ms across 100 requests; cold latency dropped 45%. | Cut Products API warm latency by 95.7% through request profiling, query parallelization, transaction consolidation, and PostgreSQL optimization. |
| E-004 | GasHub React rendering performance improved | confirmed | `source-of-truth/relevant-experiences.md` - Virtualized Trading Page; `source-of-truth/storytellings.md` | Initial mount improved 97%; per-block data-load commits improved 94% after three profiling rounds. | Reduced initial React mount time by 97% and per-block data-load commits by 94% through profiler-led refactors. |
| E-005 | GasHub frontend and backend API integration | confirmed | `source-of-truth/work-experience.md` - GasHub; user-confirmed API integration detail | Analyzed backend contracts, proposed response structures, and introduced an adapter layer to isolate payload transformations during API structure migration. Do not claim a specific API count or reliability metric. | Integrated frontend and backend APIs by analyzing contracts and introducing an adapter layer that isolated payload transformations during API structure migration. |
| E-006 | GasHub backend architecture modernization | confirmed | `source-of-truth/relevant-experiences.md` - Backend Architecture Modernization; `source-of-truth/storytellings.md` | Migrated from Supabase JS client to Drizzle ORM on Deno; added Zod, use cases, repositories, and Unit of Work. | Established a layered backend architecture with Drizzle ORM, Deno, Zod validation, repositories, use cases, and the Unit of Work pattern. |
| E-007 | GasHub automated testing | confirmed | `source-of-truth/work-experience.md` - GasHub; `resumes/resume-base.yaml` | Implemented Testing Library unit tests and Playwright end-to-end tests. | Established automated quality coverage with Testing Library unit tests and Playwright end-to-end tests. |
| E-008 | GasHub onboarding and knowledge transfer | confirmed | `source-of-truth/work-experience.md` - GasHub; `source-of-truth/relevant-experiences.md` | Documented business rules, matching engine, RLS policies, and layered backend architecture. | Onboarded engineers by documenting platform business rules and technical architecture. |
| E-009 | GasHub shared Product and Engineering design workflow | confirmed | `source-of-truth/relevant-experiences.md` - Shared Product and Engineering Design Workflow | Used Pencil.dev as a shared source of truth for design-system artifacts. | Created a shared Product and Engineering design workflow with Pencil.dev to align implementation with design-system artifacts. |
| E-010 | MyTime payment-system migration | confirmed | `source-of-truth/relevant-experiences.md` - AngularJS to Angular Migration; `source-of-truth/storytellings.md` | Migrated AngularJS/CoffeeScript payment functionality to Angular/TypeScript without downtime; achieved high test coverage. | Modernized a business-critical payment system from AngularJS and CoffeeScript to Angular and TypeScript without disrupting operations. |
| E-011 | MyTime accessibility implementation | confirmed | `source-of-truth/work-experience.md` - MyTime; `source-of-truth/storytellings.md` | Implemented W3C accessibility standards across key user-facing screens. | Improved usability across customer workflows by implementing W3C accessibility standards. |
| E-012 | Twenty20 modular architecture and quality foundation | confirmed | `source-of-truth/relevant-experiences.md` - Browser-Based Desktop Environment Architecture; `source-of-truth/storytellings.md` | Designed Angular system using SOLID and Clean Architecture; introduced Jest, GitHub Actions, and linters. | Architected a modular browser-based application with SOLID, Clean Architecture, Jest, and GitHub Actions quality gates. |
| E-013 | GreenAnt zero-downtime frontend migration | confirmed | `source-of-truth/relevant-experiences.md` - Legacy System Upgrade with Zero Downtime; `source-of-truth/storytellings.md` | Integrated AngularJS and Angular through Webpack while production remained operational. | Completed a zero-downtime AngularJS to Angular migration using Webpack dual-environment bundling. |
| E-014 | GreenAnt serverless PDF microservice | confirmed | `source-of-truth/relevant-experiences.md` - PDF Generation Microservice on AWS Lambda | Built an AWS Lambda microservice and automated deployments with GitLab CI. | Decoupled PDF generation into an AWS Lambda microservice and automated deployments with GitLab CI. |
| E-015 | Finatec Java and Docker experience | confirmed | `source-of-truth/work-experience.md` - Finatec | Worked on Java EE backend systems and Docker/microservices fundamentals. Do not present this as recent or primary experience. | Contributed to Java EE backend systems using Docker and microservices architecture. |
| E-016 | GasHub npm monorepo and dependency linking | confirmed | `source-of-truth/work-experience.md` - GasHub; user confirmation | Worked with an npm monorepo, including dependency linking between packages. | Worked with an npm monorepo and linked dependencies between packages. |

## Maintenance Rules

1. Add a ledger entry when a new career fact is confirmed and likely to be reused.
2. Link every entry to a canonical source or to an explicit user confirmation recorded in the relevant process.
3. Do not upgrade a claim's status based only on a job description, inferred scope, or a generated draft.
4. Update approved wording when the source-of-truth wording or evidence changes.
5. Review `needs confirmation` entries before using them in an application document.
