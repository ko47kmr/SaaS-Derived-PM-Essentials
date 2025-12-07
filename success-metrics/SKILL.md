---
name: success-metrics
description: Define hierarchical success metrics (North Star, Leading, Counter) and construct compelling data stories for stakeholders.
use_when: Defining success criteria for features, setting OKRs, defending product strategy
---

# Success Metrics

Move beyond "Tracking Numbers" to "Telling Stories." Use this skill to define rigorous metric hierarchies and translate them into narratives that align stakeholders.

## Context Branching (Mandatory)
Before starting, clarify:
1.  **"Scope?"** (Single Feature / Initiative / Company-wide OKR).
2.  **"Product Type?"** (BtoB SaaS / BtoC App / Service).
3.  **"Audience?"** (Engineers need specs; Execs need ROI; Marketing needs growth stories).

## Introspection Prompts
*   **Validity**: "Does this *actually* measure value, or is it a vanity metric?"
*   **Gaming**: "If I paid you $100 to maximize this number, how would you cheat? (Define the Counter-metric)."
*   **Baseline**: "Do we have a baseline today? If not, create a `[Hypothesis - Track 2wks]` task."
*   **Actionability**: "If this number drops 10%, who gets the alert and what do they do?"
*   **Story Logic**: "Why does moving *this* leading indicator predict the North Star?"

## Proactive Search Strategy
1.  **Benchmarks**: `google_search` for "[Industry] [Goal] metric benchmarks" (e.g., "B2B SaaS churn rate benchmark").
2.  **Narratives**: Search for "Airbnb North Star metric story" or "Spotify data storytelling examples" to find narrative structures.

## Frameworks

### 1. The Metric Hierarchy
*   **North Star**: The ultimate measure of value (e.g., "Nights Booked", "Weekly Active Teams").
*   **Leading Indicators**: Input metrics we can move *now* (e.g., "Search to Booking Ratio").
*   **Lagging Indicators**: The result (e.g., "Revenue", "Retention Rate").
*   **Counter-Metrics**: Guardrails (e.g., "Page Latency", "Support Ticket Volume").

### 2. The Metric Narrative (Story)
Construct the logic sentence:
> "We are pursuing **[Goal]** because it drives **[Business Value]**. We will track **[Leading Metric]** because it predicts that goal (historically correlated). We will watch **[Counter Metric]** to ensure we don't accidentally cause **[Risk]**."

## Output Format
*   Use `METRIC_PLAN_TEMPLATE.md`.
*   **Key Sections**: Business Goal, Metric Hierarchy, Stakeholder Story (Copy-paste ready), Instrumentation Spec, Validation Plan.

## Best Practices
*   **Ratio > Absolute**: "50% of users" > "50 users" (Robust against growth).
*   **One Slide Theory**: Can you explain success on a single slide?
*   **Review Cadence**: Weekly check-ins on Leading Indicators; Quarterly reset on North Star.

## Interaction Style
Data-driven storyteller. Combine rigorous hierarchy (Leading/Lagging) with business logic. Always ask: "What is the story? How does this connect to Revenue/ROI?"
