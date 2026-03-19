# Work Experience

<!-- This can be considered the source of truth for my work history.
Use the format below for each position. Include metrics and impact where possible. -->

## GasHub (Jun 2025 - Present)
**Role:** Full Stack Engineer
**Stack:** React, Supabase, Deno, Drizzle ORM, Zod, NestJS, PostgreSQL, pgTAP, Sentry, Node.js, Testing Library, Playwright, Tailwind CSS, TypeScript

Early-stage startup building a natural gas trading platform with real-time matching between sellers and buyers.
- Developed a natural gas trading application with real-time matching between sellers and buyers, including instant notifications, leveraging **Supabase** as the backend.
- Delivered a functional prototype for market validation in under **three weeks** using **React** and AI agents.
- Refactored the codebase for maintainability and quality, and implemented comprehensive unit tests with **Testing Library** plus end-to-end tests using **Playwright**.
- Collaborated in refining requirements and validating business workflows to ensure product-market fit.
- Conducted a full performance analysis of the Products API, reducing response latency from **3010ms** to **132ms (−95.7%)** by parallelizing independent queries, merging RLS transactions, and profiling with **EXPLAIN ANALYZE**. Documented index recommendations to further cut database query time from ~198ms to ~2-5ms.
- Led architecture modernization by migrating from **Supabase JS client** to **Drizzle ORM** with **Deno**, enabling transaction support via the **Unit of Work** pattern. Introduced layered architecture with **Zod** validation at the API layer, business rules in use cases, and database queries isolated in repositories.
- Built the ProductsAvailablePage with **5 independently-filtered blocks**, each supporting infinite scroll, using **TanStack Virtual** for row virtualization to handle potentially thousands of rows across blocks without performance degradation.
- Conducted **three rounds of React 18 profiler analysis** on the trading page, diagnosing render bottlenecks through flame graphs and fiber-level metrics. Applied **React.memo**, **useCallback**, and CSS-only hover state (replacing `useState`) to eliminate cascade re-renders; reduced initial mount from **59.1ms to 1.8ms (−97%)** and per-block data-load commits from **13–31ms to under 2ms (−94%)**.

## MyTime (Apr 2022 - Mar 2025)
**Role:** Frontend Software Engineer
**Location:** Los Angeles, California
**Stack:** Angular, TypeScript, AngularJS, CoffeeScript, Jest, Testing Library

MyTime is a scheduling and point-of-sale (POS) platform used by businesses globally.
- Migrated a legacy **AngularJS** (CoffeeScript) payment system to a modern **Angular/TypeScript** stack, improving code reliability and enhancing maintainability. Implemented automated unit tests with **Jest** and **Testing Library**, achieving high test coverage and ensuring the system's stability post-migration.
- Delivered a seamless integration between legacy and modern systems, enabling uninterrupted operations during the transition phase.
- Rebuilt and optimized several core modules in the legacy POS system, significantly improving user experience and enabling a successful re-launch of the application. These optimizations enhanced performance and reduced the effort required for future maintenance, making the system more scalable for future updates.
- Implemented components ensuring the support of **W3C accessibility standards**, so even visually impaired users could operate on the system.

## Twenty20 Solutions (Jan 2022 - Mar 2022)
**Role:** Frontend Software Engineer
**Location:** Irving, TX
**Stack:** Angular, Jest, GitHub Actions, TypeScript

Twenty20 Solutions was building a browser-based desktop environment product. The project was cut off due to the pandemic.
- Architected a browser-based desktop environment using **Angular**, enabling dynamic interaction with modular "mini-applications" and ensuring long-term scalability through **SOLID** and **Clean Architecture** principles.
- Introduced **Jest** for unit testing and implemented **CI/CD** workflows with **GitHub Actions**, streamlining the development process and improving team velocity.
- Set up environment configurations and integrated linters, enforcing code quality standards and maintaining consistency across the development process.

## GreenAnt (Jan 2020 - Dec 2021)
**Role:** Frontend Software Engineer
**Stack:** Angular, AngularJS, Ionic, Webpack, AWS Lambda, GitLab CI, TypeScript

GreenAnt is an energy tech company providing electric energy data dashboards and mobile tools for invoice management.
- Developed a front-end architecture of an electric energy data dashboard using **Angular**, creating reusable UI components and improving real-time data visualization.
- Led the migration from **AngularJS** to **Angular**, integrating both environments and implementing **Webpack**-based bundling, which enabled the gradual upgrade of legacy code while maintaining stability.
- Developed a PDF generation microservice with **AWS Lambda** and implemented **CI/CD** pipelines using **GitLab CI**, streamlining the deployment process and accelerating release cycles.
- Launched a mobile app using **Ionic** for invoice payment and data monitoring, significantly enhancing customer accessibility and providing a faster, more intuitive experience.

## Universidade de Brasília (Aug 2018 - Aug 2020)
**Role:** Frontend Software Developer
**Location:** Brasília
**Stack:** Angular, Angular Material, Next.js, Docker, mobile-first development

Academic research and development role at the university, focused on making government data accessible to the public.
- Developed a mobile-first dashboard to simplify access to government data, ensuring clarity and accessibility for the general public.
- Focused on UX principles to enhance data discoverability and engagement.

## Gera Energia Brasil (Feb 2019 - Dec 2019)
**Role:** Frontend Software Engineer
**Location:** Brasília
**Stack:** Angular, PrimeNG, Jasmine, CI/CD, UX

Gera Energia Brasil provides energy analytics solutions for enterprise clients.
- Led the design and development of a dashboard for energy consumption analytics, empowering enterprise clients to monitor and reduce energy costs.
- Applied **Angular** and UX techniques to improve usability and responsiveness.

## Finatec - Fundação de Empreendimentos Científicos e Tecnológicos (May 2017 - Jun 2018)
**Location:** Brasília

### Frontend Software Developer (May 2017 - Jan 2018)
**Stack:** Angular

- Created a SPA with **Angular** for managing internal data for military administration, applying UX best practices for ease of use.

### Junior Java Developer (Dec 2017 - Jun 2018)
**Stack:** Java, Docker, microservices

Finatec is a Brazilian scientific and technological foundation supporting government and military projects.
- Worked on **Java EE** backend systems and learned DevOps fundamentals, including **Docker** and microservices architecture.
