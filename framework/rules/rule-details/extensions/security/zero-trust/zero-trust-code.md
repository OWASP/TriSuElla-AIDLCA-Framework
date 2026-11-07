# TRISU-ZTC: Zero Trust Code Principles & Auditing Rules

> **Pillar**: TILLIT (Trust & Zero-Trust) | **Version**: 3.0 | **Author**: Bhaskar Puppala (PATEL)  
> **Standard**: Application-Level Zero Trust Architecture & In-Code Invariants (NIST SP 800-207 / OWASP ASVS 4.0 / CISA ZTMM)

---

## 🧭 Overview & Philosophy

Traditional Zero Trust operates at the **perimeter and network layers** (mTLS, firewalls, identity providers, VPNs). However, in modern AI-assisted development and autonomous multi-agent systems, vulnerabilities frequently arise **inside the application logic** because code implicitly trusts internal boundaries:
- Microservices assume the upstream API gateway already authenticated and authorized the request.
- Internal functions assume callers passed sanitized parameters.
- Autonomous AI agents assume messages arriving from peer agents are authentic and harmless.
- Database access layers retrieve records using ambient IDs without verifying tenant context (leading to BOLA / IDOR).

**Zero Trust Code (ZTC)** applies *"Never Trust, Always Verify"* and *"Assume Breach"* directly to **source code, memory structures, internal APIs, and autonomous agent logic**.

---

## 🚦 Zero Trust Code Principles

1. **Never Trust Any Internal Boundary**: Treat internal functions, internal RPCs, and peer agent messages with the same hostility as raw public web requests.
2. **Explicit Verification at Every Layer**: Authorize at the object/data level (BOLA prevention), not just at the HTTP gateway perimeter.
3. **Assume Breach in Logic & Memory**: Secrets retrieved on-demand via ephemeral tokens; sensitive keys zeroized from memory; errors fail closed.
4. **Continuous In-Code Auditability**: Every state-altering function or agent action emits a tamper-evident, non-repudiable audit event before execution.

---

## 📋 Rule Specifications & Auditing Checks

### Rule TRISU-ZTC-01 [CRITICAL]: Explicit In-Code Boundary Validation
**Rule**: Every internal function, module, service endpoint, and AI agent tool MUST validate its inputs (type, schema, length, and bounds) independently. Code MUST NOT assume upstream controllers or gateways have sanitized the payload.

- **Anti-Pattern (Implicit Trust)**:
  ```python
  # INSECURE: Assumes upstream gateway validated the payload
  def process_internal_order(order_payload):
      customer_id = order_payload["customer_id"]
      db.execute(f"UPDATE accounts SET balance = balance - {order_payload['amount']} WHERE id = {customer_id}")
  ```
- **Compliant Pattern (Zero Trust Code)**:
  ```python
  from pydantic import BaseModel, Field, UUID4
  from decimal import Decimal

  class OrderInternalSchema(BaseModel):
      customer_id: UUID4
      amount: Decimal = Field(gt=0, le=100000)

  def process_internal_order(order_payload: dict, session: AuthenticatedSession):
      validated = OrderInternalSchema.model_validate(order_payload)
      db.execute(
          select(Account).where(Account.id == validated.customer_id, Account.tenant_id == session.tenant_id)
      )
  ```
- **Auditing Verification**:
  - `trisu_validator.py audit` scans for unparameterized raw SQL concatenation and raw dict/string unpacking in internal methods.

---

### Rule TRISU-ZTC-02 [CRITICAL]: Scoped Object-Level Authorization (BOLA/IDOR Invariant)
**Rule**: Every database query, cache lookup, file retrieval, and data mutation MUST explicitly bind and filter on the authenticated caller's tenant and user context. Ambient ID queries without ownership verification are strictly PROHIBITED.

- **Anti-Pattern (BOLA / IDOR Vulnerability)**:
  ```python
  # INSECURE: User A can access User B's record simply by changing the record ID
  @app.get("/documents/{doc_id}")
  def get_document(doc_id: str):
      return db.query(Document).filter(Document.id == doc_id).first()
  ```
- **Compliant Pattern (Zero Trust Code)**:
  ```python
  # SECURE: Object query is strictly scoped to authenticated user and tenant enclave
  @app.get("/documents/{doc_id}")
  def get_document(doc_id: str, current_user: User = Depends(get_current_user)):
      doc = db.query(Document).filter(
          Document.id == doc_id,
          Document.tenant_id == current_user.tenant_id,
          Document.owner_id == current_user.id
      ).first()
      if not doc:
          raise HTTPException(status_code=404, detail="Document not found")
      return doc
  ```
- **Auditing Verification**:
  - Auditing requires object-level tenancy checks on all ORM and raw SQL query expressions.

