# Indeed - Software Engineer, JavaScript Ecosystem Modernization

**Company:** Indeed
**Contracting company:** Aspire IT Services, an Astek Group company
**Position:** Software Engineer, JavaScript Ecosystem Modernization
**Start Date:** 2026-09-05
**Status:** Resume prepared; awaiting recruiter response
**Last Update:** 2026-09-05

---

## Process Summary

- **Recruiter:** Ehab, Executive Director at Aspire IT Services
- **Source:** Direct recruiter message
- **Engagement:** Long-term contractor opportunity supporting Indeed
- **Location:** Fully remote, LATAM
- **Schedule:** Flexible hours with U.S. Central Time overlap

The recruiter contacted Danilo because of his documented experience migrating a legacy AngularJS and CoffeeScript payment system to Angular and TypeScript and performing a gradual AngularJS-to-Angular migration with Webpack-based bundling.

---

## Job Posting Details

The available description is preliminary. The initiative focuses on modernizing Indeed's JavaScript ecosystem across more than 2,000 applications, including upgrades to current JavaScript versions and a package-manager migration from npm to pnpm.

### Known Responsibilities

- Migrate applications to current JavaScript versions.
- Support the package-manager migration from npm to pnpm.
- Troubleshoot issues encountered during application migrations.
- Collaborate effectively across teams involved in the modernization program.

### Critical Requirements

- Strong hands-on JavaScript experience.
- Application version-migration experience.
- Hands-on pnpm experience.
- Migration troubleshooting skills.
- Effective cross-team collaboration.
- Availability for flexible hours overlapping U.S. Central Time.

---

## Profile Match Analysis

### Strong Matches

- **MyTime:** Migrated a business-critical payment system from **AngularJS/CoffeeScript** to **Angular/TypeScript** incrementally, allowing old and new systems to coexist and completing the transition without disrupting operations.
- **GreenAnt:** Led a production **AngularJS-to-Angular** migration using **Webpack**-based bundling so modules could be upgraded gradually while the application remained operational.
- **GreenAnt:** Evaluated each imported **AngularJS** library's legacy module and package-compatibility constraints and adapted its integration for **Webpack**, allowing older dependencies to coexist with modern **Angular** code during the gradual migration.
- **GasHub:** Worked with an **npm monorepo**, including dependency linking between packages, providing relevant package-management and workspace experience.
- **Troubleshooting:** Diagnosed frontend rendering and backend API bottlenecks at GasHub through systematic profiling and iterative validation.
- **Collaboration:** Documented technical architecture, onboarded engineers, and aligned Product and Engineering through shared design artifacts.

### Gaps and Constraints

- No direct professional, personal, or experimental **pnpm** experience is documented or claimed.
- npm monorepo and dependency-linking experience is transferable but should not be presented as pnpm experience.
- Experience coordinating migration work across thousands of applications is not documented; do not imply Indeed-scale migration ownership.
- U.S. Central Time overlap availability requires confirmation before committing to a schedule.

---

## Interview Preparation

### Key Talking Points

1. Explain the MyTime migration as a risk-managed transition: incremental implementation, coexistence between legacy and modern systems, automated tests, and no operational disruption.
2. Explain the GreenAnt migration strategy: Webpack-based bundling, module-by-module upgrades, continuous delivery, and avoiding a big-bang rewrite.
3. Connect npm monorepo and dependency-linking experience to transferable package-management concepts such as workspace boundaries, dependency resolution, linking, lockfiles, and reproducible installs.
4. Be explicit that pnpm has not been used directly, then explain a concrete ramp-up approach based on comparing npm workspaces with pnpm workspaces and validating migration behavior in CI.
5. Use GasHub performance investigations as evidence of systematic troubleshooting: reproduce, profile, isolate root causes, make incremental changes, and verify outcomes.

### Topics to Review

- pnpm workspace configuration and `pnpm-workspace.yaml`
- pnpm's content-addressable store and symlinked `node_modules` layout
- Strict dependency resolution and phantom-dependency failures
- npm lockfile to `pnpm-lock.yaml` migration
- Workspace protocols, package linking, overrides, and peer dependencies
- CI caching, frozen lockfiles, install reproducibility, and rollback strategies
- Codemods and automation strategies for large-scale JavaScript upgrades

### Potential Interview Questions

- How would you migrate an npm workspace to pnpm safely?
- What migration failures might pnpm's stricter dependency isolation expose?
- How would you design and roll out an automated migration across thousands of repositories or applications?
- How do you keep legacy and modern JavaScript code operational during an incremental migration?
- How do you distinguish application defects from package-manager, lockfile, build-tool, or dependency-resolution failures?
- How would you measure migration progress, compatibility, and rollback safety?

---

## Questions to Ask

- Are the 2,000 applications stored in a monorepo, multiple monorepos, or independent repositories?
- Which JavaScript runtimes, frameworks, build tools, and current npm versions are in scope?
- Is pnpm experience a strict screening requirement, or is strong npm workspace and migration experience acceptable with a short ramp-up period?
- What automation already exists for package-manager and JavaScript-version migrations?
- What are the most common migration failures the team is encountering?
- How will application ownership and cross-team coordination work during the migration?
- What Central Time overlap window is required, and is it fixed or flexible by project phase?
- What are the contract duration, compensation range, payment terms, and expected start date?

---

## Interview Process

Not provided.

---

## Application Materials

- `resume.yaml` - tailored resume source
- `resume.pdf` - generated tailored resume
- `recruiter-response.md` - draft response to Ehab
