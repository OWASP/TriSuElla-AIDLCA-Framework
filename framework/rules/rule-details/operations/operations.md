# Operations Phase

**Purpose**: Production deployment, CI/CD pipeline generation, observability setup, incident response, and operational runbooks

**Status**: Active — fully implemented

---

## Overview

The Operations phase closes the TRISUELLA-AIDLCA loop by taking the artifacts produced in Inception and Construction all the way through to a deployable, observable, and operationally ready system. It covers four primary concerns:

1. **CI/CD Pipeline Generation** — Automated pipeline definitions for build, test, and deploy
2. **Deployment Planning and Execution** — Environment-specific deployment configurations and runbooks
3. **Observability Setup** — Monitoring, alerting, dashboards, and log management
4. **Incident Response** — Runbooks, escalation paths, and breach/incident procedures

**Stages in OPERATIONS PHASE**:
- CI/CD Pipeline Generation (CONDITIONAL)
- Deployment Planning (ALWAYS when Operations phase is entered)
- Observability Setup (CONDITIONAL)
- Incident Response Planning (CONDITIONAL)

---

# Stage: CI/CD Pipeline Generation

## When to Execute

**ALWAYS Execute IF**:
- Project is intended for repeated deployment (not a one-off script)
- Team will use version control with pull/merge requests
- Multiple environments exist (dev, staging, production)

**MAY SKIP IF**:
- Purely exploratory prototype with no deployment path
- Team has existing CI/CD pipelines that will not change

---

## Step 1: Detect CI/CD Platform

Determine the CI/CD platform in use based on workspace detection findings and user input:

| Platform | Configuration File |
|---|---|
| GitHub Actions | `.github/workflows/*.yml` |
| GitLab CI | `.gitlab-ci.yml` |
| Bitbucket Pipelines | `bitbucket-pipelines.yml` |
| Azure DevOps | `azure-pipelines.yml` |
| CircleCI | `.circleci/config.yml` |
| Jenkins | `Jenkinsfile` |
| AWS CodePipeline | `buildspec.yml` + CDK/CloudFormation |
| Generic / Unknown | Ask user |

---

## Step 2: Generate CI/CD Pipeline Definition

Generate a pipeline definition appropriate for the detected platform with the following mandatory stages:

### Mandatory Pipeline Stages

**Stage 1: Static Analysis**
- Linting and code style
- SAST scan (per `construction/build-and-test.md` SAST tooling)
- Secret detection scan
- License compliance check

**Stage 2: Build**
- Compile / transpile source code
- Generate build artifacts
- Container image build (if containerized)
- Container image security scan (if containerized)

**Stage 3: Unit and Integration Tests**
- Run unit test suite with coverage reporting
- Run integration tests
- Run property-based tests (if PBT extension is enabled)
- Fail pipeline on test failures or coverage below threshold

**Stage 4: Security Scan**
- Dependency vulnerability scan
- DAST scan against ephemeral test environment (if applicable)
- IaC security scan (Checkov, tfsec, or cfn-nag for Terraform/CloudFormation)

**Stage 5: Artifact Publishing**
- Publish versioned artifacts to registry (container registry, package registry, artifact store)
- Attach SBOM to artifact
- Sign artifact (if signing is configured)

**Stage 6: Deploy to Staging**
- Deploy to staging/pre-production environment
- Run smoke tests and health checks
- Run DAST scan against staging (if not run in Stage 4)
- Gate on manual approval for production deployment (MANDATORY)

**Stage 7: Deploy to Production**
- Requires explicit human approval gate
- Deploy using blue/green, canary, or rolling strategy as documented in deployment plan
- Run post-deployment smoke tests and health checks
- Automatic rollback trigger on health check failure
- **[AI-DLCA]** If deploying retrained AI Model Weights, a secondary Dual-Key Human-in-the-Loop (HITL) authorization is MANDATORY. Fully autonomous retraining pipelines are prohibited.

### Security and Quality Gates

The following MUST be configured as pipeline gates — failures block progression:

| Gate | Blocks | Severity |
|---|---|---|
| SAST HIGH/CRITICAL findings | Merge to main | [CRITICAL] |
| Secret detection findings | Merge to main | [CRITICAL] |
| Unit test failures | Build stage | [HIGH] |
| Dependency CVE CRITICAL | Build stage | [CRITICAL] |
| Container CVE CRITICAL | Artifact publishing | [HIGH] |
| Staging health check failure | Production deployment | [CRITICAL] |
| Missing human approval | Production deployment | [CRITICAL] |

---

## Step 3: Generate IaC Security Scan Configuration

Create configuration for Infrastructure-as-Code security scanning:

- **Terraform**: Configure tfsec or Checkov to run on every Terraform plan
- **CloudFormation**: Configure cfn-nag or Checkov on every template
- **Kubernetes**: Configure kube-score or Polaris for manifest validation
- **Helm**: Configure helm lint + Checkov on chart changes

---

## Step 4: Save Pipeline Artifacts

- Save pipeline definition to appropriate path (`.github/workflows/main.yml`, etc.)
- Save IaC scan configuration to `TRISUELLA-AIDLCA-docs/operations/cicd-pipeline.md` (documentation)
- Log completion in `TRISUELLA-AIDLCA-docs/audit.md`

---

---

# Stage: Deployment Planning

## Step 1: Document Deployment Architecture

Create `TRISUELLA-AIDLCA-docs/operations/deployment-plan.md`:

```markdown
# Deployment Plan — [System Name]

## Environment Overview
| Environment | Purpose | Cloud Account/Region | Access |
|---|---|---|---|
| Development | Developer testing | [account/region] | Developer team |
| Staging | Pre-production validation | [account/region] | Dev + QA team |
| Production | Live users | [account/region] | Ops team + deployment pipeline |

## Deployment Strategy
[Blue/Green / Canary / Rolling — with rationale]

**Blue/Green**: Zero-downtime by routing traffic between two identical environments
**Canary**: Gradual traffic shift (e.g., 5% → 25% → 100%) with automated rollback triggers
**Rolling**: Replace instances gradually; simpler but no instant rollback

## Rollback Procedure
1. [Step-by-step rollback procedure]
2. Rollback trigger conditions: [health check failure, error rate spike, manual trigger]
3. Rollback time target: < [X] minutes
4. Data rollback considerations: [database migrations, backward compatibility requirements]

## Deployment Prerequisites Checklist
- [ ] All security scans passed
- [ ] All tests pass in staging
- [ ] Human approval obtained
- [ ] Change management record created (if SOC 2 required)
- [ ] Rollback plan verified
- [ ] On-call engineer notified
- [ ] Monitoring dashboards ready
```

---

## Step 2: Generate Production Readiness Checklist

Create `TRISUELLA-AIDLCA-docs/operations/production-readiness-checklist.md`:

```markdown
# Production Readiness Checklist

## Security
- [ ] All SECURITY extension rules compliant (or exceptions documented)
- [ ] Secrets loaded from secrets manager (no hardcoded secrets)
- [ ] TLS enforced, HTTP disabled
- [ ] All HIGH/CRITICAL SAST findings resolved
- [ ] Dependency vulnerability scan clean (or exceptions documented with remediation plan)
- [ ] Container images scanned (if applicable)
- [ ] Security headers configured (HSTS, CSP, X-Frame-Options, etc.)
- [ ] Authentication and authorization implemented and tested
- [ ] Rate limiting configured on public endpoints

## Privacy and Compliance
- [ ] Privacy notice deployed (if system collects personal data)
- [ ] Data retention policies implemented
- [ ] Data subject rights mechanisms in place (if GDPR/CCPA required)
- [ ] Compliance framework requirements met (PCI/HIPAA/SOC2 as applicable)
- [ ] **AI-DLCA Model Retirement Policy**: WORM (Write-Once-Read-Many) storage configured for retention of deprecated algorithmic weights and training logs.

## Observability
- [ ] Application health check endpoint implemented and responding
- [ ] Structured logging configured and routing to centralized log service
- [ ] Metrics collection configured
- [ ] Monitoring dashboard created
- [ ] Alerts configured for critical error rates, latency, and security events
- [ ] Log retention policy configured: **180 days online + 5 years archive** [CRITICAL - IND-BFSI-02]

## Reliability
- [ ] Deployment strategy documented (blue/green, canary, rolling)
- [ ] Rollback procedure documented and tested
- [ ] Health checks implemented at load balancer / API gateway
- [ ] Auto-scaling configured (if applicable)
- [ ] DR/backup strategy documented and tested

## AI/Agentic Systems (if applicable)
- [ ] AI safety controls implemented (fail-safe, scope limitation, kill switch)
- [ ] Prompt/response logging configured
- [ ] AI abuse detection alerts configured
- [ ] Model rollback procedure documented
- [ ] Human oversight mechanism accessible to operators
```

