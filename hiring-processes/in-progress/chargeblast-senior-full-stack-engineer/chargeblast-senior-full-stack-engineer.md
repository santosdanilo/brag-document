# Chargeblast - Senior Full Stack Engineer

**Company:** Chargeblast
**Position:** Senior Full Stack Engineer
**Start Date:** 2026-09-05
**Status:** Resume prepared; awaiting recruiter response
**Last Update:** 2026-09-05

---

## Process Summary

- **Source:** [Amplify IT careers listing](https://www.amplifyit.io/careers/chargeblast/full-stack-engineer)
- **Application type:** Direct application
- **Employment type:** Full time
- **Location:** Remote to United States of America

---

## Job Posting Details

- **Industry:** Fintech
- **Level:** Senior
- **Team size:** Unknown
- **Core stack:** Go, Node.js, PostgreSQL, TypeScript, Angular, Redis, AWS

---

## Company Information

Chargeblast builds payment and chargeback management software for merchants. The company focuses on fraud prevention, revenue recovery, payment strategy optimization, and automating manual financial operations with reliable, data-driven systems.

---

## Job Requirements

### Technical Skills

- Go and/or Node.js backend APIs, services, and background processing
- TypeScript and Angular or a similar modern frontend framework
- PostgreSQL schema design, query optimization, and data management
- Redis and AWS
- High-performance interfaces for large datasets, including tables, filters, exports, and charts
- Financial correctness and data integrity

### Responsibilities

- Build and maintain web applications for payment and chargeback operations.
- Own features across API design, data layers, and user interfaces.
- Build data-rich operational dashboards and tools.
- Automate complex manual financial workflows.

---

## Profile Match Analysis

Strong match for TypeScript, Angular, Node.js, PostgreSQL performance work, payment workflows, data-rich interfaces, and transaction-safe backend architecture.

The main gaps are direct Go, Redis, chargeback-domain, background-processing, broad AWS-platform, and chargeback reconciliation experience. The resume deliberately positions documented Node.js and AWS Lambda experience without implying unsupported technology or domain ownership.

| Requirement | Match | Evidence |
|---|---|---|
| Payment and critical business workflows | Strong | MyTime payment-system modernization and NgRx checkout/payment flows; E-010 |
| Chargeback domain | None | No direct chargeback experience is documented; keep as an interview discovery area |
| End-to-end full-stack delivery | Strong | GasHub prototype, API integration, layered backend, database performance, and automated tests; E-002, E-005, E-006, E-007 |
| Data-rich dashboards and large datasets | Strong | GasHub virtualized trading view plus Angular energy and government dashboards; E-003, E-004 |
| Node.js backend engineering | Strong | GasHub stack and backend architecture modernization with Drizzle ORM, Deno, and transaction support; E-006 |
| Go | None | No documented experience; do not claim |
| TypeScript and Angular | Strong | MyTime, Twenty20, GreenAnt, and GasHub; E-001, E-010, E-012, E-013 |
| PostgreSQL optimization | Strong | `EXPLAIN ANALYZE`, query parallelization, transaction consolidation, and composite-index recommendation; E-003 |
| Data integrity and atomicity | Strong | Unit of Work pattern enabled atomic multi-step operations; E-006 |
| Redis | None | No documented experience; do not claim |
| AWS | Partial | AWS Lambda PDF-generation microservice and CI/CD deployment; E-014 |
| 3+ years of full-stack experience | Partial | Seven-plus years building web applications, with recent documented end-to-end full-stack work; do not state 3+ years of full-stack experience |

---

## Interview Preparation

### Key Talking Points

1. Explain the MyTime payment migration as an incremental modernization that preserved operations, improved maintainability, and added high test coverage.
2. Connect GasHub's trading platform to Chargeblast's need for reliable operational tooling: real-time workflows, API integration, large datasets, filtering, virtualization, and measurable performance work.
3. Use the Products API investigation to demonstrate root-cause analysis across application execution, database queries, RLS transactions, and network round-trips.
4. Explain the Unit of Work migration as a response to data-integrity risk: multiple related writes became atomic instead of leaving partial state after a failure.
5. Discuss the AWS Lambda invoice-PDF service as an example of decoupling a financial workflow and making deployment independent.
6. Be explicit about direct experience with Node.js and AWS Lambda, while treating Go, Redis, chargebacks, and background-processing systems as areas to ramp up or clarify.

### Potential Interview Questions

- How would you design an idempotent chargeback or payment workflow?
- How do you preserve financial correctness when a multi-step operation fails midway?
- Walk through the PostgreSQL/API performance investigation at GasHub.
- How would you build a dashboard that remains responsive with millions of records?
- What trade-offs would you consider between Go and Node.js for APIs and background workers?
- What is your experience with Redis, queues, caching, and asynchronous processing?
- How would you approach chargeback lifecycle states, reconciliation, auditability, and retries?
- How do you validate API contracts when frontend and backend structures change together?

### Topics to Review

- Chargeback lifecycle, representment, dispute evidence, reconciliation, and payment idempotency
- PostgreSQL indexing, query plans, transactions, isolation levels, constraints, and audit trails
- Go fundamentals and production API patterns
- Redis caching, queues, locks, and failure modes
- AWS services commonly used for APIs, workers, queues, and observability
- Angular architecture for data-heavy tables, filtering, pagination, and export workflows
- System design for reliable financial workflows and background processing

---

## Questions to Ask

- Which parts of the product are built in Go versus Node.js, and what backend ownership is expected from this role?
- What are the highest-priority payment, fraud-prevention, and chargeback workflows today?
- How are idempotency, reconciliation, auditability, and financial correctness tested and monitored?
- What dataset sizes and response-time targets drive the dashboard architecture?
- How are exports, charts, asynchronous jobs, and long-running operations implemented?
- What role does Redis play in the current architecture?
- Which AWS services are used, and how much responsibility does this role have for deployment and operations?
- What does the engineering team expect during the first 90 days?
- What location and work-authorization requirements apply to remote candidates?

---

## Interview Process

_(to be filled as the process progresses)_

---

## Application Materials

- `job-description.md` - captured job description
- `job-to-evidence-matrix.md` - requirement and evidence mapping
- `resume.yaml` - tailored resume source
- `resume.pdf` - generated tailored resume
