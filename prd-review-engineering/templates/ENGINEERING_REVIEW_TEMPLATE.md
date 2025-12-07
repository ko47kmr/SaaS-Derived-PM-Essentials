### Engineering Review: [PRD Feature Name]

**Overall Status**: [Approved / Revise Required (Design gaps) / Blocked (Risk)]
**Complexity**: [Low / Medium / High (Cross-layer impact)]

**1. Design Completeness (ERD Readiness)**
*   **Score**: [Low/Med/High]
*   **Gaps**:
    *   [e.g., Missing Foreign Key spec for 'Order' -> 'User']
    *   [e.g., Data flow for 'Error State' undefined]
*   **Rec**: Add sections "Data Model" and "Relationships" to PRD.

**2. Scalability Check**
*   **Assumptions**: [e.g., Peak load 1k req/sec? If undefined, flag.]
*   **Risks**: [e.g., N+1 query risk on 'List View']
*   **Rec**: Add "Load Profile" or "Pagination Spec".

**3. Security Check**
*   **Vectors**: [e.g., New public API endpoint?]
*   **PII**: [e.g., Is 'Email' encrypted at rest?]
*   **Rec**: Add "Access Control Matrix".

**4. Critical Risks (Disruptive Changes)**
*   **[Risk Title]**: "Requirement X violates current Architecture Y."
    *   *Impact*: Major refactor required.
    *   *Rec*: Change requirement to [Z] or schedule Spike ticket.

**Search Insights**
*   **Pattern**: [e.g., 'Chunked upload for >10GB files' - AWS Docs]

**Recommendations Summary**
*   **PRD Revise**: [List top 3 edits needed]
*   **Create Spike**: [If technical feasibility is unknown]
*   **Approved**: [If no major blocks]
