# ADR-0001: Use Expo + React Native for the cross-platform mobile app

- **Status:** Accepted
- **Date:** 2026-11-01
- **Supersedes:** None
- **Superseded by:** None

> Illustrative example only. This is not a universal recommendation or a decision made for every CoolFlow user.

## Context

The product is a new mobile application intended for both iOS and Android. The initial team is small, and the product needs ordinary mobile capabilities such as camera, microphone, notifications and location. The first release does not require extensive platform-specific native code.

The project needs a development approach that supports a shared codebase without preventing native extensions if the product later requires them.

## Decision drivers

- Deliver iOS and Android without maintaining two independent application codebases.
- Preserve access to platform capabilities needed by the product.
- Keep local development and automated builds manageable for a small team.
- Avoid locking the project out of native modules if requirements become more demanding.

## Options considered

### Native Swift + Kotlin

- Benefits: direct access to platform APIs and native UI capabilities.
- Costs and risks: two application codebases, duplicated implementation and higher maintenance effort.

### Flutter

- Benefits: shared cross-platform codebase and mature UI framework.
- Costs and risks: a different language and ecosystem from the team's existing TypeScript skills.

### Expo + React Native

- Benefits: shared TypeScript codebase, broad ecosystem and access to native capabilities through Expo modules and native modules.
- Costs and risks: some advanced native integrations may require a development build, native configuration or custom modules; platform-specific testing remains necessary.

## Decision

Use **Expo + React Native with TypeScript** for the mobile application.

Start with Expo's managed workflow where it fits. Use a development build and add native modules when an evidenced product requirement cannot be met by the existing Expo APIs. Do not eject or introduce custom native code pre-emptively.

## Consequences

### Positive

- One primary application codebase serves both mobile platforms.
- Existing TypeScript knowledge and tooling can be reused.
- The project can add native modules when justified by real requirements.

### Negative / trade-offs

- Native integration and build configuration can become more involved as custom modules are introduced.
- iOS and Android behavior still needs to be verified on both platforms.
- The team must understand the boundary between Expo-managed capabilities and native project configuration.

### Follow-up

- Validate camera, microphone, notifications and location on real devices before relying on them.
- Revisit this decision if a core requirement cannot be delivered reliably through Expo and suitable native modules.

## References

- Product requirements: docs/work/<objective>/spec.md
- Expo documentation: https://docs.expo.dev/
- React Native documentation: https://reactnative.dev/
