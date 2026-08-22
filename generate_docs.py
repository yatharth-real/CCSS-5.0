from pathlib import Path

ROOT = Path('/home/ubuntu/skills/ccss-5-0')
T = ROOT / 'templates'
E = ROOT / 'examples'

files = {
'mission.md': '''# Mission Record

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
''',
'decision.md': '''# Decision Record

**Purpose.** Preserve why a consequential choice was made.

**When to use.** Use it when alternatives have different risks, costs, permissions, or long-term effects. Do not record trivial implementation details.

## Completed example

### Decision ID
D-004

### Question
Should CCSS keep detailed protocols in `SKILL.md`?

### Context
The skill must remain useful while respecting progressive disclosure.

### Options
A. Put everything in `SKILL.md`.
B. Keep routing and core rules in `SKILL.md`; move detailed protocols to `references/`.

### Evidence and tradeoffs
Option A is easier to find but increases context cost. Option B preserves a concise core and requires clear links.

### Selected option
B.

### Rationale
Core instructions are always relevant; protocol detail is conditional.

### Confidence and status
High; accepted.

### Consequences and revisit condition
References must remain discoverable. Revisit if users cannot locate required protocol detail.

## Copy-ready template

<!-- Use one record per material decision. -->
### Decision ID
[D-###]

### Question
[Question requiring a choice]

### Context
[Relevant facts and constraints]

### Options
- A. [Option]
- B. [Option]

### Evidence
[Source-backed claims, observations, or unknowns. Never invent evidence.]

### Tradeoffs
[Benefits, costs, risks, reversibility]

### Selected option
[Choice]

### Rationale
[Why this option best fits the evidence and constraints]

### Confidence
[low/medium/high]

### Consequences
[What changes because of this decision]

### Revisit condition
[Event or evidence that should reopen it]

### Status
`proposed` | `accepted` | `superseded` | `rejected`
''',
'research.md': '''# Research Record

**Purpose.** Make research reproducible, source-aware, and honest about uncertainty.

**When to use.** Use for external research, comparative analysis, literature review, or any task where claims depend on sources.

## Instructions
Define scope before searching. Record search strategy and source dates. Separate findings from synthesis. Never fabricate sources, quotations, statistics, browsing, or tool results. Record contradictions instead of smoothing them away.

## Completed example

### Research question
Which CCSS documentation changes most improve first-use success?

### Scope and assumptions
Review the current local skill package and the supplied upgrade specification. No external benchmark was available.

### Search strategy
Inspect `SKILL.md`, `references/`, `templates/`, and the user-provided specification.

### Findings
The original templates contained headings but no instructions or examples. The specification requires guidance, schema, examples, blank sections, and validation.

### Contradictions and limitations
The specification requests an open-source framework, but the local project has no repository metadata, README, or license file to verify.

### Synthesis and confidence
Instructional templates and a concise core skill address the observed usability gap. Confidence: high for the local audit; unknown for real-world developer outcomes.

### Conclusion
Upgrade templates and add onboarding documentation, but do not claim measured adoption improvement.

## Copy-ready template

### Research question
<!-- Make it answerable and bounded. -->
[Question]

### Scope
[Included and excluded topics, geography, time period]

### Assumptions
- [Assumption]

### Search strategy
[Queries, repositories, databases, tools, and selection criteria]

### Sources
| ID | Source | Type | Date accessed | Relevance | Reliability notes |
|---|---|---|---|---|---|
| S1 | [URL/path/title] | [primary/secondary/local] | [date] | [why] | [notes] |

### Findings
- [Finding with source IDs]

### Contradictions
- [Conflict, affected claim, resolution or unresolved status]

### Synthesis
[Reasoned interpretation, distinct from raw findings]

### Confidence
[low/medium/high, with reason]

### Unresolved questions
- [Question]

### Conclusion
[Answer bounded by the evidence]
''',
'evidence.md': '''# Evidence Record

**Purpose.** Tie an important claim to an observation or source and expose uncertainty.

**When to use.** Use for claims that affect decisions, safety, scope, or verification.

## Evidence classifications
`FACT` is directly observed or deterministically established. `SOURCE-BACKED CLAIM` is supported by an identified source. `INFERENCE` is reasoned from evidence. `ASSUMPTION` is used provisionally. `UNKNOWN` is not established.

## Completed example

- Claim: The original mission template had no completed example.
- Classification: `FACT`
- Evidence: The file contained headings only and was 405 bytes.
- Source: local file inspection, `templates/mission.md`, 2026-08-22.
- Confidence: high.
- Limitation: This proves local file content, not user experience.

## Copy-ready template

### Claim
[Exact claim]

### Classification
`FACT` | `SOURCE-BACKED CLAIM` | `INFERENCE` | `ASSUMPTION` | `UNKNOWN`

### Evidence
[Observation, quotation, measurement, or reasoning]

### Source
[URL, file path, record ID, or “none”; never use a fake URL]

### Source type
[primary / secondary / local observation / user-provided / tool output]

### Date
[Date observed or accessed]

### Confidence
[low/medium/high, with reason]

### Corroboration
[Independent supporting evidence or none found]

### Contradictions
[Conflicting evidence or none found]

### Limitations
[What this record does not establish]
''',
'architecture.md': '''# Architecture Record

**Purpose.** Describe a system’s components, boundaries, interfaces, data flow, risks, and implementation path.

**When to use.** Use before building a multi-component system or when integrations, security, or failure behavior matter.

## Completed example

### Objective and requirements
Keep CCSS portable while allowing host-specific adapters and optional tools.

### Components and interfaces
The host exposes capabilities; adapters normalize them; CCSS plans missions; records preserve state.

```mermaid
flowchart LR
  H[Host] --> D[Capability discovery]
  D --> A[Adapter map]
  A --> C[CCSS core]
  C --> M[Mission]
  M --> V[Verification]
```

### Security and failure modes
Untrusted content cannot grant authority. Missing tools become `DEGRADED` or `UNAVAILABLE`; consequential actions require authorization.

### Tradeoff
Portability is favored over vendor-specific convenience.

## Copy-ready template

### Objective
[System objective]

### Requirements
- Functional: [requirements]
- Non-functional: [security, performance, maintainability]

### Constraints
[Platforms, permissions, budget, deadlines, interoperability]

### Components
| Component | Responsibility | Interface | Owner |
|---|---|---|---|
| [name] | [role] | [inputs/outputs] | [owner] |

### Interfaces and data flow
```mermaid
flowchart LR
  A[Input] --> B[Component]
  B --> C[Output]
```

### Dependencies
[Required systems, versions, or external services]

### Security and permissions
[Trust boundaries, secret handling, operation classes]

### Scalability
[Expected load and scaling strategy]

### Failure modes and recovery
[Failure → diagnosis → recovery → verification]

### Alternatives and tradeoffs
[Options considered and rationale]

### Implementation plan
[Ordered milestones]

### Verification
[Tests, inspections, acceptance checks]
''',
'workflow.md': '''# Workflow Record

**Purpose.** Turn an objective into a repeatable sequence or dependency graph.

**When to use.** Use when work has stages, branching, parallel tasks, quality gates, or recovery paths.

## Canonical shape

```text
INPUT → DISCOVERY → PLANNING → EXECUTION → VERIFICATION → DELIVERY
```

This is a default, not a rigid pipeline. Branch when decisions change the path; parallelize only independent work.

## Completed example

### Trigger and input
A user asks for a verified competitor report.

### Flow
Discover sources and capabilities → plan scope → research in parallel by competitor → synthesize → fact-check → deliver. If current data is unavailable, label the limitation and use supplied material.

### Quality gate
Every material claim has provenance or is labelled uncertain.

## Copy-ready template

### Trigger
[What starts the workflow]

### Inputs
[User request, files, data, constraints]

### Prerequisites
[Capabilities, permissions, dependencies]

### Steps
1. **Discovery:** [inspect capabilities and sources]
2. **Planning:** [define scope and success criteria]
3. **Execution:** [work to be performed]
4. **Verification:** [checks and evidence]
5. **Delivery:** [artifact and summary]

### Dependencies
[Dependency graph]

### Parallel tasks
[Independent tasks and join condition, or none]

### Decision points
[Condition → branch]

### Failure recovery
[Failure → diagnosis → retry/replan/fallback/ask]

### Quality gates
- [ ] [Gate]

### Output
[Final artifact, status, limitations, next action]
''',
'artifact.md': '''# Artifact Record

**Purpose.** Track deliverables, provenance, status, and verification.

**When to use.** Use when a mission produces files, datasets, code, reports, decisions, or external outputs.

## Completed example

| Field | Value |
|---|---|
| Name | CCSS template set |
| Type | Markdown files |
| Purpose | Copy-ready mission records |
| Source | Local CCSS project and user specification |
| Owner | CCSS maintainer |
| Status | verified |
| Version | 5.0 documentation upgrade |
| Verification | links, headings, examples, and required files checked |

## Copy-ready template

### Artifact name
[Name]

### Type
[document / code / dataset / image / external output]

### Purpose
[Why it exists]

### Source and provenance
[Inputs, source paths/URLs, transformations, generator]

### Owner
[Responsible party]

### Status
`planned` | `in_progress` | `blocked` | `draft` | `verified` | `superseded`

### Dependencies
[Related artifacts or prerequisites]

### Version
[Version or commit identifier]

### Verification
[Checks performed and evidence]

### Related decisions
[Decision IDs]

### Related artifacts
[Artifact names or paths]
''',
'review.md': '''# Review Record

**Purpose.** Evaluate an artifact or mission against explicit requirements and quality risks.

**When to use.** Use before delivery of important work or after a material change.

## Completed example

### Scope
Review the CCSS template upgrade against the supplied requirements.

### Strengths
The templates now explain purpose, use, structure, examples, and copy-ready fields.

### Weaknesses and defects
The local project lacks repository-level files such as LICENSE and CONTRIBUTING.md; these were not invented.

### Verdict
`PASS WITH CHANGES`: documentation is usable, but repository metadata remains outside this skill package.

## Copy-ready template

### Objective
[What this review must establish]

### Review scope
[Files, versions, requirements, exclusions]

### Strengths
- [Strength]

### Weaknesses
- [Weakness]

### Defects
| ID | Defect | Severity | Evidence | Fix status |
|---|---|---|---|---|
| R-001 | [defect] | [critical/high/medium/low] | [evidence] | [open/fixed/deferred] |

### Risks
[Residual risks]

### Requirements compliance
- [ ] [Requirement]

### Recommendations
[Prioritized changes]

### Final verdict
`PASS` | `PASS WITH CHANGES` | `FAIL`

### Verification evidence
[Checks and results]
''',
'redteam.md': '''# Red-Team Record

**Purpose.** Challenge assumptions, misuse paths, edge cases, and failure behavior before delivery.

**When to use.** Use for important, externally visible, security-sensitive, or difficult-to-reverse work.

## Completed example

### Finding
A user could mistake a placeholder capability for an available one if status and limits were omitted.

### Severity
Medium.

### Impact and likelihood
Misdirected planning; plausible in a new environment.

### Recommendation and remediation
Require status, interface, limits, permission, and confidence in every capability record.

### Verification
Inspect the capability template and mission capability map for all fields.

## Copy-ready template

### Scope
[Mission, artifact, or workflow under attack]

### Questions to ask
- What could be wrong?
- Which assumptions could fail?
- Which edge cases are missing?
- What could an adversary exploit?
- What if a dependency, tool, or permission is unavailable?
- What happens with malformed input or unexpected scale?

### Findings
| ID | Finding | Severity | Impact | Likelihood | Recommendation | Remediation | Verification |
|---|---|---|---|---|---|---|---|
| RT-001 | [finding] | [critical/high/medium/low] | [impact] | [likelihood] | [recommendation] | [fix] | [proof] |

### Residual risks
[Known remaining risks]
''',
'checkpoint.md': '''# Mission Checkpoint

**Purpose.** Make mission state understandable without rereading the conversation.

**When to use.** Use at milestones, before consequential actions, when pausing, or after recovery.

## Completed example

- Timestamp: 2026-08-22T09:45Z
- Mission: CCSS documentation upgrade
- State: `verifying`
- Completed: templates and README drafted
- Pending: link and structure checks
- Blockers: none
- Next action: run validation
- Rollback: restore prior files from version control or backup

## Copy-ready template

### Timestamp
[ISO 8601 timestamp]

### Mission
[Mission name or ID]

### Current state
`proposed` | `ready` | `active` | `paused` | `blocked` | `awaiting_decision` | `verifying` | `completed`

### Completed work
[Done since prior checkpoint]

### Pending work
[Remaining work]

### Blockers
[Blockers or none]

### Decisions
[Decisions made or awaiting approval]

### Artifacts
[Created or changed artifacts and status]

### Next action
[Single next useful action]

### Rollback information
[Backup, commit, inverse operation, or “not available”]
''',
'capability.md': '''# Capability Registry Entry

**Purpose.** Describe what the host can honestly provide before a workflow depends on it.

**When to use.** Use during discovery for every capability that materially affects execution.

## Completed example

### Capability
Web research

### Category and description
Information acquisition; retrieve current public sources when the host supports web access.

### Availability
`available`

### Interface
Host web-search and page-reading interfaces.

### Permissions and limitations
READ; sources may be inaccessible, stale, paywalled, or contradictory.

### Confidence and fallback
High confidence in interface presence; fallback is supplied documents, with current web information marked unavailable.

## Copy-ready template

### Capability name
[Name]

### Category
[research / file / compute / media / communication / external action]

### Description
[What it can do]

### Availability
`available` | `degraded` | `fallback` | `unavailable`

### Interface
[Tool, API, host feature, or user-provided resource]

### Required permissions
`READ` | `WRITE` | `EXECUTE` | `EXTERNAL` | `DESTRUCTIVE`

### Limitations
[What it cannot guarantee]

### Dependencies
[Dependencies]

### Confidence
[low/medium/high, with reason]

### Fallback capability
[Honest substitute or “none”]
''',
}

