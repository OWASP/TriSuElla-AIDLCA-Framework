# Contributing to TriSuElla-AIDLCA Framework / Platform 🚀

Thank you for your interest in contributing to the **TriSuElla-AIDLCA Platform**! Community contributions are vital to advancing continuous trust, security, AI compliance, and automated risk governance. 

By contributing to this project, you help build a safer AI ecosystem for everyone.

---

## ⚖️ Legal Framework & Licensing Terms

To protect the integrity of the project, all contributors must adhere to strict licensing and intellectual property guidelines.

### 1. Inbound License Agreement
By submitting a Pull Request (PR), issue, or documentation update to this repository, you explicitly agree that your contributions are governed by the **Apache License, Version 2.0** and applicable **Creative Commons** terms. 
* You maintain the copyright to your individual changes.
* You grant a permanent, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright and patent license to anyone using this software.

### 2. Developer Certificate of Origin (DCO)
To ensure clear lineage and intellectual property safety, we require all commits to be signed off using the **Developer Certificate of Origin (DCO)**. This certifies that you have the legal right to submit the code.

To sign your work, simply add a `Signed-off-by` line to your commit messages (or use `git commit -s`):
```text
Signed-off-by: Jane Doe <jane.doe@example.com>
```

### 3. Commercial & Enterprise Distribution Boundary
This repository hosts the official open-source upstream core. The author, **Bhaskar Puppala (PATEL)**, and authorized entities maintain separate, proprietary commercial distributions containing advanced enterprise features, UI components, and custom orchestration wrappers under an *All Rights Reserved* structure. 
* Contributing code here **does not** grant you rights or ownership over separate commercial variations of this platform.
* Upstream bug fixes or features contributed here may be merged into the commercial engine to ensure framework synchronization.
* See also [COMMERCIAL.md](COMMERCIAL.md) and [TRADEMARKS.md](TRADEMARKS.md).

---

## 🧭 Where does my change go?

| Your change | Folder | Also do |
|---|---|---|
| New or edited rule, architecture, guide, prompt | `framework/` | If it adds or renames a rule ID, run `./solution/cli/trisu map --write` |
| Scanner, CLI, template, agent, UI | `solution/` | Add a fixture and a test in `solution/cli/tests/` |
| Executable code of any kind | `solution/` only | `framework/` must stay documents (a test enforces this) |

## 🛠️ Code of Conduct & Contribution Flow

We aim to maintain a welcoming, inclusive, and professional community. Please review the official **OWASP Code of Conduct** before interacting with the project.

### Step 1: Search and Discuss
Before writing any code, search the repository's active **Issues** and **Pull Requests** to ensure someone else isn't already working on the same item. For significant feature additions, please open a new Issue to discuss the architecture first.

### Step 2: Code Architecture Alignment
Your code must strictly align with the platform's core infrastructure metrics:
* Ensure new rules or invariant checks fit cleanly into one of the **33 Domain Families**.
* Write clear, declarative code. The platform relies on strict deterministic logic to evaluate trust.

### Step 3: Branching & Testing
1. Fork the repository and create your branch from `main`: `git checkout -b feature/my-amazing-rule`.
2. Add automated unit tests verifying both **positive** (compliance passed) and **negative** (invariant violated) conditions. Run them with `python -m unittest discover -s solution/cli/tests -v`.
3. Run local security linter checks to ensure no vulnerabilities are introduced.

### Step 4: Submit a Clean PR
* Provide a detailed summary of the changes in your PR description.
* Reference the specific Issue number being addressed (e.g., `Closes #104`).
* Ensure your commit log is clean, descriptive, and **DCO signed-off**.

---

## 📩 Contact & Escalation

For security-sensitive disclosures, please do not open a public issue. Reach out directly to the Project Maintainer:
* **Principal Maintainer:** Bhaskar Puppala (PATEL)
* **Professional Profile:** [LinkedIn](https://www.linkedin.com/in/bhaskerkpatel/)
