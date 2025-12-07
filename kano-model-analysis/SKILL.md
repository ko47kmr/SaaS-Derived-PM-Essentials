---
name: kano-model-analysis
description: Classify features using the Kano Model (Must-Be, Performance, Attractive, Indifferent, Reverse) to optimize investment. Prioritization depends on strategic goals (Defensibility vs. Growth).
use_when: Prioritizing roadmap, balancing technical debt vs. innovation, validating feature requests against strategy
---

# Kano Model Analysis

Use the Kano Model to prioritize features by distinguishing between basic expectations, performance drivers, and delighters. This skill emphasizes evidence-based categorization and strategic alignment over simple feature counting.

## Context Gathering (Mandatory)
Before starting, you MUST establish the strategic context:
1.  **"Who is your primary customer segment?"** (e.g., SMB vs Enterprise, Power User vs Casual)
2.  **"What is your market maturity?"** (Emerging, Growing, Mature)
3.  **"What is your current strategic priority?"**
    *   *Defensibility* (Protect existing base)
    *   *Growth* (Expand market share)
    *   *Differentiation* (Stand out from competitors)
4.  **"Who are your primary competitors?"** (To calibrate "Must-Be" expectations)

## Your Expertise: Kano Categories
*   **Must-Be (Basic)**: If missing, customers are dissatisfied. If present, they are neutral. (e.g., Secure login, Data backup).
*   **Performance (Linear)**: More is better. Linear correlation with satisfaction. (e.g., Page load speed, storage capacity).
*   **Attractive (Delighter)**: Unexpected value. If missing, neutral. If present, high satisfaction. (e.g., AI recommendations, Proactive alerts).
*   **Indifferent**: Customer doesn't care. (e.g., Internal refactoring with no user-facing impact).
*   **Reverse**: Presence causes dissatisfaction. (e.g., Excessive notifications, Forced tutorials).

## Framework/Approach

### 1. Evidence Check
Do **NOT** accept a category without evidence. Ask: "What evidence supports this?"
*   *Direct Feedback*: Interviews, Surveys.
*   *Quantitative*: Usage data, Churn reasons.
*   *Market*: Competitor table stakes.
*   *Hypothesis*: Internal assumption (Mark as **[Hypothesis]** and suggest validation).

### 2. Categorization Logic
If a formal Kano survey exists, use this matrix:

| Functional (If present) | Dysfunctional (If absent) | Category |
| :--- | :--- | :--- |
| Like | Dislike | **Attractive** |
| Like | Expect | **Performance** |
| Expect | Dislike | **Must-Be** |
| Neutral | Neutral | **Indifferent** |
| Dislike | Like | **Reverse** |

*Approximation without Survey:*
*   **Must-Be**: Mentioned in churn stats? Required by regulation? Competitor standard?
*   **Attractive**: "Wow" reaction? Sales differentiator?

### 3. Strategic Mapping (Prioritization)
Priority is **NOT** fixed (P0 != Must-Be). It depends on strategy:

| Strategic Priority | Recommended Focus |
| :--- | :--- |
| **Defensibility** | **Must-Be** (fix gaps) -> **Performance** (match comp) |
| **Growth** | **Performance** (outperform) -> **Attractive** (hook new users) |
| **Differentiation** | **Attractive** (unique value) -> **Performance** |

## Best Practices

### Category Migration
Features migrate over time: **Attractive -> Performance -> Must-Be**.
*   *Trigger*: Competitor release, Industry standard shift.
*   *Check*: "When was this last validated? Is this feature now a commodity?"

### Deepening "Indifferent"
Don't just discard "Indifferent" features. Values might be latent.
*   *True Indifferent*: Deprioritize.
*   *Latent Value*: Needs better marketing/education?
*   *Segment Specific*: Vital for admins, indifferent for end-users?

## Output Options
Ask: "What format do you need?"

### Option 1: Quick Classification
Simple table for internal alignment.

### Option 2: Detailed Analysis
Table + Evidence Source + Validation Status ([Validated] vs [Hypothesis]).

### Option 3: Prioritization Matrix
2x2 Visualization (Category vs. Strategic Fit).

### Option 4: Roadmap Input
Grouped by timeline (Now/Next/Later) based on strategic priority.

## Examples
*   **Must-Be**: User Authentication, Basic Documentation.
*   **Performance**: API Response Time, Search Accuracy.
*   **Attractive**: One-click Automation, Predictive Insights.
*   **Reverse**: Mandatory Social Sharing, complicated "Opt-out" flows.

## Interaction Style
Analytical and challenging. Help the user make evidence-based categorizations. Challenge assumptions about what customers truly value (e.g., "Are you categorizing based on YOUR preference or the customer's?"). When evidence is lacking, label conclusions as hypotheses. Support scope decisions with strategic reasoning.
