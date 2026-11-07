# TRISU-TEST: Property-Based Verification & Invariant Proof Rules

## Overview

These rules define the **TRISU-TEST Verification Standard**, utilizing property-based testing (PBT) to prove system invariants. Unlike traditional example-based tests, PBT defines universal truths that must hold for all valid inputs, automatically generating thousands of scenarios to find edge-case failures.

TRISU-TEST is the active enforcement of the **DUGNAD** (Functional Integrity) pillar, ensuring that the system's logic remains robust (**SISU**) even under adversarial or unanticipated input conditions.

---

## 🚦 TRISU Test Enforcement
- **Invariant-First Logic**: Analysis MUST identify testable properties (Round-trip, Idempotence, etc.) during design.
- **Shrinking Expectation**: On failure, the system MUST automatically reduce the input to the minimal reproducing case.
- **Blocking Logic**: Any [CRITICAL] or [HIGH] violation of these rules is a **Mandatory Halt**.

---

## Rule TRISU-TEST-01 [CRITICAL]: Property Identification & Invariant Mapping

**Rule**: Every logical unit MUST be analyzed for testable mathematical or business properties during the functional design phase.

**Required Categories**:
- **Round-trip**: `decode(encode(x)) == x` (Serialization, Encryption).
- **Invariant**: `measure(f(x)) == measure(x)` (Sorting, Transformation).
- **Idempotence**: `f(f(x)) == f(x)` (Normalization, Deduplication).
- **Oracle**: `f(x) == known_correct(x)` (Optimization validation).

**Verification**:
- Design artifacts include a "Testable Properties" section with categorical mappings.
- No high-complexity logic exists without at least one mapped property.

---

## Rule TRISU-TEST-02 [HIGH]: Domain-Specific Generator Integrity

**Rule**: Property tests MUST utilize structured, domain-aware generators—not just raw primitives—to ensure realistic input coverage.

**Required Controls**:
- **Constraint Enforcement**: Generators MUST respect business rules (e.g., non-negative amounts, valid email schemas).
- **Boundary Inclusion**: Generators MUST explicitly include edge cases (empty strings, zero, max values, Unicode) in every run.
- **Reusable Strategies**: Domain generators MUST be centralized as reusable assets within the testing suite.

**Verification**:
- Test code confirms custom strategies for domain objects (e.g., `Strategy<Order>`).
- Zero-usage of unbounded primitives for constrained business fields.

---

## Rule TRISU-TEST-03 [CRITICAL]: Deterministic Reproducibility

**Rule**: Every property-based test run MUST be reproducible via a logged seed value.

**Required Controls**:
- **Seed Persistence**: The unique seed for every test run MUST be logged in the CI/CD output.
- **Failure Replay**: On failure, the system MUST output the exact seed and the "shrunk" minimal failing input.
- **Deterministic CI**: CI/CD pipelines MUST log the seed for every audit-traceable run to ensure forensic replay capability.

**Verification**:
- Failure logs contain one-click replay instructions using the original seed.

---

## Rule TRISU-TEST-04 [HIGH]: Stateful Verification for Complex Workflows

**Rule**: Components managing mutable state (Caches, State Machines, Order Pipelines) MUST be verified using stateful property sequences.

**Required Controls**:
- **Model-Based Comparison**: Define a simplified, immutable model and compare its state against the real system after each generated command.
- **Random Sequence Generation**: Generate random, valid sequences of operations (Add → Update → Delete) and verify invariants hold at each step.
- **Empty Sequence Handling**: Explicitly test for null-op and empty-sequence stability.

**Verification**:
- Stateful components have a corresponding `ModelCompare` test suite.

---

## Rule TRISU-TEST-05 [HIGH]: Complementary Regression Invariants

**Rule**: Property tests MUST complement, not replace, example-based regression tests.

**Required Controls**:
- **Found-Example Pinning**: When a property test discovers a unique failure, the minimal reproducing case MUST be added to the permanent example-based test suite.
- **Critical Path Redundancy**: Business-critical paths MUST have at least one explicit example-based test for "Happy Path" documentation.

**Verification**:
- Test suite contains both `PropertyTests` and `ExampleTests` with clear separation.
