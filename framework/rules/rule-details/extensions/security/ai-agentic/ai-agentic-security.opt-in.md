# AI/Agentic/ML Security — Opt-In

**Extension**: AI, Agentic, and ML System Security

## Opt-In Prompt

The following question is automatically included in the Requirements Analysis clarifying questions when this extension is loaded:

```markdown
## Question: AI/Agentic/ML Security Extension

Does this project include any AI, LLM-backed, agentic, or machine learning components?

This covers: LLM-powered features (chat, copilot, summarization, code generation), autonomous AI agents with tool use or planning, RAG pipelines and vector stores, ML model training/serving/fine-tuning, embedding pipelines, or any system where an AI model influences or drives application behavior.

A) Yes — this project includes AI/LLM/Agentic/ML components. Enforce all AI-SECURITY rules as blocking constraints.
B) No — this project has no AI, LLM, agentic, or ML components. Skip AI-SECURITY rules.
C) Uncertain — the project may incorporate AI components in the future. Enforce as advisory (non-blocking) guidance now.
X) Other (please describe after [Answer]: tag below)

[Answer]:
```