---

### Rule TRISU-ZTC-03 [HIGH]: Zero Ambient Credentials & Memory Zeroization
**Rule**: Source code MUST NOT hold global, ambient, or long-lived static credentials in memory. Sensitive cryptographic keys and tokens MUST be acquired just-in-time via workload identities (OIDC/SPIFFE) and zeroized/cleared from memory immediately following use.

- **Anti-Pattern (Ambient Secrets)**:
  ```python
  # INSECURE: Ambient static key stored globally in memory throughout process lifetime
  OPENAI_API_KEY = "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx"
  client = OpenAI(api_key=OPENAI_API_KEY)
  ```
- **Compliant Pattern (Zero Trust Code)**:
  ```python
  # SECURE: Token retrieved dynamically via Vault/AWS Secrets Manager with ephemeral lifecycle
  from secrets_vault import get_ephemeral_token, zeroize_buffer

  def execute_model_inference(prompt: str):
      token_buffer = get_ephemeral_token("ai-inference-service", ttl_seconds=300)
      try:
          response = call_llm_with_token(prompt, token=token_buffer.value)
          return response
      finally:
          zeroize_buffer(token_buffer) # Cryptographically scrubbed from RAM
  ```
- **Auditing Verification**:
  - `trisu_validator.py audit` scans for hardcoded tokens, AWS credentials, and persistent static private keys.

---

### Rule TRISU-ZTC-04 [CRITICAL]: Deterministic Fail-Closed Execution Invariant
**Rule**: All security gates, policy evaluations, and internal exception handlers MUST fail closed. Naked `except: pass` statements, empty catch blocks, or fallback logic that grants default access upon error are strictly PROHIBITED.

- **Anti-Pattern (Fail-Open Error Suppression)**:
  ```python
  # INSECURE: If policy engine fails or times out, execution continues (Fail-Open)
  def is_authorized(user, action):
      try:
          return opa_client.evaluate(user, action)
      except Exception:
          return True # DISASTROUS FAIL-OPEN!
  ```
- **Compliant Pattern (Zero Trust Code)**:
  ```python
  # SECURE: Any error, timeout, or ambiguity immediately halts and denies access (Fail-Closed)
  def is_authorized(user, action) -> bool:
      try:
          decision = opa_client.evaluate(user, action)
          return bool(decision.allow)
      except Exception as err:
          logger.critical("Security Policy Decision Point unreachable: %s", err)
          audit_logger.emit_security_fault(event="POLICY_ENGINE_TIMEOUT", user=user.id)
          return False # Mandatory Fail-Closed (DENY)
  ```
- **Auditing Verification**:
  - `trisu_validator.py audit` detects naked `except: pass` or `except Exception: pass` patterns that suppress security faults.

---

### Rule TRISU-ZTC-05 [CRITICAL]: Banned Insecure Deserialization & Dynamic Execution
**Rule**: Dynamic code execution (`eval()`, `exec()`, `new Function()`) and unsafe object deserialization (`pickle.loads()`, `yaml.load()` without SafeLoader) are strictly PROHIBITED across all application tiers and inter-agent message buses.

- **Anti-Pattern (Insecure Deserialization)**:
  ```python
  # INSECURE: Arbitrary Remote Code Execution (RCE) via pickled agent state
  agent_state = pickle.loads(untrusted_message_bytes)
  eval(f"run_tool_{tool_name}()")
  ```
- **Compliant Pattern (Zero Trust Code)**:
  ```python
  # SECURE: Strict, typed JSON schema parsing with registered dispatch dictionary
  import json
  from pydantic import ValidationError

  TOOL_DISPATCH = {
      "query_database": run_query_tool,
      "fetch_weather": run_weather_tool,
  }

  def dispatch_agent_tool(tool_name: str, payload_bytes: bytes):
      if tool_name not in TOOL_DISPATCH:
          raise SecurityException(f"Unauthorized tool requested: {tool_name}")
      parsed = json.loads(payload_bytes.decode("utf-8"))
      return TOOL_DISPATCH[tool_name](parsed)
  ```
- **Auditing Verification**:
  - `trisu_validator.py audit` statically flags instances of `eval(`, `exec(`, `pickle.loads(`, and unsafe YAML loaders.

---

### Rule TRISU-ZTC-06 [HIGH]: Continuous In-Code Audit Telemetry (Non-Repudiation)
**Rule**: Every state-altering function, privilege escalation, data deletion, financial transaction, and autonomous AI agent tool execution MUST emit an immutable, structured audit event containing caller identity, cryptographic timestamp, and parameter digest before executing.

