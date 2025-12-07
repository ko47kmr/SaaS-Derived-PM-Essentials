### Test Suite: [Feature Name] Coverage [e.g. 90%]

**Pre-conditions**
*   User logged in as [Role]
*   Test data [X] exists

**Functional Cases (Happy Path)**
*   **TC-001 [Title]**
    *   **Steps**: 1. [Action] 2. [Action]
    *   **Data**: `user=test`, `input=valid`
    *   **Expected**: [Result]

**Negative / Edge Cases**
*   **TC-002 [Title]**
    *   **Steps**: [e.g. Enter invalid email]
    *   **Expected**: Error message "Invalid format" appears.

**Integration (API/DB)**
*   **TC-003 [Title]**
    *   **Action**: POST /api/[endpoint]
    *   **Expected**: 200 OK, JSON body contains [X]

**Performance**
*   **TC-004 Load Test**
    *   **Scenario**: 1k concurrent users
    *   **Expected**: Response < 200ms

**Security**
*   **TC-005 [Threat]**
    *   **Input**: `<script>alert(1)</script>`
    *   **Expected**: Input sanitized, no alert.

**Accessibility (BtoC/WCAG)**
*   **TC-006 Screen Reader**
    *   **Action**: Focus on [Button]
    *   **Expected**: VoiceOver reads "Submit Button"

**Search Insights**
*   [e.g. "For file upload, test 0 byte files and max size limit" - Source: Ministry of Testing]
