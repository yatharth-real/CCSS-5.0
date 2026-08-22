# CCSS Command Protocol

Parse commands as a composable configuration rather than a positional macro. Accept tokens in any order and normalize them into a canonical record.

```yaml
mode: auto
modifiers: []
action: null
target: null
options: {}
remainder: ""
```

## Token classes

`MODE` includes `auto`, `master`, `god`, and `control`. `MODIFIER` includes `deep`, `fast`, `swarm`, `preserve`, `quality`, `verify`, `redteam`, `parallel`, and `sequence`. `ACTION` includes planning, research, ideation, design, creation, build, code, analysis, debugging, testing, review, improvement, optimization, and shipping. `TARGET` is the explicit object or natural-language remainder. `OPTION` changes scope, output, timing, or authorization but never overrides safety or host permissions.

## Resolution

Apply defaults only after parsing. If multiple modes appear, retain the most explicit mode and report the conflict briefly; never let a mode bypass authorization. If incompatible modifiers appear, prefer the safer interpretation and record the choice. Treat unknown slash tokens as user text unless the host documents them. Preserve the user's target verbatim before interpreting it.

## Examples

`/god /deep /research topic` and `/research /deep /god topic` normalize to the same configuration: mode `god`, modifier `deep`, action `research`, target `topic`.

`/control /approve deploy` means prepare or continue the deployment only within the host's authorization model; it does not grant permission that the host or user has not provided.

Natural language without slash commands is valid. Infer intent, then use the smallest adequate mode and workflow.
