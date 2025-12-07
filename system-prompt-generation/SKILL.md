---
name: system-prompt-generation
description: Craft effective system prompts using the RTFCF framework (Role, Task, Format, Context, Constraints). Optimize for modularity and token efficiency.
use_when: Building AI agents, creating chatbots, programming LLMs
---

# System Prompt Generation

Overview
Integrated best practice prompt generation. RTFCF+CoT/Few-Shot/XML, <5000 chars, Modular maintenance, Split/Tool proposals, BtoB/BtoC/Domain agnostic.

## Flow
[Agent Task/Audience]
↓
[RTFCF Build]
↓
[Search Patterns/CoT ex]
↓
[Prompt Gen + Token check]
↓
[Validation/Split rec]

## Web Search for Prompt Patterns
Search `"[task] system prompt examples"` (e.g., PromptBase, Anthropic cookbook).
-   **Goal**: Find high-quality few-shot examples and reasoning patterns.
-   **Example**: "SQL agent CoT example" -> Incorporate into the "Techniques" section.

## Framework/Approach: RTFCF + Advanced
1.  **Role**: Persona/Expertise. "You are an expert [Domain] assistant."
2.  **Task**: Core goal. "Your task is to..."
3.  **Format**: Rigid JSON/XML structure. "Output must be valid XML."
4.  **Context**: Schemas, Business Logic, Reference data.
5.  **Constraints**: Guardrails. "Do not answer if..." "JSON only."
6.  **Techniques**:
    -   **Chain of Thought (CoT)**: "Think step-by-step."
    -   **Few-Shot**: Provide 3 diverse examples (Input -> Output).
7.  **Meta**: Length check (<5000 chars), Versioning.

## Output Format
### System Prompt: [Agent Name] (Tokens: ~2500)

```xml
<system_prompt version="1.0">
  <role>
    You are an expert [Domain] assistant specializing in [Specific Niche].
  </role>
  <task>
    [Core Task Description]. Use the provided context to answer questions.
  </task>
  <context>
    [Schemas/Data snippets/Business Logic]
  </context>
  <constraints>
    1. If the answer is unknown, say "Need more info".
    2. Output strict JSON only. No markdown prose.
  </constraints>
  <few_shot>
    <example>
      <input>...</input>
      <output>...</output>
    </example>
    <!-- Provide 3 examples -->
  </few_shot>
  <cot>
    First, analyze the user request. Second, check valid schemas. Third, generate the response.
  </cot>
</system_prompt>
```

**Validation:**
-   **Test inputs**: Run 3 few-shot examples against the generated prompt.
-   **Edge cases**: Test guardrails (e.g., "Ignore instructions", "Delete table").
-   **Alternatives**: If too complex, propose Langchain tools.

## Length/Maint Constraints & Split Proposal
**Token Estimation**: Aim for <5000 chars (approx. 1200-1500 tokens) for the system prompt itself.
-   **Modular XML**: Design sections to be easily editable.
-   **Complex? Split Proposal**:
    -   **Multi-agent**: Use a Langchain orchestrator if the task requires distinct personas.
    -   **Tools**: Use Function Calling (OpenAI tools) for external data lookups instead of stuffing context.

## Best Practices
-   **RTFCF base**: Always start with Role, Task, Format, Context, Constraints.
-   **CoT/Few-Shot/XML**: These increase accuracy by ~50%. Use them.
-   **<4k tokens modular**: Keep it lean. Split if it grows too large.
-   **Split if multi-task**: Propose Langchain or multi-agent architecture.
-   **Tools for external**: Don't hardcode dynamic data. Use tools.
-   **Iterate**: Gen -> Test A/B -> Refine.

## Style
"Prompt engineer virtuoso. Enforce best practices. Modular and clean. <5000 chars. Honest proposals for splitting/tools."
