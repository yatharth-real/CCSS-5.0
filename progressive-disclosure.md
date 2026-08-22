# Progressive Disclosure

Load only the detail needed for the current mission.

## Level 1: routing

Read `SKILL.md` to identify the mode, action, constraints, and required capability classes.

## Level 2: protocol

Load one or more references when the mission requires them: command parsing, mission state, evidence and security, or federation and adapters.

## Level 3: records and examples

Copy a relevant file from `templates/` when the mission needs a durable record. Read a matching file from `examples/` when the user needs a concrete pattern or when the workflow is unfamiliar.

Do not load every reference by default. Do not duplicate reference content in `SKILL.md`. If a needed capability or host feature is unavailable, say so and use an honest fallback or mark it `UNAVAILABLE`.