- **Compliant Pattern (Zero Trust Code)**:
  ```python
  def delete_customer_data(customer_id: str, session: AuthenticatedSession):
      audit_event = {
          "event_id": str(uuid.uuid4()),
          "event_type": "DATA_ERASURE_REQUEST",
          "principal_id": session.user_id,
          "tenant_id": session.tenant_id,
          "target_resource": f"customer:{customer_id}",
          "timestamp": datetime.now(timezone.utc).isoformat(),
          "payload_digest": hashlib.sha256(customer_id.encode()).hexdigest(),
      }
      audit_vault.emit_immutable_log(audit_event)
      db.execute(delete(Customer).where(Customer.id == customer_id, Customer.tenant_id == session.tenant_id))
  ```
- **Auditing Verification**:
  - Mutation endpoints and agent tool handlers must demonstrate correlated audit emission calls.

---

### Rule TRISU-ZTC-07 [CRITICAL]: Unsafe Shell & Process Subprocess Execution Invariant
**Rule**: Invocation of operating system commands via dynamic shell execution (`shell=True`, `os.system()`, `popen()` with raw string concatenation) is strictly PROHIBITED. All system processes MUST be invoked with discrete, parameterized argument lists, absolute binary paths, strict execution timeouts, and sanitized environment blocks.

- **Anti-Pattern (Command Injection Vulnerability)**:
  ```python
  # INSECURE: Vulnerable to arbitrary command injection via shell=True
  import subprocess

  def convert_user_file(filename: str):
      subprocess.run(f"convert {filename} output.png", shell=True) # DISASTROUS RCE!
  ```
- **Compliant Pattern (Zero Trust Code)**:
  ```python
  # SECURE: Explicit argument list, no shell invocation, strict timeout, isolated environment
  import subprocess
  from pathlib import Path

  ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
  CONVERT_BINARY = "/usr/bin/convert"

  def convert_user_file(input_path: Path, output_path: Path):
      if input_path.suffix.lower() not in ALLOWED_EXTENSIONS:
          raise ValueError("Invalid file extension")
      # Execute with strict argument vector, no shell interpreter
      subprocess.run(
          [CONVERT_BINARY, str(input_path.resolve()), str(output_path.resolve())],
          shell=False,
          check=True,
          timeout=15, # Blast-radius bounded by time
          env={"PATH": "/usr/bin"} # Clean isolated environment
      )
  ```
- **Auditing Verification**:
  - `trisu_validator.py audit` statically checks for `shell=True` and `os.system(` calls in application code.

---

### Rule TRISU-ZTC-08 [CRITICAL]: Autonomous Agent Tool Dispatch Boundary & Confinement
**Rule**: Autonomous AI agents invoking local or remote tools MUST execute within deterministic confinement boundaries. Tool arguments synthesized by LLMs MUST undergo schema validation before execution. Any mutating, financial, external webhook, or destructive tool MUST require an attested Human-in-the-Loop (HITL) approval token before invocation.

- **Anti-Pattern (Unconstrained Agent Tool Execution)**:
  ```python
  # INSECURE: Directly dispatches LLM-synthesized tool and arguments with ambient privileges
  def on_agent_tool_call(tool_name: str, raw_arguments: dict):
      execute_dynamically(tool_name, **raw_arguments) # NO VALIDATION, NO HITL!
  ```
- **Compliant Pattern (Zero Trust Code)**:
  ```python
  # SECURE: Strict typed Pydantic schema validation, HITL gating for critical operations, timeout
  from pydantic import BaseModel, Field
  from guardrails import require_hitl_approval, emit_tool_audit

  class DatabaseDropTableToolSchema(BaseModel):
      table_name: str = Field(pattern=r"^[a-zA-Z0-9_]+$")
      tenant_id: str

  def on_agent_tool_call(tool_name: str, raw_arguments: dict, caller_context: AgentContext):
      # 1. Deterministic schema validation
      if tool_name == "drop_table":
          validated = DatabaseDropTableToolSchema.model_validate(raw_arguments)
          # 2. Enforce tenant isolation invariant
          if validated.tenant_id != caller_context.tenant_id:
              raise SecurityException("Cross-tenant mutation attempt blocked")
          # 3. Mandatory Human-In-The-Loop (HITL) gate for destructive actions
          require_hitl_approval(action="DROP_TABLE", context=validated)
          # 4. In-code audit telemetry
          emit_tool_audit(tool_name, validated, caller_context)
          return drop_table_safely(validated.table_name, validated.tenant_id)
  ```
- **Auditing Verification**:
  - AST scanning ensures all agent tool dispatchers enforce schema validation and authorization checks.

---

*OWASP TriSuElla-AIDLCA Zero Trust Code Specification v3.0 — Continuous Verification Inside Application Logic.*
