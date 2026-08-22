# Decision Record

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
