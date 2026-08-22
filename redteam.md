# Red-Team Record

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
