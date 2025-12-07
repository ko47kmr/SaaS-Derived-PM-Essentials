# Product Manager Skills Suite

A comprehensive collection of Claude Code skills designed to support product managers throughout the entire product lifecycle - from strategic planning to execution and iteration.

## Skills Catalog

### 📊 Strategy & Discovery
*   [competitive-analysis](competitive-analysis/SKILL.md): Porter's 5 Forces, SWOT.
*   [use-case-discovery](use-case-discovery/SKILL.md): JTBD validation.
*   [kano-model-analysis](kano-model-analysis/SKILL.md): Feature prioritization.
*   [market-sizing](market-sizing/SKILL.md): TAM/SAM/SOM.
*   [persona-development](persona-development/SKILL.md): B2B Personas.
*   [customer-journey-mapping](customer-journey-mapping/SKILL.md): Lifecycle maps.

### 📝 Planning & Specification
*   [phased-development](phased-development/SKILL.md): MVP -> Scale.
*   [prd-generation](prd-generation/SKILL.md): Detailed Specs.
*   [success-metrics](success-metrics/SKILL.md): KPIs & North Star.
*   [user-story-generation](user-story-generation/SKILL.md): Agile Stories.
*   [ticket-generation](ticket-generation/SKILL.md): Jira/Linear Tickets.

### 🔍 Review & Validation
*   [prd-competitive-assessment](prd-competitive-assessment/SKILL.md): Market Fit.
*   [prd-review-engineering](prd-review-engineering/SKILL.md): Technical Feasibility.
*   [prd-review-customer](prd-review-customer/SKILL.md): Usability.
*   [risk-analysis](risk-analysis/SKILL.md): Mitigation.

### 🧪 Quality & Testing
*   [test-case-generation](test-case-generation/SKILL.md): Functional/Edge cases.
*   [test-spec-generation](test-spec-generation/SKILL.md): Test Plans.

### 🚀 Go-to-Market
*   [demo-scenario](demo-scenario/SKILL.md): Demo Scripts.
*   [user-documentation](user-documentation/SKILL.md): Guides.
*   [release-notes](release-notes/SKILL.md): Customer Comms.
*   [stakeholder-pitch](stakeholder-pitch/SKILL.md): Executive Buy-in.

### 🔄 Iteration & AI
*   [feedback-analysis](feedback-analysis/SKILL.md): Theme extraction.
*   [system-prompt-generation](system-prompt-generation/SKILL.md): Agent Programming.
*   [system-prompt-update](system-prompt-update/SKILL.md): Safe, Iterative Updates.

## How to Use
These skills are designed to be used with Claude Code or the Agent SDK.
Ensure the `pm-skills-suite` directory is in your `.claude/skills` path or configured in your agent settings.

## Adapting for Other Platforms (Gemini Gems, GPTs)
While designed for Claude, these skills function effectively as robust system prompts and can be adapted for Google Gemini Gems or OpenAI GPTs.

**Adaptation Steps:**
1.  **Extract Core Instructions**: Copy the **Framework/Approach**, **Output Format**, and **Best Practices** sections from the `SKILL.md` file.
2.  **Define Persona**: Use the **Overview** and **Interaction Style** sections to define the AI's persona.
3.  **Configure**:
    *   **Gemini Gems**: Paste the combined content into the "Instructions" field.
    *   **GPTs**: Paste the combined content into the "Instructions" field of the GPT builder.
4.  **Note**: These prompts are optimized for Claude (e.g., XML tag usage). You may need to verify performance and adjust formatting slightly for other models.

## About this Project

**Purpose & Authorship**  
This repository was created for the purpose of personal technical verification and as a contribution to knowledge sharing among Product Managers. A significant portion of this content was written with the assistance of **Antigravity** (powered by Google's Gemini models).

**Context & Scope**  
While these skills are grounded in **B2B SaaS Product Management** experience, they have been generalized to be applicable to **B2C** and other domains where possible. The frameworks and examples provided are for illustrative purposes and should be adapted to your specific context.

**Contribution**  
We welcome contributions! If you have suggestions for new skills, improvements to existing ones, or adaptations for different industries, please feel free to open a pull request or submit an issue.

**Disclaimer**  
This repository is provided as a template and educational resource. It is not affiliated with any specific company or organization.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
