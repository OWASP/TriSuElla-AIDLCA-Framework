# [OPT-IN REQUIRED] AI Development Lifecycle Architecture (AI-DLCA)

> **Extension Name**: AI-DLCA Governance & Lifecycle (ISO 5338/5259/42001)
> **Trigger**: AI, MLOps, LLM, or GenAI project components detected.

The user is requesting to build an Artificial Intelligence system. AI systems introduce unique probabilistic risks (Model Drift, Bias, Semantic Attacks) that traditional deterministic software engineering lifecycles cannot manage. 

You **MUST** offer to activate the AI-DLCA Governance extension to enforce ISO 5338, ISO 5259, and ISO 42001 lifecycle constraints.

**Prompt the user with:**
> "I detect this software involves AI/ML components. Because AI systems are probabilistic, they require rigorous, specialized lifecycle governance (ISO 5338, ISO 5259 data gates, and ISO 42001 oversight). Should I activate the **AI-DLCA Governance** extension to mathematically govern the data engineering, versioning, hitl-retraining, and Layer 4 observability pipelines?"

If the user answers YES, record "AI-DLCA Governance: Enabled" in the state file and apply the `ai-dlca.md` rules throughout the workflow.