readme = '''# CCSS 5.0

**Creative Customs Smart Skill — The Master of All**

CCSS is a platform-neutral framework for turning natural-language goals into proportionate, verifiable missions. It helps an AI system or human operator discover capabilities, plan work, preserve decisions and evidence, recover from failure, and deliver artifacts without pretending that unavailable tools or permissions exist.

## Why it exists

Broad requests often fail at the seams: unclear outcomes, hidden assumptions, missing permissions, weak provenance, and no definition of “done.” CCSS makes those seams explicit without requiring one vendor, model, agent runtime, or tool provider.

## How it works

```text
UNDERSTAND → DISCOVER → MODEL → PLAN → EXECUTE → OBSERVE
→ VERIFY → CRITIQUE → IMPROVE → DELIVER
```

The host is an adapter boundary:

```text
HOST → CAPABILITY DISCOVERY → ADAPTER MAP → CCSS CORE → MISSION
```

If a host feature is unavailable, CCSS uses an honest fallback or records `UNAVAILABLE`. It does not simulate execution.

## Quick start

1. Read `SKILL.md` for routing and operating rules.
2. Use `/auto` for ordinary work.
3. Use `/master` when the mission needs explicit planning.
4. Use `/god` for maximum legitimate review and alternatives.
5. Use `/control` when you want checkpoints and approval gates.
6. Copy a relevant file from `templates/` for durable records.
7. Read `examples/` for concrete patterns.

Example:

```text
/master /deep /verify
Research three approaches to migrating our documentation site.
Compare risks and costs, use current sources, and deliver a recommendation.
Ask before any external publication.
```

## Core vocabulary

A **Mission** is bounded work with an outcome and success criteria. A **Capability** is something the host can provide. A **Skill** is reusable procedural knowledge. A **Tool** is an executable interface. An **Agent** is a bounded worker or perspective when supported. A **Workflow** is the dependency-aware path through the work. An **Artifact** is a deliverable. **Evidence** supports a claim. **Verification** checks whether a result meets its criteria. A **Checkpoint** records recoverable state. A **Mode** controls orchestration depth and user control.

## Modes and commands

`/auto` is the default. `/master` makes the mission explicit. `/god` adds deep alternatives, federation, red-team review, and quality control. `/control` emphasizes user checkpoints. Modifiers include `/deep`, `/fast`, `/quality`, `/verify`, `/redteam`, `/parallel`, and `/sequence`. Actions include `/plan`, `/research`, `/design`, `/create`, `/build`, `/analyze`, `/debug`, `/test`, `/review`, `/improve`, `/optimize`, and `/ship`.

## Installation and portability

Copy the `ccss-5-0` directory into the Skills or prompt-resource directory supported by the target runtime. Keep `SKILL.md` and load references and templates only when needed. The exact installation command is host-specific; CCSS does not assume Manus, a particular model, or a particular API.

## Extensions

Add a new Skill when reusable domain knowledge or a repeatable workflow deserves its own package. Add a reference when detail is useful but not always relevant. Add a template when a record has a stable schema. Keep the core concise and avoid duplicating instructions.

## Limitations

CCSS cannot grant access, bypass authentication, verify unavailable sources, guarantee model behavior, or authorize external and destructive actions. It cannot turn an inference into a fact. Host support, permissions, source quality, and human approval remain decisive.

## Contributing

Improve the smallest weak area. Preserve terminology and safety boundaries. Add a realistic example for new behavior, validate internal references, and document limitations. Do not add invented capabilities, fake sources, or unsupported benchmark claims.

## License

No license file was present in the supplied skill package. Add the project’s chosen license before publishing it as an open-source repository.
'''
files['README.md'] = readme

