# Capability Registry Entry

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
