---
name: prd-competitive-assessment
description: Evaluate PRD features against competitors use Parity Matrices and Moat Analysis. Provides quantitative win probabilities and GTM recommendations.
use_when: Validating a new feature PRD, assessing market position, preparing sales battlecards
---

# PRD Competitive Assessment

Ensure your feature beats the competition, not just matches it. Use this skill to fact-check your PRD against real-world competitor capabilities.

## Input & Verification (Mandatory)
Start by asking:
1.  **"PRD Overview?"** (Summarize key features).
2.  **"Competitors?"** (List 3-5, e.g., "Competitor X, Y").
3.  **"Sources?"** (Any internal battlecards? Or rely on G2/Web?)

## Mandatory Search Protocol (Fact-Checking)
Before assessing, verify the claims:
1.  **Search**: `google_search` for "[Competitor X] [Feature Name] docs" or "[Competitor Y] pricing page".
2.  **Verify**: "Found that Competitor X has had this since 2022. Is our version significantly different?"
3.  **Label**: Use `[Verified via search]` for confirmed facts.

## Frameworks

### 1. Parity Matrix
Create a table comparing:
*   **Feature / Capability**: The granular requirement.
*   **Competitor X**: Do they have it? (Yes/No/Partial).
*   **Ours**: What is our spec?
*   **Gap/Edge**: Are we Ahead or Behind?

### 2. Moat Analysis (Quantitative)
Does this feature create a moat?
*   **Cost**: Is it cheaper for the customer?
*   **Time**: Is it 2x faster to implement?
*   **Outcome**: Does it produce better results (e.g., higher match rate)?

### 3. Verdict & Win Probability
*   **Low (<30%)**: We are playing catch-up.
*   **Med (50%)**: We are at parity.
*   **High (>70%)**: We have a clear differentiator (Moat).

## Output Format
*   Use `COMPETITIVE_ASSESSMENT_TEMPLATE.md`.
*   Includes: Parity Matrix, Moat Analysis, Win Probability, GTM Recs.

## Best Practices
*   **Honest Gaps**: If we are behind, admit it. Marketing needs to know so they can position around it.
*   **Quarterly Refresh**: Competitors move fast. This assessment expires in 3 months.
*   **The "Why Switch?" Test**: If a user has Competitor X, is this feature enough to make them switch?

## Interaction Style
Critical fact-checker. "I checked the docs, and Competitor Y actually does this. How are we different?" Focus on evidence-based moats.
