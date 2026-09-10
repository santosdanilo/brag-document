---
name: search-linkedin-jobs
description: Search and rank LinkedIn Jobs and Posts for React, Angular, Frontend, Full Stack, and Product Engineer roles, especially USA or EMEA opportunities that explicitly accept candidates in LATAM. Use when the user asks to find, filter, compare, or monitor LinkedIn job opportunities.
compatibility: Requires the project-scoped LinkedIn MCP server configured in opencode.json.
---

# Search LinkedIn Jobs

Use this skill only for job-discovery work. Never apply, send a message, connect with a recruiter, or alter a hiring-process record unless the user separately requests that action.

## Candidate Profile

Before ranking results, read the canonical profile and experience files:

- `source-of-truth/personal-professional-profile.md`
- `source-of-truth/work-experience.md`
- `source-of-truth/relevant-experiences.md`
- `resumes/fullstack-2026-01/resume.yaml` when a resume-level comparison is useful

Treat `source-of-truth/` as authoritative. Use only skills, employers, dates, responsibilities, and metrics found there. Do not invent a match or infer experience from a generic technology keyword.

The default target profile is React/Angular/full-stack, with particular attention to React, Angular, TypeScript, Next.js, Node.js, NestJS, PostgreSQL, Supabase, AWS, testing, performance, APIs, and technical leadership. Angular is a primary stack, not an adjacent match: the canonical profile lists Angular as expert-level and the work history contains multiple Angular roles plus AngularJS-to-Angular migrations.

## Search Workflow

1. Search formal listings with `linkedin_search_jobs` using several focused queries, including `React`, `Angular`, `Full Stack Engineer`, `Frontend Engineer`, `Angular Developer`, and `Product Engineer`. Use `work_type="remote"`, `date_posted="past_week"`, and `sort_by="date"`. Search `United States`, `Europe`, `Middle East`, `Africa`, and `Remote` as separate location queries when appropriate.
2. Search informal hiring posts with short, focused queries rather than long keyword chains. Use several of these query families with `date_posted="past-week"`: `hiring React LATAM`, `hiring Angular LATAM`, `"full stack" LATAM`, `"frontend" Brazil remote`, `"product engineer" LATAM`, `"Node.js" LATAM hiring`, `"React" "Latin America"`, `"Angular" "Latin America"`, `contratando React internacional`, `contratando Angular internacional`, `buscamos React LATAM`, and `buscamos Angular LATAM`. Validate relevance against the actual post text; LinkedIn keyword matching is broad.
3. Use up to five concurrent subagents for non-overlapping search or verification work when delegation is available. Suggested assignments are USA formal listings, EMEA formal listings, React/Angular/frontend posts, full-stack/product posts, and verification/link recovery. The coordinator must provide each worker the same search timestamp, 72-hour cutoff, candidate evidence, and output schema, then deduplicate all results centrally. Do not dispatch duplicate query families.
4. Deduplicate formal results by job ID or canonical URL. Deduplicate posts by the direct LinkedIn post URL first, then by attached job URL or application URL as internal fallback keys when the post URL is unavailable. Never treat an application URL as the post URL or display it as the post link.
5. Fetch full details for promising formal listings with `linkedin_get_job_details`.
6. Verify the exact posting age. LinkedIn exposes a `past_week` filter, not a reliable 72-hour filter, so retain only listings and posts published within the last 72 hours unless the user explicitly changes the window.
7. Inspect the employer location and candidate eligibility separately. A US or EMEA employer is not enough: require explicit evidence that candidates located in LATAM are accepted.
8. For formal listings, retain a confirmed result only when the applicant metric is numeric and below 100. Treat `applicants` and `people clicked apply` as different LinkedIn metrics, report the exact label, and do not call either one an exact candidate count.
9. Put posts and formal listings without an applicant metric into separate unverified sections. Never imply that a post's reactions or comments are application counts.
10. Exclude or flag listings that require US work authorization, US residency, a specific non-LATAM country, or an unavailable location. Do not treat `remote` alone as proof of LATAM eligibility.
11. Rank retained formal listings and posts independently against verified resume evidence, prioritizing React or Angular and TypeScript relevance, full-stack scope, seniority, remote compatibility, explicit LATAM eligibility, recency, and applicant volume where available.

## Retrieval And Verification Rules

