# Build and Test

**Purpose**: Build all units and execute comprehensive testing strategy

## Prerequisites
- Code Generation must be complete for all units
- All code artifacts must be generated
- Project is ready for build and testing

---

## Step 1: Analyze Testing Requirements

Analyze the project to determine appropriate testing strategy:
- **Unit tests**: Already generated per unit during code generation
- **Integration tests**: Test interactions between units/services
- **Performance tests**: Load, stress, and scalability testing
- **End-to-end tests**: Complete user workflows
- **Contract tests**: API contract validation between services
- **Security tests**: Vulnerability scanning, penetration testing

---

## Step 2: Generate Build Instructions

Create `TRISUELLA-AIDLCA-docs/construction/build-and-test/build-instructions.md`:

```markdown
# Build Instructions

## Prerequisites
- **Build Tool**: [Tool name and version]
- **Dependencies**: [List all required dependencies]
- **Environment Variables**: [List required env vars]
- **System Requirements**: [OS, memory, disk space]

## Build Steps

### 1. Install Dependencies
\`\`\`bash
[Command to install dependencies]
# Example: npm install, mvn dependency:resolve, pip install -r requirements.txt
\`\`\`

### 2. Configure Environment
\`\`\`bash
[Commands to set up environment]
# Example: export variables, configure credentials
\`\`\`

### 3. Build All Units
\`\`\`bash
[Command to build all units]
# Example: mvn clean install, npm run build, brazil-build
\`\`\`

### 4. Verify Build Success
- **Expected Output**: [Describe successful build output]
- **Build Artifacts**: [List generated artifacts and locations]
- **Common Warnings**: [Note any acceptable warnings]

## Troubleshooting

### Build Fails with Dependency Errors
- **Cause**: [Common causes]
- **Solution**: [Step-by-step fix]

### Build Fails with Compilation Errors
- **Cause**: [Common causes]
- **Solution**: [Step-by-step fix]
```

---

## Step 3: Generate Unit Test Execution Instructions

Create `TRISUELLA-AIDLCA-docs/construction/build-and-test/unit-test-instructions.md`:

```markdown
# Unit Test Execution

## Run Unit Tests

### 1. Execute All Unit Tests
\`\`\`bash
[Command to run all unit tests]
# Example: mvn test, npm test, pytest tests/unit
\`\`\`

### 2. Review Test Results
- **Expected**: [X] tests pass, 0 failures
- **Test Coverage**: [Expected coverage percentage]
- **Test Report Location**: [Path to test reports]

### 3. Fix Failing Tests
If tests fail:
1. Review test output in [location]
2. Identify failing test cases
3. Fix code issues
4. Rerun tests until all pass
```

---

## Step 4: Generate Integration Test Instructions

Create `TRISUELLA-AIDLCA-docs/construction/build-and-test/integration-test-instructions.md`:

```markdown
# Integration Test Instructions

## Purpose
Test interactions between units/services to ensure they work together correctly.

## Test Scenarios

### Scenario 1: [Unit A] → [Unit B] Integration
- **Description**: [What is being tested]
- **Setup**: [Required test environment setup]
- **Test Steps**: [Step-by-step test execution]
- **Expected Results**: [What should happen]
- **Cleanup**: [How to clean up after test]

### Scenario 2: [Unit B] → [Unit C] Integration
[Similar structure]

## Setup Integration Test Environment

### 1. Start Required Services
\`\`\`bash
[Commands to start services]
# Example: docker-compose up, start test database
\`\`\`

### 2. Configure Service Endpoints
\`\`\`bash
[Commands to configure endpoints]
# Example: export API_URL=http://localhost:8080
\`\`\`

## Run Integration Tests

### 1. Execute Integration Test Suite
\`\`\`bash
[Command to run integration tests]
# Example: mvn integration-test, npm run test:integration
\`\`\`

### 2. Verify Service Interactions
- **Test Scenarios**: [List key integration test scenarios]
- **Expected Results**: [Describe expected outcomes]
- **Logs Location**: [Where to check logs]

### 3. Cleanup
\`\`\`bash
[Commands to clean up test environment]
# Example: docker-compose down, stop test services
\`\`\`
```

---

## Step 5: Generate Performance Test Instructions (If Applicable)

Create `TRISUELLA-AIDLCA-docs/construction/build-and-test/performance-test-instructions.md`:

```markdown
# Performance Test Instructions

## Purpose
Validate system performance under load to ensure it meets requirements.

## Performance Requirements
- **Response Time**: < [X]ms for [Y]% of requests
- **Throughput**: [X] requests/second
- **Concurrent Users**: Support [X] concurrent users
- **Error Rate**: < [X]%

## Setup Performance Test Environment

### 1. Prepare Test Environment
\`\`\`bash
[Commands to set up performance testing]
# Example: scale services, configure load balancers
\`\`\`

### 2. Configure Test Parameters
- **Test Duration**: [X] minutes
- **Ramp-up Time**: [X] seconds
- **Virtual Users**: [X] users

## Run Performance Tests

### 1. Execute Load Tests
\`\`\`bash
[Command to run load tests]
# Example: jmeter -n -t test.jmx, k6 run script.js
\`\`\`

### 2. Execute Stress Tests
\`\`\`bash
[Command to run stress tests]
# Example: gradually increase load until failure
\`\`\`

### 3. Analyze Performance Results
- **Response Time**: [Actual vs Expected]
- **Throughput**: [Actual vs Expected]
- **Error Rate**: [Actual vs Expected]
- **Bottlenecks**: [Identified bottlenecks]
- **Results Location**: [Path to performance reports]

## Performance Optimization

If performance doesn't meet requirements:
1. Identify bottlenecks from test results
2. Optimize code/queries/configurations
3. Rerun tests to validate improvements
```

---

## Step 6: Generate Additional Test Instructions (As Needed)

Based on project requirements, generate additional test instruction files:

### Contract Tests (For Microservices)
Create `TRISUELLA-AIDLCA-docs/construction/build-and-test/contract-test-instructions.md`:
- API contract validation between services
- Consumer-driven contract testing
- Schema validation

### Security Tests
Create `TRISUELLA-AIDLCA-docs/construction/build-and-test/security-test-instructions.md` with the following mandatory sections:

#### SAST (Static Application Security Testing)
- **Purpose**: Analyze source code for security vulnerabilities without executing the code
- **Tool selection by language**:

| Language | Recommended SAST Tools |
|---|---|
| JavaScript/TypeScript | Semgrep, ESLint security plugin, njsscan |
| Python | Bandit, Semgrep, Safety |
| Java | SpotBugs + FindSecBugs, Semgrep, SonarQube |
| Go | Gosec, Semgrep |
| C#/.NET | Security Code Scan, Semgrep |
| Ruby | Brakeman |
| PHP | PHPStan + security rules, Psalm |
| Any language | Semgrep (rule sets available for all major languages) |

- **Execution**: SAST MUST run in CI/CD on every pull request and MUST block merge on HIGH or CRITICAL findings
- **Baseline**: Establish a clean baseline on project start; all new findings introduced by a PR are blocking
- **Configuration**: Document which rule sets are enabled and any accepted false-positive suppressions (with justification and owner)

#### DAST (Dynamic Application Security Testing)
- **Purpose**: Test running application for security vulnerabilities by sending crafted HTTP requests
- **Tool selection**:

| Scenario | Recommended Tool |
|---|---|
| Web application / REST API | OWASP ZAP (Zed Attack Proxy) |
| GraphQL API | OWASP ZAP + GraphQL scan |
| gRPC services | Semgrep for proto files + manual review |
| Containerized staging environment | OWASP ZAP automated scan |

- **Execution**: DAST MUST run against a deployed staging/test environment on every release candidate build
- **Scope**: Document the DAST scope (included/excluded endpoints) and authentication configuration
- **Minimum checks**: SQL injection, XSS, CSRF, authentication bypass, insecure direct object reference, security misconfiguration, sensitive data exposure
- **Findings**: HIGH and CRITICAL DAST findings MUST be resolved before production deployment

#### Secret Detection Scan
- Run secret detection against the entire repository and all build artifacts before deployment
- Tools: git-secrets, detect-secrets, TruffleHog, GitGuardian
- MUST scan: source code, config files, IaC templates, Docker layers, environment files
- Any detected secrets MUST be rotated immediately and treated as compromised, not just removed from code

#### Dependency Vulnerability Scan
- Run dependency vulnerability scan with up-to-date CVE database
- Tools: npm audit / yarn audit (JS), pip-audit / Safety (Python), OWASP Dependency-Check (Java/.NET), Grype (multi-language), Snyk
- CRITICAL and HIGH severity CVEs in direct dependencies MUST block deployment
- HIGH severity CVEs in transitive dependencies MUST have a documented remediation plan with deadline

