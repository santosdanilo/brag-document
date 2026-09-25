# Job-to-Evidence Matrix

## Process

- **Company:** Confidential US-based sales-engagement SaaS company (name not provided)
- **Position:** Senior Full-Stack Engineer / Primary Product Engineer
- **Source job description:** Supplied by Danilo on 2026-09-25; captured in `job-description.md`
- **Last reviewed:** 2026-09-25
- **Status:** Closed at user's request
- **End date:** 2026-09-25

## Outcome

Process closed at the user's request. No hiring outcome was recorded.

## Requirement Mapping

| ID | Requirement or responsibility | Priority | Evidence IDs / source paths | Match | Claim status | Resume treatment or gap | Recruiter question |
|---|---|---|---|---|---|---|---|
| R-001 | 8+ years senior full-stack experience and end-to-end product ownership | High | E-001, E-002, E-005, E-006, E-007; `source-of-truth/work-experience.md` - GasHub | Partial | confirmed | Use verified experience duration and describe specific end-to-end GasHub delivery; do not claim 8+ years as a senior full-stack engineer or sole ownership of a whole platform. Clarify full-stack scope and seniority. | How does the company define primary-engineer ownership and seniority? |
| R-002 | Senior TypeScript and Node.js across modern and legacy systems | High | E-005, E-006, E-010, E-013; `source-of-truth/personal-professional-profile.md` - Skills; `source-of-truth/work-experience.md` - GasHub | Partial | needs confirmation | Emphasize TypeScript, backend architecture, and AngularJS/legacy modernization. Node.js is listed in the profile and GasHub stack, but recent service implementation is documented on Deno; clarify direct Node.js backend work before claiming depth. | How much of the role is Node.js services versus frontend and AWS operations? |
| R-003 | Strong current Angular experience; product uses Angular 16 | High | E-010, E-012, E-013; `source-of-truth/work-experience.md` - MyTime, Twenty20, GreenAnt | Strong for Angular; version recency needs confirmation | needs confirmation | Feature Angular and TypeScript plus legacy-to-modern Angular migrations; do not claim Angular 16 or a specific current version without confirmation. | Which Angular 16 patterns or upgrades are most important to the team? |
| R-004 | Daily AWS operations across ECS Fargate, Lambda, SQS, Aurora, SES, CodePipeline, and CodeBuild | High | E-014; `source-of-truth/personal-professional-profile.md` - Skills; `source-of-truth/work-experience.md` - GreenAnt | Partial | needs confirmation | Current confirmed resume treatment: AWS Lambda PDF-generation microservice and CI/CD deployment only. Clarify hands-on services, operations, and infrastructure changes before adding more. | Which AWS services are in active daily use, and what is the on-call/operations scope? |
| R-005 | Root-cause live production incidents for paying customers (memory/heap, API edge cases, queue backlogs) | High | E-003, E-004; `source-of-truth/storytellings.md` - API and React profiling stories | Partial | needs confirmation | Use measured API and frontend root-cause analysis; do not imply incidents in a paid production system or heap/queue debugging until confirmed. | What incident types and production reliability responsibilities occur most often? |
| R-006 | Daily Claude Code use and custom AI-agent workflows | High | E-002; `source-of-truth/work-experience.md` - GasHub; `source-of-truth/relevant-experiences.md` - AI-assisted delivery | Partial | needs confirmation | Current evidence supports using AI agents to accelerate a prototype and reviewing AI-generated design/code artifacts. Clarify Claude Code frequency and personally built workflows; do not claim these yet. | What Claude Code workflows are expected or already established? |
| R-007 | Automate manual processes and stabilize product operations | High | E-002, E-006, E-014; `source-of-truth/work-experience.md` - GasHub and GreenAnt | Partial | confirmed | Describe product workflow delivery, atomic multi-step operations, and Lambda decoupling; direct automation of recurring manual operations is not documented. | Which manual tasks are currently handled by people and are the first automation targets? |
| R-008 | Clarify incomplete specifications, make estimates, and deliver to estimates | High | `source-of-truth/work-experience.md` - GasHub, lines 15 and 22; `source-of-truth/work-experience.md` - MyTime | Partial | needs confirmation | Use documented requirements refinement and technical feasibility recommendations; no estimation accuracy or delivery-estimate evidence is documented. Ask user for a specific example before claiming. | What planning and estimation process does the team use? |
| R-009 | Scope and build new products from scratch | High | E-002, E-012; `source-of-truth/storytellings.md` - prototype and browser-desktop stories | Strong | confirmed | Highlight the real-time sales prototype delivered in under three weeks and modular Angular product architecture. |  |
| R-010 | Work autonomously in a small/lean team and care for customer impact | High | E-002, E-003, E-006, E-008; `source-of-truth/work-experience.md` - GasHub | Partial | confirmed | Present concrete startup delivery, performance diagnosis, backend modernization, and onboarding; avoid claiming sole or primary ownership of the platform. | How many engineers currently support the product and how is ownership shared? |
| R-011 | Integrate third-party services and handle API edge cases | High | E-005; `source-of-truth/work-experience.md` - GasHub API integration | Partial | confirmed | Show frontend/backend contract integration and adapter-layer work. Third-party provider integrations and edge-case handling are not documented. | Which external services and mailbox providers are most business-critical? |
| R-012 | React | Medium | E-002, E-004; `source-of-truth/work-experience.md` - GasHub | Strong | confirmed | Include recent React product development and profiler-led performance optimization. |  |
| R-013 | Email deliverability: DKIM, DMARC, SPF, warmup, blocklists, sender reputation | Medium | No documented evidence | None | do not claim | Keep off resume; treat as a domain gap. | Which deliverability systems and operational metrics are in scope? |
| R-014 | Gmail API, Microsoft Graph, IMAP/SMTP, and OAuth | Medium | No documented evidence | None | do not claim | Keep off resume; treat as a domain gap. | Which mailbox-provider integrations are currently supported? |
| R-015 | PHP/Laravel, Stripe/billing, Linux/Ansible, or sales-tech/martech | Low | E-010 for payment workflows; `source-of-truth/work-experience.md` - MyTime | Partial for payment workflows only; none for named tools/domains | confirmed | Use MyTime payment-system modernization accurately; do not claim Stripe, billing ownership, PHP/Laravel, Linux/Ansible, or sales-engagement domain experience. | Is billing code in scope, and which payment providers are used? |
| R-016 | Public open-source work, personal agent/MCP tooling, or local developer community | Low | No documented evidence | None | do not claim | Keep off resume unless the user confirms relevant work. |  |
| R-017 | Remote LATAM and strong US business-hours overlap | High | User's application intent; schedule not confirmed | None | needs confirmation | Do not state time-zone availability until confirmed. | What exact US-hours overlap is required? |

## Completion Checklist

- [x] All requirements and major responsibilities are represented.
- [x] Evidence points to the ledger or a canonical source file where available.
- [ ] Every high-priority requirement has a final resume treatment, confirmed gap, or recruiter question.
- [ ] No `needs confirmation` or `do not claim` item is used as a resume claim.
- [ ] Selected resume claims reviewed against `guidelines/resume-tone-rubric.md`.
- [ ] Resolve material evidence questions before writing `resume.yaml`.
