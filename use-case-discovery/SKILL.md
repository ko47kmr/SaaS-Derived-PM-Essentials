---
name: use-case-discovery
description: Discover and validate high-value use cases using a dual-mode approach (Exploration vs. Development). Includes frameworks for market research, specificity ladders, and value prioritization.
use_when: Defining product vision, exploring new markets, validating feature requests, prioritization
---

# Use Case Discovery

This skill supports two distinct modes: **Exploration** (understanding market patterns) and **Development** (defining specific scenarios).

## Intent Clarification (Mandatory)
Before proceeding, you MUST clarify the user's intent:

"What is your goal for this session?"
*   **(A) Explore**: Understand industry adoption patterns and representative use cases for a product category.
*   **(B) Develop**: Define a specific use case for your product with detailed user scenarios.

> If (A): Proceed to **Exploration Mode**.
> If (B): Proceed to **Development Mode**.

---

## Mode A: Exploration (Category Overview)

### 1. Define Product Category
Ask: "What product category are you exploring?" (e.g., CRM, Data Platform, Project Management).

### 2. Research Planning Protocol
**Do not search blindly.** establish a plan first:
1.  **Identify Gaps**: "What do you already know? What specific questions need answers?"
2.  **Map Landscape**: "Who are the major players? Who are adjacent competitors?"
3.  **Identify Sources**: Analyst reports, G2/Capterra, Competitor case studies, Job postings.
4.  **Create Plan**: Define search queries and trusted sources.

### 3. Synthesize Patterns
After research, identify:
*   **High Adoption Industries**: Where is this category essential?
*   **Representative Use Cases**: Common patterns (3-5 per industry).
*   **Buyer Personas**: Who holds the budget?

---

## Mode B: Development (Use Case Definition)

### 1. Context Gathering
Establish the sandbox:
*   **Category**: Product domain.
*   **Industry/Segment**: Vertical (e.g., Retail) and Size (e.g., Enterprise).

### 2. Persona Specification
*   **Role**: Title and Function (e.g., Marketing Ops Manager).
*   **Tools**: What do they live in daily?

### 3. Specificity Ladder
Guide the user from vague concepts to actionable specs. Ask: "What level are we at?"

| Level | Description | Example |
|:---|:---|:---|
| **L1: Category** | General need | "Improve retention" |
| **L2: Domain** | Industry specific | "Reduce churn in mid-market" |
| **L3: Persona** | Role specific | "CSM identifies at-risk accounts" |
| **L4: Scenario** | Situation specific | "When usage drops >30%, CSM needs alert" |
| **L5: Workflow** | Step-by-step | "Alert -> Dashboard -> Email -> CRM Log" |

### 4. Scenario Development (The "Job")
*   **Trigger**: What initiates this?
*   **Context**: Constraints/Conditions.
*   **Current Workaround**: How do they do it now? (Competitors? Excel? Nothing?)
*   **Desired Outcome**: Success criteria.
*   **Failure Mode**: Consequence of not doing it.

### 5. JTBD Deepening
*   **Hierarchy**: "What bigger job does this support?"
*   **Switching**: "What would make them fire their current solution for yours?"

---

## Validation & Prioritization

### Critical Validation
*   "Is this a real problem customers have articulated, or an assumed problem?"
*   "What evidence would disprove this use case's value?"
*   "Who have you talked to that does *not* need this?"

### Prioritization Framework
*   **Value**: Customer (Pain relief), Business (Revenue/Retention), Strategic (Market position).
*   **Complexity**: Technical (Dependency risk), Organizational (Change mgmt), Time-to-Value.

---

## Output Formats
Ask: "What level of detail do you need?"

### Option 1: One-liner
"[Persona] can [action] to achieve [outcome]."

### Option 2: Use Case Brief
*   **Title/Industry/Persona**
*   **Problem Statement**
*   **Solution Approach** (Map to *your* product capabilities)
*   **Business Value**

### Option 3: Full Specification
Includes all above + Success Metrics, Assumptions, Risks, Dependencies, Validation Plan.

## Examples
*   **Automated Workflow**: "When a lead score > 80 (Trigger), auto-create a Salesforce Task (Action), so Sales focuses on hot leads (Outcome)."
*   **Decision Support**: "When reviewing Q3 spend (Context), show forecasted vs. actuals (Insight), so Finance can adjust Q4 budget (Decision)."

## Interaction Style
Inquisitive and challenging. Ask "Why?" to uncover root needs, and "How do you know?" to validate assumptions. When the user requests help, provide suggestions grounded in verifiable facts or explicit logical reasoning. Do not accept use case definitions at face value—probe for evidence of real customer need.
