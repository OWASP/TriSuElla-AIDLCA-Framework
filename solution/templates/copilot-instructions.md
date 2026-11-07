<!-- Drop this file into .github/copilot-instructions.md -->
# GitHub Copilot Instructions — TRISUELLA-AIDLCA v3.4.0

When assisting with code generation, review, or architecture in this repository:
1. Always implement security by default adhering to the OWASP Top 10, OWASP Top 10 for LLM Applications (2025 Standard), and the 9 Solution Layers of the TriSuElla Continuous Trust Platform.
2. Validate and sanitize all inputs at system and function boundaries. Never trust client or model input.
3. Apply the TRI-SU-ELLA Engine Triad: prioritize Trust (TRI) and Security (SU) invariants before admitting cognitive tasks.
4. For AI/LLM features:
   - Ensure vector store queries isolate user tenancy, require pre-retrieval authorization filters (`TRISU-DLIT-03`), and redact PII.
   - Enforce semantic validation and JSON-schema constraints on all model outputs.
   - Sandbox all agent tool-use with minimal execution privilege and mandatory HITL gates.
5. If you identify any [CRITICAL] or [HIGH] vulnerability, immediately flag it and propose a secure refactoring.
