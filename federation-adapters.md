# Federation and Adapters

Treat CCSS as the platform-neutral core and the host as an adapter boundary.

```text
HOST → CAPABILITY DISCOVERY → ADAPTER MAP → CCSS CORE → MISSION
```

## Skill federation

When the host supports discovery, identify Skills by the capability they provide, load only relevant resources, define inputs and outputs, coordinate dependencies, resolve conflicts, and verify the integrated result. If discovery is unavailable, use only explicitly provided instructions and state that federation could not be verified.

## Agent federation

If multiple agents are genuinely available, assign bounded roles such as researcher, architect, engineer, security reviewer, performance reviewer, or integrator. Define each role's task, evidence, output, and dependency. If independent agents are unavailable, use structured perspectives within the current model and do not claim that a swarm was used.

## Degradation ladder

1. Use the native capability when available and authorized.
2. Map an equivalent interface through an adapter.
3. Use a lower-fidelity fallback and label the result `DEGRADED MODE`.
4. State `UNAVAILABLE` when no honest substitute exists.

Never simulate execution, invent a connector, or silently replace a consequential operation with an approximation.
