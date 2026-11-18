# Development Flow

Use this reference when planning or reconsidering product direction. Scale the work to the decision, and skip, combine, or revisit stages as needed. Several objectives can be at different stages at the same time.

| Stage | Purpose |
| --- | --- |
| 1. Idea → Brainstorm | Clarify the problem, users, and value. Review competing products and current workarounds, then identify an opportunity and product hypothesis. Use proportionate research where evidence is missing. |
| 2. Lightweight strategic DDD | Establish a provisional domain language, boundaries, and key rules. Develop tactical domain design in the Spec when needed. |
| 3. Concept Prototype → Validation | Test the riskiest assumptions with a time-boxed prototype, spike, or other proportionate method before committing to MVP scope. |
| 4. Roadmap | Define product-level MVP or current-version scope, non-goals, and later direction. |
| 5. UI Prototype | Explore key flows, visual direction, screens, and states. Validate with users when useful. |
| 6. Design Spec Loop | Write a unified Spec covering requirements, acceptance criteria, solution, optional tactical domain design, implementation, and verification. |
| 7. Implementation Loop | Implement and verify the agreed behavior. Record evidence and unresolved risks. |
| 8. Human Acceptance → Documentation Sync → Release | Obtain human acceptance, sync accepted facts, and obtain separate authorization for any applicable release before executing and verifying it. |

## Three Adaptive Loops

- **Design Spec Loop (Step 6).** Draft → Review → Refine. Resolve important design issues before substantial implementation.
- **Implementation Loop (Step 7).** Build → Test → Review → Fix. Check code and Spec conformance. Return to the Design Spec Loop when the design needs revision.
- **Evolution Loop (cross-stage).** Capture new input → Reassess affected decisions → Adapt. Start at any stage and return to any relevant stage. New evidence can change product assumptions without a prior release or Roadmap update. Keep routine design and code corrections in their local loops, and ask the human to decide major product changes.

Documentation Sync is a post-acceptance step. See the [local documentation standard](documentation.md) for how to record and archive work.
