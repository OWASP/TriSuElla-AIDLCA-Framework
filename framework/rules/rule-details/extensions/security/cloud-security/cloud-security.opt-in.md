# Cloud Security — Opt-In

**Extension**: Platform-Agnostic Cloud Security (AWS / Azure / GCP / Multi-Cloud / Kubernetes)

## Opt-In Prompt

The following question is automatically included in the Requirements Analysis clarifying questions when this extension is loaded:

```markdown
## Question: Cloud Security Extension

Is this system deployed to or hosted on cloud infrastructure?

This covers: any deployment to AWS, Azure, GCP, DigitalOcean, Hetzner, Fly.io, Vercel, Railway, or similar cloud providers; containerised workloads on Kubernetes (EKS, AKS, GKE, self-managed); serverless functions (Lambda, Azure Functions, Cloud Functions, Cloudflare Workers); or any multi-cloud or hybrid-cloud architecture.

A) Yes, Public Cloud (AWS / Azure / GCP or other provider) — enforce all CLOUD-SEC rules as blocking constraints
B) Yes, Kubernetes (managed or self-managed) — enforce all CLOUD-SEC rules with emphasis on container and workload identity rules
C) Yes, Serverless / Edge — enforce CLOUD-SEC rules applicable to serverless architectures
D) Yes, Multi-Cloud or Hybrid — enforce all CLOUD-SEC rules across all providers in scope
E) No — on-premise only with no cloud services involved. Skip CLOUD-SEC rules.
X) Other (describe deployment model after [Answer]: tag)

[Answer]:
```
