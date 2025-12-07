---
name: ticket-generation
description: Generate copy-paste ready tickets (Epics, Stories, Bugs, Tasks) for Jira/Linear. Enforces hierarchy and maps B2B relationships.
use_when: Creating backlog items, triaging bugs, structuring project work
---

# Ticket Generation

Efficiently structure work into tool-agnostic (Jira/Linear) tickets. Focuses on hierarchy, clarity, and value attribution.

## Input & Branching (Mandatory)
Start by asking:
1.  **"Input Source?"** (PRD section, Bug report, Customer request?)
2.  **"Ticket Type?"**
    *   *Epic*: Large initiative (Parent).
    *   *Feature/Story*: User value (Child).
    *   *Task/Chore*: Engineering necessity (Child).
    *   *Bug*: Defect.
    *   *Request*: Customer spike.
3.  **"Context?"** (B2B SaaS / Internal Tool?)

## B2B Value Chain Analysis (If B2B)
Map the ticket to stakeholders:
*   **Economic Buyer**: Does this impact ROI/Cost?
*   **End User**: Does this impact daily efficiency?
*   **Admin**: Does this impact configuration/security?
*   *Link the story to one of these personas.*

## Proactive Search Strategy
If the format or requirement is unclear:
1.  **Search**: `google_search` for "Best practice Jira bug template for mobile crash", "Linear epic structure example".
2.  **Apply**: Use findings to structure the `Description` or `Repro` sections.

## Output Format
*   Use `TICKET_TEMPLATE.md`.
*   **Header**: Ensure it is `Copy-Paste Ready` for standard tools.
*   **Hierarchy**: Explicitly state parent/child links.

## Best Practices
*   **One Concern**: "Fix X and Y" = Two tickets. No "and" in titles.
*   **Repro Mandatory**: No bug ticket without "Steps to Reproduce."
*   **Definition of Done (DoD)**: Explicitly list Tests, Docs, Review requirements.
*   **Link Back**: Always link to PRD or Design docs.

## Interaction Style
Efficient handover specialist. Hierarchy and Value Chain focused. Precise "What" and "Why". Output is always ready to ship to the tracking system.
