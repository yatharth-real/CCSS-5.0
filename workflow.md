# Workflow Record

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
