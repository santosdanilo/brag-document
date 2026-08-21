---
name: manage-hiring-processes
description: Manage hiring process lifecycle — register new processes, track progress, prepare interviews, generate customized resumes, and close/archive completed processes. Use when the user mentions a new job opportunity, wants to register a hiring process, prepare for interviews, generate a resume for a specific process, or complete/close a process.
---

# Manage Hiring Processes

Full lifecycle management of hiring processes: from initial registration through interview preparation to closure and archival.

## When to Use

- User shares a recruiter message or job posting and wants to start tracking it
- User asks to register, create, or start a new hiring process
- User wants to complete, close, or archive a hiring process
- User wants to generate a customized resume for a specific process

## Workflow: Registering a New Process

### Step 1 — Create the process directory and tracking file

1. Create a directory at `hiring-processes/in-progress/{company}-{role}/` (kebab-case)
2. Create `{company}-{role}.md` inside with the structure below

### Step 2 — Tracking file structure

Use completed processes as reference (in `hiring-processes/completed/`). The file should contain:

- **Header**: Company name, position, start date, status, last update
- **Process Summary**: Initial contact details, recruiter info, platform
- **Job Posting Details**: Location, company type, team size, requirements
- **Company Information**: About, business model, culture
- **Job Requirements**: Technical skills, soft skills, responsibilities
- **Profile Match Analysis**: How the user's experience aligns with requirements (cross-reference `source-of-truth/work-experience.md` and `source-of-truth/relevant-experiences.md`)
- **Interview Preparation**: Key talking points, potential questions, topics to review (cross-reference `interview-preparation/` and `knowledge-base/`)
- **Questions to Ask**: Thoughtful questions about the role, team, and company
- **Interview Process**: (left empty — filled as the process progresses)

### Step 2.25 — Build the job-to-evidence matrix

Before drafting the profile-match analysis or `resume.yaml`:

1. Copy `hiring-processes/_templates/job-to-evidence-matrix.md` to `{company}-{role}/job-to-evidence-matrix.md`.
2. Extract the job requirements and responsibilities into the matrix.
3. Map each requirement to evidence IDs from `source-of-truth/evidence-ledger.md` or direct canonical source paths.
4. Mark the match as **Strong**, **Partial**, or **None** and classify the claim as **confirmed**, **needs confirmation**, or **do not claim**.
5. Give every high-priority requirement a resume treatment, an explicit gap, or a recruiter question.

Do not use a job-description keyword as evidence. A missing match is a gap, not an invitation to infer experience.

### Step 2.5 — Discover and verify evidence

Before drafting profile-match analysis, resume bullets, or a cover letter:

1. Read `source-of-truth/work-experience.md`, `source-of-truth/relevant-experiences.md`, `source-of-truth/storytellings.md`, and `source-of-truth/evidence-ledger.md`.
2. Compare the documented evidence with the completed job-to-evidence matrix and identify missing context, contribution, trade-offs, or results.
3. If important evidence is missing, interview the user one question at a time using the `grill-me` approach. Do not ask for facts already available in the repository.
4. For each question, provide a recommended interpretation based on the existing evidence and wait for the user's answer before asking the next question.
5. Structure confirmed stories internally as **Situation, Task, Action, Result (STAR)**. Emphasize the user's personal contribution and the resulting business or product impact.
6. Add reusable, confirmed facts to the evidence ledger with a source reference and approved resume wording.
7. Classify claims before using them: **confirmed**, **needs confirmation**, or **do not claim**. Never fill gaps with assumptions.

Use an adaptive question sequence rather than a fixed questionnaire. Ask only the next question needed to resolve the current gap, typically covering the problem, responsibility, decisions, actions, collaboration, constraints, evidence of results, and lessons learned.

### Step 3 — Generate a customized resume (when applicable)

If the process would benefit from a tailored resume, use the **Resume Generator** tool (bundled in the `generate-custom-resumes` skill):

Before creating `resume.yaml`, complete the matrix and check every selected claim against `source-of-truth/evidence-ledger.md` and `guidelines/resume-tone-rubric.md`.

1. Create `resume.yaml` inside the process directory with only the fields to override from the base resume (`resumes/resume-base.yaml`)
2. Use `id`-based matching to override specific companies/roles/bullets
3. Keep a traceable mapping from each tailored claim to a confirmed evidence ID or canonical source path in the job-to-evidence matrix
4. Follow the instructions in `.agents/skills/generate-custom-resumes/resume-generator/README.md` (section "Adding a New Hiring Process")
5. Generate the PDF:

```bash
cd .agents/skills/generate-custom-resumes/resume-generator && npm install
# Resume only
node src/index.js \
  --custom hiring-processes/in-progress/{company}-{role}/resume.yaml \
  --output hiring-processes/in-progress/{company}-{role}/resume.pdf

# Resume + cover letter (if cover-letter.md exists in the process directory)
node src/index.js \
  --custom hiring-processes/in-progress/{company}-{role}/resume.yaml \
  --output hiring-processes/in-progress/{company}-{role}/resume.pdf \
  --cover-letter hiring-processes/in-progress/{company}-{role}/cover-letter.md
```

**YAML customization reference:**

```yaml
title: Custom Title for This Opportunity

introduction: |
  Tailored introduction emphasizing relevant experience...

experiences:
  - id: company-id          # must match an id in resume-base.yaml
    roles:
      - id: role-id         # must match a role id under that company
        bullets:
          - Customized achievement bullet
        keySkills: Relevant, Skills, Here
```

Key points:
- Only include fields you want to override; everything else inherits from base
- Company IDs and role IDs are kebab-case and must match `resumes/resume-base.yaml`
- `keySkills` at company level and role level are independent
- Add a comment at the top of the YAML with the generation command for future reference

For standalone resume generation (not tied to a hiring process), see the **generate-custom-resumes** skill.

### Step 4 — Reply to the recruiter

If the user provides the initial recruiter message, generate a professional reply expressing interest and asking relevant follow-up questions.

## Workflow: Completing a Process

1. Move the process directory from `hiring-processes/in-progress/{process-name}/` to `hiring-processes/completed/{process-name}/`
2. Update the tracking file with:
   - **End date**
   - **Final status** (e.g., "Process completed", "Offer received", "Rejected", "Withdrawn")
   - **Outcome** details (offer terms, rejection reason, learnings, etc.)

## Reference Files

| Purpose | Path |
|---------|------|
| Work experience (source of truth) | `source-of-truth/work-experience.md` |
| Relevant experiences | `source-of-truth/relevant-experiences.md` |
| Storytellings (STAR format) | `source-of-truth/storytellings.md` |
| Evidence ledger | `source-of-truth/evidence-ledger.md` |
| Job-to-evidence matrix template | `hiring-processes/_templates/job-to-evidence-matrix.md` |
| Interview preparation templates | `interview-preparation/` |
| Resume base YAML | `resumes/resume-base.yaml` |
| Resume generator docs | `.agents/skills/generate-custom-resumes/resume-generator/README.md` |
| Resume writing tips | `guidelines/resume-tips.md` |
| Resume tone rubric | `guidelines/resume-tone-rubric.md` |
| Copywriting tips | `guidelines/copywriting-tips.md` |
| Completed processes (examples) | `hiring-processes/completed/` |
