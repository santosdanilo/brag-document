# Job-to-Evidence Matrix

## Process

- **Company:** Confidential US-based sales-engagement SaaS company (name not provided)
- **Position:** Senior Full-Stack Engineer / Primary Product Engineer
- **Source job description:** Supplied by Danilo on 2026-09-25; captured in `job-description.md`
- **Last reviewed:** 2026-09-25
- **Status:** Ready for resume with explicit gaps

## Requirement Mapping

| ID | Requirement or responsibility | Priority | Evidence IDs / source paths | Match | Claim status | Resume treatment or gap | Recruiter question |
|---|---|---|---|---|---|---|---|
| R-001 | 8+ years as a senior full-stack engineer; end-to-end ownership | High | E-001, E-002, E-005, E-006, E-007; `source-of-truth/work-experience.md` - GasHub | Partial | confirmed | State documented 7+ years building applications and highlight recent full-stack delivery; do not claim 8+ years in a senior full-stack role or sole platform ownership. | How does the company define primary-engineer ownership and seniority? |
| R-002 | Senior TypeScript and Node.js across modern and legacy codebases | High | E-005, E-006, E-010, E-013; `source-of-truth/personal-professional-profile.md` - Skills; `source-of-truth/work-experience.md` - GasHub | Partial | confirmed | Feature TypeScript, Node.js/NestJS from the profile, backend architecture work, and AngularJS modernization. Clarify any production Node service examples in interviews; do not imply GasHub's Deno backend was Node.js. | How much of the role is Node.js services versus frontend and AWS operations? |
| R-003 | Strong current Angular experience; product uses Angular 16 | High | E-010, E-012, E-013; `source-of-truth/work-experience.md` - MyTime, Twenty20, GreenAnt | Strong for Angular; version recency unverified | confirmed | Highlight Angular/TypeScript and incremental AngularJS migrations; do not state Angular 16 or a specific current version. | Which Angular 16 patterns or upgrades are most important to the team? |
| R-004 | Daily AWS operations across ECS Fargate, Lambda, SQS, Aurora, SES, CodePipeline, and CodeBuild | High | E-014, E-018; `source-of-truth/work-experience.md` - GreenAnt | Partial | confirmed | Include professional AWS Lambda microservice/deployment and a separately identified personal web-app setup using EC2, CodeBuild, CodePipeline, S3, and CloudFront. ECS/Fargate, SQS, Aurora, SES, and daily paid-customer production operations are gaps. | Which AWS services are in active daily use, and what is the on-call/operations scope? |
| R-005 | Resolve production incidents affecting paying customers, including heap/API/queue issues | High | E-003, E-004; `source-of-truth/storytellings.md` - API and React profiling stories | Partial | confirmed | Use measured API and frontend root-cause analysis; do not claim paid-production incident response or heap/queue debugging. | What incident types and reliability responsibilities occur most often? |
| R-006 | Daily Claude Code use and custom AI-agent workflows | High | E-002; `source-of-truth/work-experience.md` - GasHub; `source-of-truth/relevant-experiences.md` - AI-assisted delivery | Partial | confirmed | Highlight AI-agent-assisted prototype delivery and review of AI-generated artifacts; do not claim Claude Code or custom agent workflows. | What Claude Code workflows are expected or already established? |
| R-007 | Automate manual processes and stabilize product operations | High | E-002, E-006, E-014; `source-of-truth/work-experience.md` - GasHub and GreenAnt | Partial | confirmed | Describe real-time workflow delivery, atomic business operations, and Lambda decoupling; direct automation of recurring manual operations is not documented. | Which manual tasks are the first automation targets? |
| R-008 | Clarify incomplete specs, estimate work, and deliver reliably | High | `source-of-truth/work-experience.md` - GasHub, lines 15 and 22 | Partial | confirmed | Show requirements refinement and technical-feasibility recommendations; do not claim estimation accuracy. | What planning and estimation process does the team use? |
| R-009 | Scope and build new products from scratch | High | E-002, E-012; `source-of-truth/storytellings.md` - prototype and browser-desktop stories | Strong | confirmed | Highlight the real-time sales prototype delivered in under three weeks and modular Angular product architecture. |  |
| R-010 | Operate autonomously in a small/lean team with customer impact | High | E-002, E-003, E-006, E-008; `source-of-truth/work-experience.md` - GasHub | Partial | confirmed | Present concrete startup delivery, performance diagnosis, backend modernization, and onboarding; avoid claiming sole platform ownership. | How many engineers currently support the product, and how is ownership shared? |
| R-011 | Third-party service integrations and API edge cases | High | E-005; `source-of-truth/work-experience.md` - GasHub API integration | Partial | confirmed | Keep the frontend/backend API adapter as an interview example; do not present it as a third-party integration. The tailored resume prioritizes stronger measured outcomes. | Which external services and mailbox providers are most business-critical? |
| R-012 | React | Medium | E-002, E-004; `source-of-truth/work-experience.md` - GasHub | Strong | confirmed | Include recent React product development and profiler-led performance optimization. |  |
| R-013 | Email deliverability: DKIM, DMARC, SPF, warmup, blocklists, sender reputation | Medium | No documented evidence | None | do not claim | Keep off resume; treat as a domain gap. | Which deliverability systems and operational metrics are in scope? |
| R-014 | Gmail API, Microsoft Graph, IMAP/SMTP, and OAuth | Medium | No documented evidence | None | do not claim | Keep off resume; treat as a domain gap. | Which mailbox-provider integrations are supported? |
| R-015 | PHP/Laravel, Stripe/billing, Linux/Ansible, or sales-tech/martech | Low | E-010; `source-of-truth/work-experience.md` - MyTime | Partial for payment workflows only | confirmed | Use MyTime payment-system modernization; do not claim Stripe, billing ownership, PHP/Laravel, Linux/Ansible, or sales-engagement experience. | Is billing code in scope, and which payment providers are used? |
| R-016 | Public open source, personal agent/MCP tooling, or local developer community | Low | No documented evidence | None | do not claim | Keep off resume unless confirmed. |  |
| R-017 | Remote LATAM and strong US business-hours overlap | High | User's application intent; availability not confirmed | None | needs confirmation | Do not state schedule availability until confirmed. | What exact US-hours overlap is required? |

## Completion Checklist

- [x] All requirements and major responsibilities are represented.
- [x] Evidence points to the ledger or a canonical source file where available.
- [x] Every high-priority requirement has a resume treatment, explicit gap, or recruiter question.
- [x] Unconfirmed and unsupported claims are excluded from resume content.
- [x] Selected resume claims reviewed against `guidelines/resume-tone-rubric.md`.