#### Container Image Scan (if containerized)
- Scan all container images for OS and package vulnerabilities before pushing to registry
- Tools: Trivy, Grype, Snyk Container, Amazon ECR scanning, Docker Scout
- CRITICAL CVEs MUST be remediated before production deployment
- Images MUST be built from supported, non-EOL base images

#### AI/LLM Security Tests (if AI extension is enabled)
- **Prompt injection test suite**: Test a battery of known prompt injection payloads against all LLM-consuming endpoints
- **Indirect injection tests**: Test with adversarial content in retrieved documents, emails, and external data sources
- **Tool invocation boundary tests**: Verify that LLM-driven tool calls are rejected for out-of-scope tools or invalid parameters
- **Output validation tests**: Verify that malicious LLM outputs are blocked from reaching downstream systems
- **Rate limiting tests**: Verify that LLM endpoints enforce per-user rate limits

#### Penetration Testing Guidance
- **Scope Definition**: Document the in-scope systems, IP ranges, endpoints, and attack types for penetration testing
- **Frequency**: Annual penetration test minimum; after significant architectural changes
- **Types**: External network pen test, web application pen test, API pen test; add social engineering and physical tests for high-security environments
- **Remediation SLA**: Define remediation SLAs by severity (Critical: 7 days, High: 30 days, Medium: 90 days, Low: next release)
- **Report Retention**: Pen test reports MUST be retained for compliance purposes (minimum 1 year)

### End-to-End Tests
Create `TRISUELLA-AIDLCA-docs/construction/build-and-test/e2e-test-instructions.md`:
- Complete user workflow testing
- Cross-service scenarios
- UI testing (if applicable)

---

## Step 7: Generate Test Summary

Create `TRISUELLA-AIDLCA-docs/construction/build-and-test/build-and-test-summary.md`:

```markdown
# Build and Test Summary

## Build Status
- **Build Tool**: [Tool name]
- **Build Status**: [Success/Failed]
- **Build Artifacts**: [List artifacts]
- **Build Time**: [Duration]

## Test Execution Summary

### Unit Tests
- **Total Tests**: [X]
- **Passed**: [X]
- **Failed**: [X]
- **Coverage**: [X]%
- **Status**: [Pass/Fail]

### Integration Tests
- **Test Scenarios**: [X]
- **Passed**: [X]
- **Failed**: [X]
- **Status**: [Pass/Fail]

### Performance Tests
- **Response Time**: [Actual] (Target: [Expected])
- **Throughput**: [Actual] (Target: [Expected])
- **Error Rate**: [Actual] (Target: [Expected])
- **Status**: [Pass/Fail]

### Additional Tests
- **Contract Tests**: [Pass/Fail/N/A]
- **Security Tests**: [Pass/Fail/N/A]
- **E2E Tests**: [Pass/Fail/N/A]

## Overall Status
- **Build**: [Success/Failed]
- **All Tests**: [Pass/Fail]
- **Ready for Operations**: [Yes/No]

## Next Steps
[If all pass]: Ready to proceed to Operations phase for deployment planning
[If failures]: Address failing tests and rebuild
```

---

## Step 8: Update State Tracking

Update `TRISUELLA-AIDLCA-docs/TRISUELLA-AIDLCA-state.md`:
- Mark Build and Test stage as complete
- Update current status

---

## Step 9: Present Results to User

Present comprehensive message:

```
"🔨 Build and Test Complete!

**Build Status**: [Success/Failed]

**Test Results**:
✅ Unit Tests: [X] passed
✅ Integration Tests: [X] scenarios passed
✅ Performance Tests: [Status]
✅ Additional Tests: [Status]

**Generated Files**:
1. ✅ build-instructions.md
2. ✅ unit-test-instructions.md
3. ✅ integration-test-instructions.md
4. ✅ performance-test-instructions.md (if applicable)
5. ✅ [additional test files as needed]
6. ✅ build-and-test-summary.md

Review the summary in TRISUELLA-AIDLCA-docs/construction/build-and-test/build-and-test-summary.md

**Ready to proceed to Operations stage for deployment planning?""
```

---

## Step 10: Log Interaction

**MANDATORY**: Log the phase completion in `TRISUELLA-AIDLCA-docs/audit.md`:

```markdown
## Build and Test Stage
**Timestamp**: [ISO timestamp]
**Build Status**: [Success/Failed]
**Test Status**: [Pass/Fail]
**Files Generated**:
- build-instructions.md
- unit-test-instructions.md
- integration-test-instructions.md
- performance-test-instructions.md
- build-and-test-summary.md

---
```