- Use no more than five concurrent LinkedIn workers or subagents. Parallelize independent query families, not repeated requests for the same search. If LinkedIn tools share one browser session, serialize browser navigation and detail retrieval while allowing independent result analysis in parallel; never let concurrent navigation overwrite another worker's result.
- Validate every formal-search response before using it. Confirm that the response URL retained the requested location, `f_TPR`, remote work type and sort order. Reject or separately flag responses containing `Jobs you may be interested in`, `Top job picks`, `Expand your search`, dropped filters, or a different location than requested.
- Treat a timeout as a retrieval failure, not an empty result. Retry once with one narrower query, `max_pages=1`, and reduced concurrency. If it still fails, record the query as unavailable and continue with successful searches. If the LinkedIn MCP is disconnected, stop and report that clearly.
- For posts, store these fields separately whenever available: `post_url`, `application_url`, `poster`, `company_or_client`, `posted_age`, `post_date_basis`, `employer_location`, `client_location`, `latam_evidence`, `applicant_metric`, `resume_match`, and `verification_gaps`. `application_url` is internal metadata only and must not be displayed as the post link.
- Recover the direct post URL by opening or clicking the LinkedIn post result through read-only navigation. The post body or search response does not need to expose a URL; use the URL LinkedIn returns after opening the clickable post. Prefer direct `/feed/update/` or `/posts/` URLs when available, but do not require a specific permalink format. Do not use an application URL, attached job URL, recruiter profile URL, or search-results URL as the post link. If the post cannot be opened or LinkedIn does not return a direct post URL, report `post URL unavailable`.
- Distinguish original publication from reposting. `Reposted 2 hours ago` is not proof that the underlying post was published within 72 hours. If the original publication timestamp cannot be established, do not place the item in confirmed results; mark it as a promising lead with `original age unverified` or exclude it when the strict cutoff is required.
- Evaluate geography as three separate facts: employer headquarters/location, job/listing location, and explicit candidate eligibility. A listing shown in the United States or a LATAM country does not establish the employer's headquarters. A US/EMEA client mentioned in a post does not establish the recruiting company or client identity unless the source makes it explicit.
- Preserve LinkedIn's exact applicant label and value: `Applicants`, `people clicked apply`, `Candidates who clicked apply`, or another displayed label. Do not convert clicks, reactions, comments, or reposts into applicants. A formal listing without a numeric metric is unverified, even when it otherwise looks relevant.
- Compare requirements against canonical evidence only. Flag unsupported requirements such as a specific language level, country authorization, framework, backend language, years of experience, or people-management history. Do not infer experience from a related technology or generic title.
- Keep formal listings and posts in separate rankings. Formal listings require date, eligibility, and numeric applicant-metric verification for confirmation. Posts are ranked by explicit LATAM eligibility, verified employer/client geography, stack fit, seniority fit, source quality, recency, and availability of a directly recovered LinkedIn post URL; applicant count remains `unavailable` unless an attached formal listing provides it.

## Search Rules

- Keep the user's default geography precise: USA or EMEA-based opportunities that accept people in LATAM. Do not silently broaden this to any job advertised in a LATAM country.
- Keep the default recency precise: the last 3 days means the last 72 hours from the time of the search.
- Keep the default applicant threshold strict: fewer than 100 means `<100`; exactly 100 does not qualify.
- Prefer roles with React or Angular in the requirements. Treat React and Angular as primary target stacks. Include other frontend roles only when the overlap is substantial and label the reason.
- Distinguish `confirmed match`, `promising but unverified`, and `excluded` instead of hiding uncertainty.
- If eligibility, date, or applicant count cannot be verified, say so explicitly and lower confidence.
- Do not expose salary or other sensitive personal information unless the user asks for it.
- Use the same language as the user's request. Keep technology names and LinkedIn metric labels in English.

## Output Format

Return a compact report with these sections:

### Confirmed Matches

Use a table with:

`Priority | Role / company | Employer location | Posted | Applicant metric | LATAM evidence | Resume match | Link`

Only include formal listings that pass the date, eligibility, and `<100` applicant checks.

### Promising Formal Leads

List formal listings missing one verification. State exactly what is unverified, especially original age, applicant count, employer geography, or LATAM eligibility.

### Hiring Posts

Rank relevant hiring posts independently from formal listings. Use this structure when possible:

`Priority | Role / company or client | Poster | Posted | Post link | LATAM evidence | Resume match | Verification gaps`

Display the direct LinkedIn post URL recovered by opening or clicking the post result in the `Post link` field. The URL does not need to be visible in the post body or search response. Do not display an application URL, attached job URL, recruiter profile URL, or search-results URL in that field. If the post cannot be opened or no direct LinkedIn post URL is returned, write `post URL unavailable` explicitly. Report `Applicant metric: unavailable` for posts without a formal LinkedIn applicant metric, and never use reactions or comments as a proxy.

### Excluded

List notable results and one concise exclusion reason, such as `older than 72 hours`, `100 or more applicants`, `US work authorization required`, `not React/Angular/full-stack`, or `LATAM eligibility not stated`.

### Recommended Next Actions

Suggest which opportunities deserve manual review or application. Do not perform the application or contact action.

End with the search timestamp and a brief note that LinkedIn applicant metrics are platform-reported proxies, not guaranteed candidate counts.

## Failure Handling

- If the LinkedIn MCP is unavailable or disconnected, report that clearly and stop. Do not install a third-party scraper or request API credentials automatically.
- If a search returns too many results, narrow by date, remote work type, role keywords, and location before increasing pagination. Prefer short query families over one broad query.
- If a response drops a requested filter or falls back to recommendations, do not use those results as if they came from the requested search. Re-run a narrower supported query or mark the result as unverified.
- If a post cannot be opened or LinkedIn does not return a direct post URL, state `post URL unavailable` and do not display the application link. Do not substitute an application URL, attached job URL, search-results URL, short-link, or poster's profile URL.
- If no listing passes all filters, report the strongest near-matches and the specific failed criterion instead of relaxing the filters silently.
