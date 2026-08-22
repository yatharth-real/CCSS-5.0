# Mission Record

**Purpose.** Define the outcome, operating conditions, state, and proof for substantial work.

**When to use.** Use this record when work has multiple dependent steps, meaningful risk, or more than one material artifact. Do not use it as a transcript.

## Instructions
Capture observable facts and label assumptions. Record capability limits before planning around them. Keep state current and do not mark a mission complete merely because a command was issued.

## Structure / schema
A mission has an objective, desired outcome, constraints, success criteria, capability map, workflow, milestones, risks, blockers, artifacts, decisions, and verification.

## Completed example

### Mission name
Upgrade CCSS templates

### Status
`completed`

### Objective
Replace placeholder records with copy-ready templates without expanding the core prompt unnecessarily.

### Desired outcome
A new developer can understand, copy, fill, and validate every operational record.

### Constraints and success criteria
- Keep `SKILL.md` concise and portable.
- Preserve permission and evidence rules.
- Every template includes guidance, an example, and a blank copy-ready section.

### Assumptions
- The host can read and write Markdown files.
- No external service is required.

### Capability map
| Capability | Status | Interface | Limits | Permission | Confidence |
|---|---|---|---|---|---|
| File editing | available | host filesystem | sandbox scope | WRITE | high |
| Markdown validation | available | local scripts | not semantic proof | READ/EXECUTE | medium |

### Skills, tools, and dependencies
- Skill: `ccss-5-0`
- Dependency: existing reference protocols

### Workflow
`inspect → design → implement → validate → review → deliver`

### Milestones and state
- Completed: audit, design, implementation, validation
- Current: completed
- Blockers: none

### Risks
Over-documentation could make the core skill harder to load.

### Artifacts and provenance
- `SKILL.md`: edited from the existing project.
- `templates/*.md`: generated from this specification.

### Verification
All required templates exist; headings contain instructions and examples; internal references resolve.

### Final result
CCSS now has a usable starter-document system.

## Copy-ready template

<!-- Replace every bracketed value. Remove instructional comments when finished. -->

### Mission name
[Short unique name]

### Status
`proposed` | `ready` | `active` | `paused` | `blocked` | `awaiting_decision` | `verifying` | `completed`

### Objective
<!-- State the exact problem or task. -->
[Objective]

### Desired outcome
<!-- Describe the observable result. -->
[Outcome]

### Constraints and success criteria
- Constraints: [limits, deadlines, format, budget, permissions]
- Success criteria: [measurable checks]

### Assumptions
- [Assumption, labelled for later verification]

### Capability map
| Capability | Status | Interface | Limits | Permission | Confidence |
|---|---|---|---|---|---|
| [name] | [available/degraded/fallback/unavailable] | [interface] | [limits] | [READ/WRITE/EXECUTE/EXTERNAL/DESTRUCTIVE] | [low/medium/high] |

### Required Skills, tools, and dependencies
- Skills: [names or none]
- Tools: [interfaces or none]
- Dependencies: [dependencies]

### Workflow
[Sequence or graph; identify independent parallel nodes and decision points.]

### Milestones and state
- Completed: [work]
- Current: [work]
- Next: [work]
- Blockers: [blockers or none]

### Risks
- [Risk, likelihood, impact, mitigation]

### Artifacts and provenance
- [Artifact, source, version, status]

### Decisions
- [Decision ID and selected option]

### Verification plan and result
- Planned checks: [checks]
- Results: [evidence]

### Final result
[Concise result or limitation]