examples = {
'simple-task.md': '# Simple Task\n\n**Request:** Summarize a supplied Markdown file in 200 words.\n\n**Route:** `/auto summarize the supplied file in 200 words`.\n\n**Behavior:** Read the file, summarize only its content, check length, and report any ambiguity. No mission record is needed unless the task expands.\n',
'complex-mission.md': '# Complex Mission\n\n**Request:** Build and validate a documentation migration plan across four repositories.\n\n**Route:** `/master /verify`.\n\n**Mission graph:** inspect repositories and permissions → map dependencies → draft parallel migration options → review risks → select a plan → verify links and rollback steps → deliver report.\n',
'god-mode.md': '# God Mode\n\n**Request:** Stress-test a proposed AI product launch plan.\n\n**Route:** `/god /deep /redteam /verify`.\n\n**Behavior:** Compare alternatives, identify evidence gaps, challenge assumptions, inspect capability limits, model failure paths, and deliver a decision-ready review. The mode increases scrutiny; it does not authorize publication or spending.\n',
'research-mission.md': '# Research Mission\n\n**Request:** Compare three current open-source workflow engines.\n\n**Route:** `/master /research /verify`.\n\n**Required records:** research, evidence, decision, and review. Every current claim gets a source and access date; contradictions and unavailable data remain visible.\n',
'software-project.md': '# Software Project\n\n**Request:** Build a small authenticated dashboard.\n\n**Route:** `/master /build /test /verify`.\n\n**Workflow:** requirements → architecture → capability and permission audit → implementation → automated tests → security review → deployment approval. External publication is a separate authorized step.\n',
'tool-limited-environment.md': '# Tool-Limited Environment\n\n**Situation:** Web research is unavailable.\n\n**Behavior:** Record the capability as `unavailable`, do not claim current web facts, use supplied documents if sufficient, label the result `DEGRADED MODE`, and state what would require live research.\n',
'multi-skill-mission.md': '# Multi-Skill Mission\n\n**Request:** Produce a data-backed article with charts and a polished PDF.\n\n**Route:** `/master /research /analyze /create /verify`.\n\n**Federation:** research gathers sources; data analysis normalizes and checks data; writing produces copy; document generation creates the artifact; review verifies provenance, rendering, and requirements. Each capability has explicit inputs, outputs, dependencies, and fallback behavior.\n',
}
for name, text in examples.items():
    (E / name).write_text(text)
for name, text in files.items():
    (T / name).write_text(text) if name.endswith('.md') and name != 'README.md' else (ROOT / name).write_text(text)
''