---

---

# Stage: Observability Setup

## When to Execute

**ALWAYS Execute IF**:
- System is deployed to a non-local environment
- System has users (external or internal)
- System is part of a production or staging environment

---

## Step 1: Generate Monitoring Configuration

Create `TRISUELLA-AIDLCA-docs/operations/observability-setup.md` documenting:

### Metrics to Monitor

**Application Metrics**:
- Request rate (requests per second)
- Error rate (4xx and 5xx by endpoint)
- Latency (p50, p95, p99 response times)
- Availability (uptime percentage)

**Infrastructure Metrics**:
- CPU, memory, disk utilization
- Network throughput and error rates
- Database connection pool utilization and query latency
- Cache hit rate (if caching is used)

**Security Metrics** (MANDATORY):
- Authentication failure rate (per user and globally)
- Authorization failure rate
- Rate limit violation rate
- Unusual access patterns (off-hours, unusual geographies, privilege escalation attempts)

**AI/Agentic Metrics** (if AI extension is enabled):
- LLM API token consumption per user/session
- Tool invocation rate and failure rate per tool
- Model inference latency and error rate
- Prompt injection detection rate
- Agent loop iteration count (detect runaway agents)
- **[AI-DLCA] Layer 4 Continuous Observability**: Asynchronous telemetry tracking statistical Data/Model Drift (e.g., K-S tests) against training baselines without impacting inference latency.

---

## Step 2: Generate Alerting Configuration

Define critical alerts that MUST be configured before production deployment:

| Alert | Condition | Severity | Notification |
|---|---|---|---|
| High Error Rate | 5xx rate > 5% for 5 minutes | Critical | PagerDuty/on-call |
| High Latency | p99 latency > [X]ms for 5 minutes | Warning | Slack/email |
| Authentication Failures | > [X] failures/minute from single IP | Critical | Security team |
| Service Unavailable | Health check failures for 2 minutes | Critical | PagerDuty/on-call |
| Secret Access Anomaly | Unexpected secret retrieval patterns | Critical | Security team |
| AI Token Budget Exceeded | User exceeds token budget | Warning | Application log + alert |
| Agent Runaway | Agent iteration count > threshold | Critical | Security team + auto-terminate |

---

## Step 3: Generate Dashboard Definition

Document the monitoring dashboard structure covering the four golden signals:
- **Latency**: Response time distribution and percentiles
- **Traffic**: Request rate and volume
- **Errors**: Error rates by type and endpoint
- **Saturation**: Resource utilization approaching capacity

---

---

# Stage: Incident Response Planning

## When to Execute

**ALWAYS Execute IF**:
- System handles personal data
- System is production-facing with external users
- Security extension is enabled
- System processes financial transactions

---

## Step 1: Generate Incident Response Runbook

Create `TRISUELLA-AIDLCA-docs/operations/incident-response-runbook.md`:

