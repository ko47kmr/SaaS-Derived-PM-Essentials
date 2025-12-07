### Test Plan Draft: [Release Name/Version] (PM Ready for Eng/QA)

**Objective**
*   Validate [Scope] with zero regression on [Critical Path].

**Risk-Based Scope Matrix**
| Feature / Component | Risk Level | Priority | Coverage Strategy |
| :--- | :--- | :--- | :--- |
| **[e.g. Payment v2]** | [High] | [P0] | [100% Functional + Security Scan] |
| **[e.g. UI Polish]** | [Low] | [P2] | [Visual check / Ad-hoc] |
| **[e.g. Legacy API]** | [Med] | [P1] | [Regression Suite 20% Critical Path] |

**In Scope**
*   **Functional**: [List key new features]
*   **Regression**: [List critical existing flows to protect]
*   **Devices (BtoC)**: [e.g. iPhone 14+, Pixel 7+, Chrome/Safari]

**Out of Scope**
*   [e.g. Deprecated features, IE11 support]

**Approach & Strategy**
*   **Types**: [Functional, Performance, Security, Accessibility]
*   **Tools**: [Suggest team standard, e.g. Cypress for E2E, k6 for Load]
*   **Environments**: [Staging, Production Canary]

**Resources & Schedule**
*   **Owners**: [QA Name], [Dev Name] for Unit Tests
*   **Timeline**: Start [Date] -> Code Freeze [Date] -> Sign-off [Date]

**Exit Criteria (Quality Gates)**
*   [ ] 0 P0 (Blocker) bugs.
*   [ ] < 3 P1 bugs (with workaround).
*   [ ] 95% Automated Suite Pass Rate.
*   [ ] Performance: Latency < [200ms] at [1k] req/sec.

**Search Insights**
*   [e.g. "Standard payment migration testing requires parallel run for 24h" - Source: Stripe Docs]
