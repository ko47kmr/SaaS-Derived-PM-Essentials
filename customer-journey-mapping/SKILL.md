---
name: customer-journey-mapping
description: Map end-to-end customer journeys identifying touchpoints, pain points, and opportunities. Focuses on evidence-based validation and cross-functional handoffs.
use_when: Improving onboarding, reducing churn, optimizing user experience, designing new features
---

# Customer Journey Mapping

Visualizing the user's end-to-end experience to identify friction and opportunities. This skill emphasizes evidence over assumption and connects silos (Sales/Product/CS).

## Purpose & Scope Clarification (Mandatory)
Before starting, clarify:
1.  **"Which journey?"** (Full lifecycle, Onboarding, Purchase, Support, Renewal)
2.  **"Who is the user?"** (Prospect, Buyer, Admin, Power User, Churned User)
3.  **"BtoB or BtoC?"**
4.  **"What is the focus?"** (Pain identification, Opportunity prioritization, Handoff optimization)

## Context Branching

### Path A: BtoB (Business)
*   **Lifecycle**: Awareness -> Evaluation -> Purchase -> Onboarding -> Adoption -> Renewal.
*   **Critical Friction**: Handoffs between teams (Sales -> CS, CS -> Support).
*   **Multi-Persona**: Different people involved at each stage.

### Path B: BtoC (Consumer)
*   **Lifecycle**: Awareness -> Purchase -> Usage -> Retention.
*   **Critical Friction**: Drop-off points in the funnel/app.
*   **Channel Focus**: Mobile app, Web, Email, Push.

## Research Validation Protocol
**Do NOT map based on guesses.**
1.  **Gap Detection**: "Do we have data for this drop-off?"
2.  **Web Search**: Use `google_search` for "SaaS onboarding benchmarks", "G2 reviews for [Competitor] onboarding pain".
3.  **Labeling**:
    *   **[User-Data]**: Analytics, Logs, Tickets.
    *   **[Research-Supplemented]**: Benchmarks, Competitor Reviews.
    *   **[Hypothesis]**: Assumption (Needs validation).

## Frameworks

### 1. The Core Map
| Stage | Actions | Thoughts | Touchpoints | Pain **[Source]** | Opp **[Priority]** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **User Defined** | ... | ... | ... | ... | ... |

### 2. Critical Prompts
*   **Pain**: "Do you have quantitative evidence for this pain (e.g., support ticket volume)?"
*   **Touchpoints**: "Who owns this touchpoint? Is the messaging consistent with the previous step?"
*   **Opportunities**: "What is the Impact vs Feasibility of fixing this?"
*   **Validation**: "What would disprove this hypothesis?"

### 3. Handoff Map (BtoB)
Focus on the "Seams" between teams:
*   **Sales -> CS**: Does CS know what was promised?
*   **CS -> Product**: Does Product know the root cause of churn?

## Output Formats
Ask: "What format defines the audience?"
*   **Table**: Quick analysis (Use `JOURNEY_MAP_TEMPLATE`).
*   **Timeline**: Visual flow for presentations.
*   **Service Blueprint**: Front-stage vs Back-stage (for Ops/Eng).
*   **Opportunity Matrix**: Prioritized list of fixes (for Roadmap).

## Interaction Style
Holistic, user-centric, evidence-based. Challenge unverified pains with "Source?". Proactively research benchmarks. Prioritize high-impact opportunities. Connect silos across teams.