```markdown
# Incident Response Runbook — [System Name]

## Incident Severity Classification
| Severity | Definition | Response Time | Escalation |
|---|---|---|---|
| P1 — Critical | System down, data breach suspected, active attack | 15 minutes | CEO, Legal, Security team |
| P2 — High | Significant performance degradation, potential data exposure | 30 minutes | Engineering lead, Security team |
| P3 — Medium | Partial outage, non-critical feature unavailable | 2 hours | On-call engineer |
| P4 — Low | Minor issues, no user impact | Next business day | Ticket queue |

## On-Call Contacts
[Document escalation chain and contact information]

## General Incident Response Steps
1. **Detect**: Alert fires or incident reported
2. **Assess**: Determine severity, affected scope, initial impact
3. **Contain**: Isolate affected components if active attack; enable maintenance mode if needed
4. **Investigate**: Root cause analysis using logs, metrics, and audit trail
5. **Remediate**: Apply fix, verify, deploy
6. **Communicate**: User/stakeholder communication per severity level
7. **Review**: Post-mortem within 5 business days for P1/P2 incidents

## Security Incident Procedure

### Suspected Data Breach (P1)
1. Immediately notify: Security lead, Legal, Engineering lead
2. **CERT-In / RBI Notification**: MUST occur within **6 hours** of detection [CRITICAL - IND-BFSI-01]
3. Preserve evidence: Do NOT delete logs; snapshot affected systems
4. Contain: Revoke compromised credentials, isolate affected systems
5. Assess scope: Determine what data was accessed, by whom, over what period (use audit logs)
6. External notification: Follow applicable regulatory deadlines (CERT-In: 6 hours; GDPR: 72 hours)
7. Post-mortem required

### Active Prompt Injection or AI Abuse (P1/P2 for AI systems)
1. Identify the affected session(s) and the adversarial inputs
2. Block the attacking user/IP
3. Review tool invocation logs for any unauthorized actions taken
4. Reverse any unauthorized actions if reversible
5. Analyze prompt logs to understand attack vector
6. Update prompt injection defenses
7. Post-mortem required

### Credential Compromise (P1)
1. Immediately rotate ALL credentials that may be affected (use secrets manager rotation)
2. Revoke all active sessions for affected users/services
3. Review access logs for the potentially compromised credential covering the window of exposure
4. Assess whether any unauthorized actions were taken
5. Notify affected users if their data may have been accessed
6. Post-mortem required

## Post-Mortem Template
```markdown
## Post-Mortem: [Incident Name] — [Date]

### Impact
[What broke, how many users affected, duration]

### Timeline
[Chronological sequence of events from alert to resolution]

### Root Cause
[The fundamental cause, not just the proximate cause]

### Contributing Factors
[What conditions allowed the root cause to manifest]

### Resolution
[What was done to resolve the incident]

### Action Items
| Action | Owner | Due Date |
|---|---|---|
| [Preventive measure] | [Name] | [Date] |

### Lessons Learned
[What did we learn that improves future operations?]
```
```

---

## Step 2: Update State Tracking

Update `TRISUELLA-AIDLCA-docs/TRISUELLA-AIDLCA-state.md`:

```markdown
## Stage Progress
### 🟡 OPERATIONS PHASE
- [x] CI/CD Pipeline Generation
- [x] Deployment Planning
- [x] Observability Setup
- [x] Incident Response Planning
```

---

## Step 3: Present Operations Completion

```markdown
# 🚀 Operations Phase Complete

> **📋 <u>**REVIEW REQUIRED:**</u>**
> Please examine the operations artifacts at: `TRISUELLA-AIDLCA-docs/operations/`
> Key files:
> - `cicd-pipeline.md` — CI/CD pipeline documentation
> - `deployment-plan.md` — Deployment strategy and rollback procedure
> - `production-readiness-checklist.md` — Pre-launch checklist
> - `observability-setup.md` — Monitoring, metrics, and alerting
> - `incident-response-runbook.md` — Incident response procedures



> **🚀 <u>**WHAT'S NEXT?**</u>**
>
> **You may:**
>
> 🔧 **Request Changes** — Update any operations artifact
> ✅ **Complete** — TRISUELLA-AIDLCA workflow is complete. Your system is ready for production deployment.

---
```
