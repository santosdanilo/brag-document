# Sigma Software - Senior Software Engineer

**Company:** Sigma Software
**Position:** Senior Software Engineer
**Start Date:** 2026-09-07
**Status:** Closed at user's request
**End Date:** 2026-09-07
**Last Update:** 2026-09-07

---

## Outcome

Process closed at the user's request. No hiring outcome was recorded.

## Process Summary

- **Source:** Job description supplied by the user
- **Application type:** To be defined
- **Engagement:** PJ / B2B contractor
- **Location:** Brazil, Argentina, Colombia, or Mexico; 100% remote
- **Compensation:** USD

The opportunity is for an international Revenue & Reporting platform used by Finance and Accounting teams. The role is backend-focused and combines TypeScript, PostgreSQL, ORM-based data access, cloud, CI/CD, architecture, troubleshooting, testing, and end-to-end ownership.

## Job Posting Details

- **Industry:** Revenue, reporting, Finance, and Accounting software
- **Level:** Senior
- **Team size:** Unknown
- **Core stack:** TypeScript, PostgreSQL, Prisma, AWS, CI/CD, NestJS, Turborepo, React, Next.js
- **Benefits:** 20 days of PTO, national holidays, and company-provided laptop

## Company Information

The supplied description does not include additional company information. Sigma Software is presented as the contracting company for an international client project.

## Job Requirements

### Technical Skills

- Strong backend TypeScript
- PostgreSQL or relational databases
- ORM usage, preferably Prisma
- Software architecture and scalability strategies
- AWS or other cloud experience
- CI/CD
- NestJS, Turborepo, monorepos, React, and Next.js as relevant stack or differentiators

### Domain and Delivery Expectations

- Build scalable systems for critical financial data.
- Implement complex business logic and reporting workflows.
- Contribute to testing, troubleshooting, and scalability improvements.
- Make technical decisions with autonomy.
- Demonstrate ownership and deliver projects end to end.
- Collaborate daily in English with an international team.

## Profile Match Analysis

The tailored resume positions a strong match for backend TypeScript, PostgreSQL performance and data access, ORM-based architecture through Drizzle, software architecture, AWS Lambda, CI/CD, React, monorepos, financial-adjacent workflows, troubleshooting, and end-to-end ownership. `NestJS` is included only as a documented skills keyword because project-specific scope is not described in the source-of-truth files.

The main documented gaps are direct `Prisma`, `Turborepo`, and Revenue & Reporting / Accounting platform experience. AWS evidence is specific to Lambda and serverless deployment rather than broad cloud-platform ownership. These items will remain explicit gaps unless the user confirms additional experience.

Primary evidence:

- **GasHub:** Modernized the backend with Drizzle ORM, Deno, Zod, repositories, use cases, and Unit of Work; improved PostgreSQL-backed API warm latency by 95.7%; and delivered a real-time trading platform prototype.
- **GasHub:** Worked with an npm monorepo, linked package dependencies, integrated APIs, implemented automated tests, and led onboarding around complex business rules and architecture.
- **GreenAnt:** Built an AWS Lambda PDF-generation microservice and GitLab CI deployment pipeline for invoice workflows.
- **MyTime:** Modernized a business-critical payment system from AngularJS/CoffeeScript to Angular/TypeScript without disrupting operations.
- **Twenty20 Solutions:** Applied SOLID and Clean Architecture and introduced Jest and GitHub Actions CI/CD.

See `job-to-evidence-matrix.md` for requirement-level mapping and claim limits.

## Interview Preparation

### Key Talking Points

1. Explain the GasHub backend modernization as a response to missing transaction support: Drizzle ORM, layered boundaries, repositories, use cases, and Unit of Work enabled atomic multi-step operations.
2. Walk through the Products API performance investigation: request waterfall, `EXPLAIN ANALYZE`, sequential RLS transactions, `Promise.all`, transaction consolidation, and the composite-index recommendation.
3. Connect the natural gas trading platform and MyTime payment system to the need for reliable business rules, data integrity, and critical financial workflows, without claiming direct Revenue & Reporting experience.
4. Explain how the npm monorepo and linked dependencies transfer to Turborepo concepts, while being explicit that Turborepo itself is not documented.
5. Use the AWS Lambda invoice-PDF microservice and GitLab CI pipeline to demonstrate cloud deployment and CI/CD experience.
6. Prepare a concrete explanation of ownership: feasibility assessment, architecture decisions, API contracts, implementation, automated tests, performance validation, and onboarding.

### Potential Interview Questions

- How would you design a Revenue & Reporting backend around correctness, auditability, and reproducible calculations?
- How would you model reporting periods, revenue adjustments, and late-arriving financial data in PostgreSQL?
- How do you choose transaction boundaries for a workflow that writes multiple related records?
- Walk through the GasHub API performance investigation and the measurements used to validate the changes.
- What trade-offs would you consider between Prisma and Drizzle for a TypeScript backend?
- How would you structure a NestJS application using modules, providers, validation, repositories, and use cases?
- How would you scale reporting queries and long-running data-processing workflows?
- What is your experience with Turborepo, npm workspaces, dependency linking, and monorepo boundaries?
- How do you test complex business rules and protect financial data integrity?
- Tell us about a project you led from technical discovery through delivery and validation.

### Topics to Review

- Prisma compared with Drizzle: schema management, migrations, transactions, relation loading, and query performance
- NestJS modules, dependency injection, providers, pipes, guards, interceptors, testing, and application boundaries
- PostgreSQL transactions, isolation levels, constraints, indexes, query plans, migrations, and reporting query strategies
- Revenue recognition concepts, reporting periods, adjustments, reconciliation, audit trails, and idempotency
- Scalable data processing: queues, batch jobs, retries, idempotency, backpressure, and observability
- AWS services for APIs, workers, scheduled processing, storage, and monitoring
- Turborepo task pipelines, caching, workspace boundaries, and CI optimization
- System design fundamentals from `interview-preparation/training-interviews-hard-skills.md`, especially scalability, database design, API design, queues, and event-driven architecture
- Behavioral preparation from `interview-preparation/training-interviews-soft-skills.md`, using the API bottleneck and backend modernization stories in `source-of-truth/storytellings.md`

## Questions to Ask

- Is Prisma a strict requirement, or is strong TypeScript ORM experience with Drizzle acceptable?
- How much of the backend is currently built with NestJS, and what would this role own?
- Is the codebase a Turborepo monorepo? How are packages, deployments, and CI pipelines organized?
- Which revenue, reporting, accounting, reconciliation, or audit workflows are most critical today?
- How are financial calculations validated, versioned, audited, and corrected when source data changes?
- What are the expected scale, latency, and freshness targets for reporting and data processing?
- Which AWS services are used, and how much infrastructure and operational ownership is expected?
- How are background jobs, retries, idempotency, and observability handled?
- What does end-to-end ownership look like for this team, from discovery through production support?
- What are the contract duration, payment schedule, expected working hours, and English-overlap requirements?

## Interview Process

_(to be filled as the process progresses)_

## Application Materials

- `job-description.md` - captured job description
- `job-to-evidence-matrix.md` - requirement and evidence mapping
- `resume.yaml` - tailored resume source
- `resume.pdf` - generated tailored resume
- `recruiter-response.md` - draft email to the recruiter
