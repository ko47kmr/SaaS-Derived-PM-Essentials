---
name: prd-generation
description: Generate comprehensive, triaged Product Requirements Documents (PRDs) and User Stories. Adapts to scale (Simple/Light/Full) and context (BtoB/BtoC).
use_when: Writing specs for new features, defining user stories, aligning engineering teams
---

# PRD Generation

Create clear, triaged, and evidence-based specifications. This skill adapts to the initiative's scale, preventing "over-speccing" for small tasks and "under-speccing" for complex ones.

## Context Branching (Mandatory)
Before starting, ask:
1.  **"What is the Scale?"**
    *   *Simple*: Single User Story.
    *   *Medium*: Light PRD (Problem + Solutions).
    *   *Large*: Full PRD (Risks, Tech specs, Dependencies).
2.  **"New or Update?"**
3.  **"Category?"** (BtoB SaaS / BtoC App / API).
4.  **"Who is the Team?"** (Eng-heavy? Design-heavy?).

## Introspection & Triage Prompts
*   **Triage**: "Is every requirement truly a P0? What can we cut to Phase 2?"
*   **Metrics**: "How will we measure success? Do we have a baseline?"
*   **Corner Cases**: "What happens in error states? Offline mode? Empty states?"
*   **Out of Scope**: "What are we explicitly NOT doing?"

## Proactive Search Strategy
If requirements are vague or benchmarks are missing:
1.  **Identify Gaps**: "Missing error handling patterns" or "standard metrics for this feature".
2.  **Search**: `google_search` for "Best practice user story for password reset", "Intercom PRD template examples".
3.  **Present**: "Industry standard suggests including X. Should we add it?"

## Frameworks & Templates

### 1. Simple (User Story)
For atomic tasks.
*   **Template**: `USER_STORY_TEMPLATE.md`
*   **Focus**: Persona, Action, Benefit, Acceptance Criteria (AC).

### 2. Medium (Light PRD)
For features or enhancements.
*   **Template**: `LIGHT_PRD_TEMPLATE.md`
*   **Focus**: Problem, Goals, Scope, User Stories, High-level AC.

### 3. Large (Full PRD)
For new products or major modules.
*   **Template**: `FULL_PRD_TEMPLATE.md`
*   **Focus**: Full functional/non-functional specs, Risks, Tech Debt, Dependencies, GTM.

## Interaction Style
Structured and adaptive. Adjust detail level to the Scale. Leave zero ambiguity but encourage introspection ("Do we really need this?"). Challenge assumptions with "How will we measure this?".
