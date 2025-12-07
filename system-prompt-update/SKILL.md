---
name: system-prompt-update
description: Safe iterative system prompt updates w/regression prevention, token control, auto-eval.
---

# System Prompt Update (Final Improved)

**Overview**
Safe updates w/impact analysis, full output, language persistence, diff/eval.

**Flow**
Impact → Strategy Confirm → Gen Full → Diff/Auto-Eval → Lifecycle。

## 1. Impact Analysis (Pre-work)
Input: Current prompt + Request。
1. Diff Check: Request vs existing logic。
2. Side Effect Scan: "Change X breaks Y? (e.g., JSON parser)"
3. Language Check: Detect current language,

 **Maintain**。

## 2. Strategy Confirmation
Output:
```
# Update Strategy
Target: [Section/tag]
Change: [Summary]
Risks: [Potential regressions]
Verification: Diff + few-shot test
```
*Wait user OK*。

## 3. Generate (Full Text)
**ALWAYS full valid prompt, NO `...`**。
Version: vYYYY-MM-DD-HHMM。
Changelog update/create:
```
<!-- CHANGELOG
2025-12-07-1046: JSON constraint add (Current)
-->
```
Token est/count + trim if bloat (Intent preserve)。

## 4. Self-Correction & Explanation
1. Review generated: Unintended changes?
2. Explain changes in **User language** (Japanese ex)。
3. Conflict: "Shorter vs CoT? Priority?"
Test spec? "Run spec/verify pass?"

## 5. Lifecycle Check
```
**Update Complete.**
1. Diff verify (Markdown below)。
2. Regression: Original few-shot test。
3. Downstream docs/apps impact update?
4. Complex? RAG/Tools propose (Langchain functions)。
```

**Diff Example:**
```
Old:
<role>Old role</role>

New:
<role>New role</role>
```

**Best Practices**
- Atomic: 1 section change。
- Language persist。
- Modular XML/JSON。
- CoT/Few-shot。
- Eval loop。

**Interaction Style**
Diligent maintainer。Cautious precise。Intent first。