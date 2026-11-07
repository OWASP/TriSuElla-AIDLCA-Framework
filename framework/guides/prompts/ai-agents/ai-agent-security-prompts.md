# AI / Agent Prompts — Secure AI System Design and Implementation

## A-01: Design a Secure LLM-Powered Feature

```
Design a secure [FEATURE TYPE] feature powered by an LLM.

Feature description: [describe what the feature does for the user]
LLM provider: [OpenAI GPT-4 / Claude / Gemini / local model / etc.]
User input involved: [what does the user provide as input?]
Sensitive data involved: [does user data, PII, or business data get included in prompts?]
Output type: [generated text / structured JSON / code / actions]

Design the feature with these security controls:

1. Prompt injection prevention:
   - How is user input separated from system instructions?
   - What input sanitisation is applied before user input reaches the model?
   - How does the system handle inputs that attempt to override the system prompt?

2. Data minimisation in prompts:
   - What is the minimum context needed for the model to do its job?
   - How is PII and sensitive data kept out of prompts (or tokenised before inclusion)?
   - If using RAG: how is retrieval scoped to the user's authorized data?

3. Output handling:
   - Is model output treated as trusted or untrusted?
   - What validation is applied to model output before it is stored or displayed?
   - If output is rendered in HTML: how is XSS prevented?
   - If output is executable (code, SQL, shell): how is it sandboxed?

4. Rate limiting and abuse prevention:
   - Token budget per user/session
   - Rate limit on model API calls
   - Anomaly detection for unusually long prompts or high-frequency calls

5. Audit and observability:
   - What is logged for each model call? (metadata — not full prompt if it contains PII)
   - How are model failures and unexpected outputs detected?

Produce: a design document with architecture diagram (ASCII), security controls table, and identified risks.
```

---

## A-02: Secure Multi-Agent System Design

```
Design a secure multi-agent workflow for:

Task: [describe the task the agents should accomplish]
Agents needed: [list the agent types — e.g., Planner, Researcher, Coder, Reviewer]
External tools/APIs the agents use: [list what the agents can call]
Sensitive data in scope: [what data do agents access?]

Design requirements:
1. Agent identity: each agent has a unique identity with a declared tool_scope (allow-list of permitted tool calls)
2. Agent communication: how do agents pass information? (event bus / shared state / direct call). Specify the message format and how messages are authenticated.
3. Orchestrator role: which component assigns tasks? How does it validate agent identity before accepting results?
4. Human-in-the-loop gates: which actions require human approval before an agent proceeds? (e.g., writing to production, sending external communications)
5. Prompt injection defense: how does each agent handle untrusted content from tool outputs or web content?
6. Audit trail: produce a schema for the audit log that records every agent action, tool call, and decision
7. Failure handling: what happens when an agent fails, produces unexpected output, or violates its scope?

Output:
- Agent taxonomy table (agent name | purpose | tool_scope | input | output)
- Communication flow diagram (ASCII)
- Security controls per agent
- Audit log schema
```

---

## A-03: RAG Security Design

```
Design a secure Retrieval-Augmented Generation (RAG) system for:

Use case: [what documents are being indexed and retrieved?]
Users: [who queries the RAG system? single user? multi-tenant?]
Data sensitivity: [what is the classification of the indexed documents?]
Vector database: [Pinecone / Weaviate / Qdrant / pgvector / Chroma / etc.]
Embedding model: [OpenAI / local / etc.]

Address these security requirements:

1. Access control at indexing time:
   - How are document permissions captured at index time?
   - How is metadata about document access rights stored alongside the vector embedding?

2. Access control at retrieval time:
   - How does the query include the user's identity and role?
   - How does the retrieval filter ensure user A cannot retrieve user B's documents?
   - What happens if the access control metadata is missing? (fail closed)

3. PII and sensitive data in the index:
   - Is PII scrubbed from documents before indexing?
   - If PII must be indexed: how is it protected? (Encrypted chunks? Access-controlled segments?)

4. Embedding poisoning prevention:
   - How is the document ingestion pipeline secured? (only trusted sources, integrity verification)
   - How are adversarial documents detected before indexing?

5. Retrieval audit:
   - Log every retrieval: user/agent identity, query hash, chunk IDs returned, timestamp

6. Data residency:
   - Do any vector databases or embedding APIs process data outside allowed jurisdictions?

Output: RAG architecture diagram + security controls per component + risk table.
```

---

## A-04: LLM Output Validation

```
Implement output validation for an LLM that produces [OUTPUT TYPE]:

Context: [describe the system and what the LLM is supposed to produce]
Output format expected: [free text / JSON / code / SQL / markdown / etc.]
What could go wrong: [what harmful or malformed outputs are you concerned about?]

Implement:
1. Schema validation: parse and validate the output against the expected structure; reject malformed output
2. Content safety checks:
   - Does the output contain PII it was not supposed to include?
   - Does it contain secrets or credentials (scan output with the same secret detection patterns used in code)
   - Does it contain instructions that could be executed if rendered (JS in HTML context, SQL injection patterns if output becomes a query)
3. Hallucination / grounding check: if the output should be grounded in source documents, verify citations exist in the provided context
4. Length and token validation: reject outputs that are abnormally short or long
5. Retry strategy: if validation fails, what is the retry prompt? How many retries before escalating to human review?

Generate the validation code with clear comments explaining each check.
```

---

## A-05: Prompt Template Security Review

```
Review this LLM prompt template for security issues:

[PASTE YOUR PROMPT TEMPLATE]

Check for:
1. Prompt injection surface: where can user input be injected? Is it clearly delimited from instructions?
2. Secret or key exposure: does the prompt contain API keys, passwords, or internal configuration?
3. Sensitive data inclusion: does the prompt include PII, health data, or financial data that could be logged?
4. System prompt extraction risk: could a user ask the model to reveal the system prompt? How is it protected?
5. Scope boundary: does the prompt clearly constrain what the model should and should not do?
6. Jailbreak resistance: does the prompt include explicit instructions about refusing out-of-scope requests?

For each issue found: explain the risk and provide an improved version of the template section.
```

---

## A-06: MCP Server Security Review

```
Review this MCP (Model Context Protocol) server configuration for security:

[PASTE YOUR MCP SERVER CONFIG OR DESCRIPTION]

Check for:
1. Authentication: does the MCP server require authentication from clients? What mechanism?
2. Tool scope: is the list of exposed tools the minimum necessary? Are any overly broad tools exposed?
3. Input validation: does the server validate inputs to each tool before executing?
4. Output sanitisation: are tool outputs sanitised before being returned to the model?
5. Secret handling: are any secrets or credentials accessible through MCP tools?
6. Rate limiting: is there a rate limit on tool calls?
7. Audit logging: is every tool call logged?
8. Network exposure: is the MCP server accessible only to authorised clients?

Provide a hardened MCP server configuration addressing each issue.
```
