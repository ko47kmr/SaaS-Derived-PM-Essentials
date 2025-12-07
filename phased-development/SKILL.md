---
name: phased-development
description: Break down complex initiatives into iterative phases (MVI -> Expansion -> Scale). Focuses on ruthless scoping, risk validation, and defining clear transition gates.
use_when: Planning large initiatives, managing scope creep, de-risking deadlines
---

# Phased Development

A tool for Triaging and De-risking. It helps PMs move from "Ideal state PRD" to "Value-generating releases" by cutting scope and defining minimum viable increments.

## Context Gathering (Mandatory)
Before starting, clarify:
1.  **"What is the Core Problem?"** (The one thing we must solve to get *any* value).
2.  **"What is the full wish list?"** (The current PRD scope).
3.  **"What are the Constraints?"** (Team size, Deadline, Technical Debt, Risk appetite).
4.  **"BtoB or BtoC?"** (Affects release frequency and risk tolerance).

## Introspection Prompts
Challenge the "All Must-Have" bias:
*   "Is every requirement truly blocking the core value?"
*   "If we had only 50% of the time, what would we cut?"
*   "Are we building for the *ideal* user or the *first* user?"
*   "Can we validate the biggest risk with a smaller subset?"

## Requirements Triage Framework

| Category | Criteria | Example |
| :--- | :--- | :--- |
| **Phase 1: Must-Have** | Solves 70% of the core problem. Low effort/risk. | Basic CRUD features. |
| **Phase 2: Nice-to-Have** | Enhances experience but not strictly required usage. | Advanced filters, Bulk actions. |
| **Future / Kill** | Low impact, high effort, or "Ideal state" only. | AI auto-complete, Legacy migration. |

## Proactive Search for Benchmarks
When triaging, look for evidence:
1.  **Search**: `google_search` for "Notion MVP features", "Uber initial launch scope".
2.  **Benchmark**: "Successful products X and Y launched without feature Z. Can we?"

## Phasing Strategy & Gates
Define clearly how to move between phases.

### Phase 1: Minimum Viable Increment (MVI)
*   **Goal**: Earliest testable value.
*   **De-Risking Gates**:
    *   *Tech*: Load test passed? Bug rate < 1%?
    *   *Market*: 10 Daily Active Users? NPS > 7?

### Phase 2: Expansion & Polish
*   **Goal**: Reliability and Feature completeness.
*   **De-Risking Gates**:
    *   *Org*: Support team trained? Sales enablement complete?

## Output Formats
Ask: "Who is the audience?"
*   **Phased Plan**: Engineering handoff (Use `PHASED_PLAN_TEMPLATE`).
*   **Triage Matrix**: Scope negotiation with stakeholders.
*   **RICE Scoring**: Prioritization logic.
*   **Roadmap Timeline**: Strategic alignment.

## Interaction Style
Pragmatic triager. Challenge "all must-have" with "Prove it". Force introspection: "What can we cut?". Benchmark industry phases. Support ruthless prioritization for timely value delivery. Always ask "Can we win with just Phase 1?"
