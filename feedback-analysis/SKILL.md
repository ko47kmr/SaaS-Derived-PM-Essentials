---
name: feedback-analysis
description: Analyze customer feedback (qualitative). Identify critical use cases and pain points. Prioritize based on business impact.
use_when: Understanding customer pain, prioritizing fixes, validating roadmap
---

# Feedback Analysis

Overview
Qualitative analysis of customer feedback. Identify use cases, pain impact, and critical business issues. Prioritize themes (Critical/High/Med reasoning) and recommend roadmap items. Qualitative report (No dashboard), encouraging PM introspection and validation.

## Flow
[Qual Input]
↓
[Theme/Use Case]
↓
[Impact Reasoning (Search)]
↓
[Qual Priority Report]

## Input Focus
**Qualitative Raw**:
- Quotes, support tickets, survey comments, customer interviews.
- **Usage hints (Optional)**: Drop off patterns, failed actions.
- **Sources**: Describe where the feedback is coming from (e.g., "45 tickets, 20 NPS comments").
- **No hard quant volume**: Focus on "Frequent" patterns rather than exact stats.

## Web Search for Similar Cases
Search `"[pain] customer feedback cases"` (e.g., Intercom, Productboard blogs).
- **Goal**: Find benchmarks or similar patterns.
- **Example**: "Setup friction → Wizard, churn -15% impact." Use this for reasoning support.

## Qualitative Framework (Use Case/Pain Impact Focus)
1.  **Input Class**: Group raw quotes and data.
2.  **Theme/Use Case Extract**: Map pains to specific user goals/workflows.
3.  **Impact Examination**: Is it **Business Critical**?
    -   Does it block adoption?
    -   Is it a churn driver?
    -   What is the estimated ARR risk?
4.  **Prioritization**:
    -   **Critical**: Churn driver, blocks core business flow.
    -   **High**: Adoption friction, significant efficiency loss.
    -   **Med**: Nice to have, polish, edge cases.
    -   *Reasoning*: "Pain in core use case → High critical."
5.  **Synthesis**: Create a narrative story/trend.
6.  **Recs**: Action/Validate.

## Output Format
### Feedback Report: [Period]

**Input Overview:**
-   **Sources**: 45 tickets, 20 NPS comments, 5 interviews
-   **Sentiment trend**: Neg up post-update

**Key Themes & Use Case Mapping (Prioritized):**

1.  **Critical: Setup Friction (Core onboarding use case)**
    -   **Use case**: "New user config → Campaign"
    -   **Pain**: "Too many clicks/ jargon"
    -   **Impact examination**: Blocks adoption, estimated 40% drop, $2M ARR segment risk
    -   **Quotes**: "PhD needed"
    -   **Reasoning**: Frequent early funnel, churn driver

2.  **High: Query Perf (Daily analysis use case)**
    -   **Impact**: Time waste $X/hr, retention risk
    -   **Quotes**: [3]

3.  **Med: Docs Gap (Edge lookup)**
    -   **Impact**: Support load low ARR

**Synthesis Narrative:**
"Core onboarding friction dominates (60% feedback), blocking high ARR users. Perf secondary daily pain. Education gap minor. Trend: Post v2.0 spike → Feature bloat suspect."

**Recommendations:**
1.  **Critical**: "Wizard prototype" ticket, Q2 prio1
2.  **Validate**: Interview 10 ARR> $1M complainers
3.  **Roadmap**: Top3 Q2, Monitor NPS post-fix

**PM Introspect Prompt:** "Missed use cases? Strategic pain? Quant validate plan?"

## Best Practices
-   **Use case lens**: Core flows vs Edge cases.
-   **Impact story**: Reason through the business impact (ARR/Churn risk).
-   **Quotes anonymize**: Use real voices but protect identity.
-   **Validate always**: Follow up with interviews.
-   **Quarterly review**: Look for long-term trends.

## Style
"Qualitative insight synthesizer. Use case/pain impact story. Rich reasoning. Push for action/validation."
