# Editorial harness

Cereja uses a four-part harness around editorial generation and channel rendering.

| | Feedforward | Feedback |
|---|---|---|
| **Descriptive** | [Guides](guides.md) | [Sensors](sensors.md) |
| **Normative** | [Guards](guards.md) | [Checks](checks.md) |

This separates **helpful context**, **pre-action constraints**, **observability** and **acceptance criteria**.

## Editorial flow

```text
NÚCLEO + EDITORIAL PACKET + FLAME
              ↓
           GUIDES
              +
           GUARDS
              ↓
    AGENT / SKILL / RENDERER
              ↓
           SENSORS
              ↓
           CHECKS
              ↓
        KELL APPROVAL
              ↓
          PUBLISH
              ↓
         LEARN-BACK
```

Human approval remains mandatory for publication.

## Why the distinction matters

A voice guide is not a voice check.

A rights note is not a rights guard unless it can stop or escalate invalid use.

A trace showing that a renderer introduced a new claim is a Sensor.

A rule that blocks the output when an unapproved new claim is detected is a Check/Guard depending on when it is enforced.

## Maturity labels

Use:
- **documented**
- **implemented**
- **automated**
- **validated**

Do not describe a proposed reviewer role or Markdown rule as operational automation.
