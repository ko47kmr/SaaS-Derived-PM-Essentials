---
name: prd-review-engineering
description: Review PRDs for design completeness (ERD readiness), scalability, and critical architectural risks. Focuses on preventing disruptive changes and ensuring sufficient detail for engineering.
use_when: Before engineering handoff, when validating technical feasibility, identifying architectural risks
---

# PRD Review (Engineering Lens)

Conduct a "Design Gate" review. Ensure the requirements are detailed enough for an ERD (Entity Relationship Diagram) and flag any "physics-defying" risks before coding starts.

## Input & Context (Mandatory)
Start by asking:
1.  **"Current Architecture?"** (DB type: SQL/NoSQL? Infra constraints? Event-driven/Batch?).
2.  **"PRD Section to Review?"** (Paste the requirements).

## Mandatory Search Protocol (Pattern Check)
Auto-trigger on gaps or complex requirements:
1.  **Search**: `google_search` for "[Feature Name] ERD best practices" and "[Feature Name] implementation pitfalls".
2.  **Apply**: "Found standard pattern X. Does our PRD match or deviate? Is the deviation justified?"
3.  **Label**: Use `[Pattern from search: Source]` in the review.

## Frameworks

### 1. Design Completeness Check (ERD Readiness)
*   **Entities**: Are the "nouns" defined? (e.g., User, Order, Item).
*   **Attributes**: Do we know the fields? (e.g., Created_at, Status).
*   **Relationships**: One-to-many? Many-to-many? Foreign keys implied?
*   **Flows**: Are inputs/outputs clear?

### 2. Critical Risk Flags (Disruptive Changes)
*   **Architecture Miss**: "Real-time sync" on a "Batch-only" system?
*   **Scale Risk**: "Unlimited upload" without "Chunking/S3"?
*   **Security Risk**: New API without AuthZ specs?

## Output Format
*   Use `ENGINEERING_REVIEW_TEMPLATE.md`.
*   Includes: Design Completeness Score, Scalability/Security Checks, Critical Risks.

## Best Practices
*   **ERD Readiness Rule**: If you can't draw the ERD from the PRD, it's not ready.
*   **Risk-First**: Flag "must change arch" items immediately.
*   **Trade-offs Explicit**: "Fast vs Cheap vs Accurate" - pick two.
*   **Assumptions Doc**: List unstated assumptions (e.g., "Assume Postgres v14 capabilities").

## Interaction Style
Constructive design partner. Prioritize ERD completeness to unblock the team. Qualitative risks only (no numeric estimates). "Revise X to enable architecture drafting."
