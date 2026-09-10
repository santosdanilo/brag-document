---
name: message-linkedin-recruiters
description: Draft personalized LinkedIn outreach messages to recruiters for a specific hiring post or role, then send only after the user confirms the exact draft. Use when the user asks to message, contact, or reach out to a recruiter about an opportunity.
compatibility: Requires the project-scoped LinkedIn MCP server configured in opencode.json.
---

# Message LinkedIn Recruiters

Use this skill for **new recruiter outreach** tied to a specific hiring post or
formal job listing. The objective is a short, intentional message that makes
it obvious the candidate read the opportunity and has relevant evidence.

## Non-Negotiable Rules

- Draft before sending, even when the user says to send immediately.
- Send only after the user explicitly confirms the exact message text.
- Send only to the recruiter profile identified by the user or resolved from
  the relevant post.
- Support new outreach only. Do not treat a profile-based message as a reply
  to an existing LinkedIn conversation.
- Never connect, apply, register a hiring process, or send follow-ups unless
  the user separately requests those actions.
- Never invent experience, seniority, metrics, availability, location,
  language proficiency, compensation expectations, or interest in a company.
- Never claim that a message was sent unless the LinkedIn send tool confirms
  it.
- Keep the post permalink and any application URL as separate fields. Never
  use an application URL as evidence that a post was read.

## Source Of Truth

Before drafting, read the relevant canonical files:

- `source-of-truth/personal-professional-profile.md`
- `source-of-truth/work-experience.md`
- `source-of-truth/relevant-experiences.md`
- `source-of-truth/evidence-ledger.md` when available and relevant

Use only evidence documented in `source-of-truth/`. If the opportunity asks
for an important fact that is not documented, omit it or ask the user one
focused question. Do not infer experience from a keyword overlap.

## LinkedIn Retrieval Workflow

1. Identify the recruiter profile and the exact opportunity. Accept a
   canonical LinkedIn post URL, a LinkedIn job URL, or enough information to
   search for them.
2. Retrieve the post or job details using LinkedIn read tools. For a post,
   preserve the canonical `/feed/update/...` URL when LinkedIn exposes it.
3. Retrieve the recruiter profile with `linkedin_get_person_profile`, using
   `sections="posts"` only when the recruiter's recent activity helps verify
   the opportunity or personalize the message.
4. Confirm that the profile is messageable. Capture `profile_urn` when the
   profile response provides it.
5. Extract one or two specific details from the opportunity, such as the
   product context, role scope, technical challenge, geography, or contract
   type. Do not copy the whole job description into the message.
6. Compare those details with verified candidate evidence from the canonical
   files.
7. If the role, recruiter, or relevant post cannot be verified, say what is
   missing and draft only if the user explicitly wants a lower-confidence
   message.

## Message Principles

Base the message on Nicole Barra's post, [Rating Candidates DMs, Part
#3](https://www.linkedin.com/feed/update/urn:li:activity:7503055367602409472/).
The retrieved guidance supports these principles:

- Make the message genuinely personalized.
- Demonstrate attention to detail.
- Make it obvious that the candidate read the specific job post.

The carousel has ten pages, but its slide-specific content is not reliably
available through the LinkedIn MCP. Do not invent or attribute additional
rules to Nicole's post.

Prefer this structure:

1. Greeting using the recruiter's name.
2. Specific reference to the role and one detail from the post.
3. One or two directly relevant evidence-based qualifications.
4. A concise reason for reaching out.
5. One low-friction call to action, such as asking whether the profile could
  be relevant or whether the recruiter would like a resume.

Keep the first draft normally between LinkedIn's practical short-message
range, roughly 400 characters when that can be done without losing useful
context. Do not force an arbitrary limit when the opportunity requires a
clearer explanation; remove repetition first.

Avoid:

- Generic openings such as "I hope you are doing well" or "I am a perfect fit."
- Empty praise about the company or recruiter.
- A full resume pasted into the message.
- A list of every technology in the candidate profile.
- Unsupported claims such as "I have extensive experience" without evidence.
- Pressure, entitlement, desperation, or requests to bypass the application
  process.
- Asking several questions at once.
- Mentioning the applicant count, reactions, or comments as hiring evidence.

## Language And Tone

- Match the language of the hiring post when practical.
- Use English for an English-language role or when the recruiter's post is in
  English.
- Use Portuguese for a Portuguese-language opportunity unless the role clearly
  requires an English outreach message.
- Keep technical terms in English.
- Sound direct, warm, professional, and specific rather than promotional.

## Draft Review Output

Before any send operation, return:

```text
Recruiter: <name and LinkedIn profile URL>
Opportunity: <role and company/client>
Post: <canonical post URL or unavailable>
Application link: <URL or unavailable>
Personalization evidence: <specific post detail used>
Candidate evidence: <canonical source path and concise supported fact>

Draft:
<exact message text>

Reply with "confirm" to send this exact message, or provide edits.
```

If a required fact is missing, include a `Verification gap` line and do not
silently fill it with an assumption.

## Sending Workflow

After the user confirms the exact draft:

1. Re-check that the recipient username/profile URL is the intended recruiter.
2. Use `linkedin_send_message` with the exact approved text,
   `confirm_send=true`, and `profile_urn` when available.
3. Do not change wording, add a greeting, or append a resume link after
   confirmation.
4. Report the tool result accurately and include the recipient profile and
   opportunity. If sending fails, report the failure without claiming success.

If the user asks to reply to a recruiter's existing conversation, do not use
`linkedin_send_message` as a reply path. Explain that the available send tool
uses profile-based compose and may create a separate message; draft the reply
for the user instead.

## Example Draft Pattern

```text
Hi <Name>, I saw your post about the <Role> role at <Company>, especially the
focus on <specific detail>. I have documented experience with <relevant skill>
and <relevant outcome or scope>, including <concise evidence>. Would my
background be relevant for this opportunity? I would be happy to share my
resume.
```

Replace every placeholder with verified information before presenting the
draft. If no concrete result is documented, describe the responsibility
without manufacturing an outcome.
