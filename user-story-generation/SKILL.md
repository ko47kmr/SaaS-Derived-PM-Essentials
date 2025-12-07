---
name: user-story-generation
description: Breakdown requirements into small, independent, sprint-ready User Stories. Enforces INVEST criteria and Gherkin syntax for zero ambiguity.
use_when: Sprint planning, backlog grooming, handing off specs to developers
---

# User Story Generation

Create tactical, execute-ready chunks of work ("Stories") from high-level requirements.

> **Note**: Use `customer-journey-mapping` for identifying strategic pains and opportunities. Use `user-story-generation` to convert those insights into specific, buildable tickets for a sprint.

## Input & Branching (Mandatory)
Start by asking:
1.  **"Source of Requirement?"** (Journey Map, PRD, or Raw feedback?)
2.  **"Story Type / Complexity?"**
    *   *Simple*: Single screen/action (1-3 pts).
    *   *Complex*: Multi-step flow/API (5-8 pts).
    *   *Epic*: Too big? (13+ pts -> Split first).

## INVEST Validation Protocol
Run every proposed story through this check:
*   **Independent**: Can it land without waiting for another story?
*   **Negotiable**: Is the specific implementation open for engineering discussion?
*   **Valuable**: Does it have a clear "So that [Benefit]"?
*   **Estimable**: Is it clear enough to size?
*   **Small**: Can it fit in one sprint?
*   **Testable**: Do the ACs cover edge cases?

## Proactive Search Strategy
If the requirement is vague:
1.  **Identify Gaps**: "Missing edge cases for login" or "Security standard for password reset".
2.  **Search**: `google_search` for "Best practice user story for [Feature] AC".
3.  **Label**: Mark as **[Benchmark-inspired]**.

## Sizing Guidance (Fibonacci)
*   **1 pt (Trivial)**: Copy change, Color tweak.
*   **2 pts (Simple)**: New field, Minor logic.
*   **3 pts (Medium)**: New page, Standard CRUD.
*   **5 pts (Complex)**: New integration, complex logic.
*   **8 pts (Large)**: Multi-day work, high risk.
*   **13+ pts (Epic)**: **MUST SPLIT**.

## Output Format
*   Use `USER_STORY_TEMPLATE.md`.
*   **Sprint Organization**: If generating multiple stories, suggest logical grouping:
    > "Sprint Backlog Suggestion: Story A (3pts) + Story B (5pts) = 8pts total. Dependency: A before B."

## Interaction Style
Collaborative tactical partner. Enforce INVEST/Gherkin for zero ambiguity. Challenge "too big/epic" stories with splits. Focus on "What" and "Why"; leave "How" to engineering.
