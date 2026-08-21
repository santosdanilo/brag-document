# Job-to-Evidence Matrix

Use one copy of this file at `hiring-processes/in-progress/{company}-{role}/job-to-evidence-matrix.md`.

## Process

- **Company:**
- **Position:**
- **Source job description:**
- **Last reviewed:**
- **Status:** Draft / Ready for resume / Needs clarification

## Instructions

- Extract requirements from the job description before drafting the profile match or resume.
- Use evidence IDs from `source-of-truth/evidence-ledger.md` whenever possible.
- Use direct source paths when a relevant claim is not yet in the ledger.
- Mark unsupported requirements as gaps; do not convert them into resume claims.
- Every high-priority requirement must end with a resume treatment, a gap, or a recruiter question before `resume.yaml` is created.

## Requirement Mapping

| ID | Requirement or responsibility | Priority | Evidence IDs / source paths | Match | Claim status | Resume treatment or gap | Recruiter question |
|---|---|---|---|---|---|---|---|
| R-001 |  | High / Medium / Low |  | Strong / Partial / None | confirmed / needs confirmation / do not claim |  |  |

## Match Definitions

- **Strong:** Direct, recent, and sufficiently specific evidence exists.
- **Partial:** Related evidence exists, but the tool, scope, recency, or outcome differs.
- **None:** No evidence is documented. Keep it as a gap or question.

## Completion Checklist

- [ ] All requirements and major responsibilities are represented.
- [ ] Evidence points to the ledger or a canonical source file.
- [ ] Every high-priority requirement has a treatment, gap, or question.
- [ ] No `needs confirmation` or `do not claim` item is used as a resume claim.
- [ ] Resume claims are reviewed against `guidelines/resume-tone-rubric.md`.
