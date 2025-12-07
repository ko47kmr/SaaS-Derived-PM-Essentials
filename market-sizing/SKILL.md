---
name: market-sizing
description: Calculate TAM/SAM/SOM using Top-Down, Bottom-Up, and Value-Theory approaches. Emphasizes research planning, rigorous assumption testing, and sensitivity analysis.
use_when: Go/No-go decisions, Investment planning, Resource allocation, Pitch decks
---

# Market Sizing

Estimate the potential revenue opportunity with decision-useful precision. This skill avoids false precision by focusing on rigorous assumptions and sensitivity analysis.

## Purpose Clarification (Mandatory)
Before starting, you MUST clarify the goal:
1.  **"What decision will this inform?"** (Go/No-go, Investment level, Resource allocation, External pitch)
2.  **"What level of precision do you need?"** (Order of magnitude, Directional ±50%, Precise ±20%)
3.  **"What is your time horizon?"** (1 year, 3 years, 5+ years)

## Context Gathering (Mandatory)
Replcing hard-coded assumptions with user context:
*   **Ideal Customer Profile (ICP)**: Size, Industry, Geography.
*   **Pricing Model**: Subscription, Usage, One-time.
*   **Current Position**: Leader, Challenger, New Entrant.
*   **Competitors**: Who are you stealing share from?

## Methodology Selection

| Approach | Best For | Limitations |
| :--- | :--- | :--- |
| **Top-Down** | Mature markets, Initial screening. | Market definition ambiguity. Risk of overestimation. |
| **Bottom-Up** | Validating Top-Down, Specific segments. | Labor intensive. Misses unknown segments. |
| **Value-Theory** | New markets, Disruptive products. | Subjective. Uncertain WTP (Willingness to Pay). |

*Guidance*: "Which approach matches your data availability? Can we triangulate using two methods?"

## Research Planning Protocol
**Do NOT calculate before planning.**
1.  **Identify Data Points**: Total Revenue, Growth Rate, # Customers, ACV, Competitor Share.
2.  **Map Sources**:
    *   *Tier 1*: Analyst Reports (Gartner/IDC).
    *   *Tier 2*: Associations/Gov Stats.
    *   *Tier 3*: Competitor 10-Ks/Press Releases.
    *   *Tier 4*: Proxies (Adjacent markets).
3.  **Search Plan**: specific queries and trusted sources.
4.  **Documentation**: Record Source, Date, and Confidence (High/Med/Low) for every point.

## Assumption Challenge Framework
Challenge these dangerous assumptions:
*   **Market Size**: "Source? Year? Does it include adjacent categories?"
*   **Growth Rate**: "Historical or Projected? Pre/Post disruption?"
*   **SAM %**: "What % truly fits the product? Exclusion criteria?"
*   **Win Rate**: "Based on history or hope? Against which competitor?"
*   **ACV**: "Aspirational or Validated WTP?"

## SOM Reality Check
1.  **Capacity**: "SOM / ACV = # Deals. Can Sales close this many?"
2.  **History**: "Is this growth inconsistent with historical trajectory?"
3.  **Pipeline**: "What % of SOM is in the pipeline now?"
4.  **Name Test**: "Can you name 10% of these target customers?"

## Sensitivity Analysis
Single-point estimates are dangerous. Create scenarios:
*   **Variables**: Top 3 uncertain assumptions (e.g., Win Rate, ACV).
*   **Scenarios**: Pessimistic / Base / Optimistic.
*   **Output**: Impact range (e.g., SOM $5M - $12M).

## Output Options
Ask: "What format defines the audience?"
*   **Executive Summary**: 1-pager, Key numbers, Confidence. (For Investors)
*   **Detailed Analysis**: Methodology, Triangulation, Logic. (For Strategy)
*   **Assumptions Log**: Audit trail of every number. (For Validation)
*   **Sensitivity Table**: Risk assessment. (For Risk Mgmt)

## Interaction Style
Analytical and rigorously skeptical. Challenge every assumption with "What is the source?" and "What would change this?". Never accept round numbers or industry benchmarks without scrutiny. When the user lacks data, help identify proxy approaches while clearly labeling uncertainty. The goal is decision-useful estimates, not false precision.
