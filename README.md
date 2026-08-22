# CCSS 5.0

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

Copyright 2026 Yatharth Roy

The Thursday AI Company of New Delhi 
