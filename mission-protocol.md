# CCSS Mission Protocol

Represent substantial work as a mission. Use a graph when dependencies are non-linear; use a short sequence for routine work.

```yaml
mission:
  objective: ""
  desired_outcome: ""
  constraints: []
  success_criteria: []
  assumptions: []
  capabilities: []
  skills: []
  tools: []
  nodes: []
  dependencies: []
  milestones: []
  state: proposed
  risks: []
  blockers: []
  artifacts: []
  decisions: []
  verification: []
```

## Capability record

For each required capability, record `name`, `status` (`available`, `degraded`, `fallback`, or `unavailable`), `interface`, `limitations`, `permissions`, and `confidence`. Map host-native tools, plugins, Skills, APIs, or agents to the conceptual capability without hard-coding a vendor.

## Workflow generation

Derive nodes from objective, complexity, risk, constraints, dependencies, and available capabilities. Typical primitives are understand, inspect, research, define, design, implement, test, review, verify, package, and deliver. Do not force every primitive into every mission. Parallelize only independent nodes with useful host support. Add checkpoints before consequential or difficult-to-reverse actions.

## State transitions

Use `proposed → ready → active → paused | blocked | awaiting_decision → verifying → completed`. On failure, record the failed node, observed evidence, diagnosis, selected recovery path, and changed plan. Never mark a mission completed solely because a command was issued.

## Completion

A mission is complete only when success criteria are checked and material artifacts are available or the user has accepted an explicit limitation. Deliver a concise state summary, key decisions, assumptions, verification performed, risks, and next action.
