# 🚀 Publishing to GitHub Wiki: Step-by-Step Guide

This guide explains how to publish the **TriSuElla-AIDLCA-Framework** Wiki to your GitHub repository.

---

## Method 1: Push Directly via Git (Recommended - Fastest & Preserves All Pages)

GitHub manages repository wikis as independent Git repositories with the `.wiki.git` suffix.

### Step 1: Enable Wiki on GitHub (If not already enabled)
1. Go to your GitHub repository (e.g., `https://github.com/OWASP/TriSuElla-AIDLCA-Framework` or `https://github.com/thundel/TriSuElla-AIDLCA-Framework`).
2. Click **Settings** → Under **Features**, ensure the **Wikis** checkbox is checked.
3. Click the **Wiki** tab at the top of your repository and click **Create the first page** (you can type anything and click **Save page** to initialize the wiki Git repository).

### Step 2: Clone the Wiki Repository Locally
In your terminal, clone the wiki repository into a temporary folder:
```bash
# For OWASP repository:
git clone https://github.com/OWASP/TriSuElla-AIDLCA-Framework.wiki.git trisuella-wiki

# Or for personal repository:
git clone https://github.com/thundel/TriSuElla-AIDLCA-Framework.wiki.git trisuella-wiki
```

### Step 3: Copy Wiki Files from `wiki/` into the Cloned Repo
Copy all markdown files from the project's `wiki/` folder into the cloned `trisuella-wiki/` folder:

```bash
# On Linux / macOS / Git Bash:
cp -r wiki/* trisuella-wiki/

# On Windows (PowerShell):
Copy-Item -Path "wiki\*" -Destination "trisuella-wiki\" -Recurse -Force
```

### Step 4: Commit and Push
```bash
cd trisuella-wiki
git add .
git commit -m "docs(wiki): publish TriSuElla-AIDLCA-Framework v3.4.0 documentation suite"
git push origin master # Note: GitHub Wiki default branch is usually master or main
```

Your GitHub Wiki is now live with the full sidebar navigation, diagrams, and pages!

---

## Method 2: Copy-Paste via GitHub Web Interface (No Git Clone Required)

If you prefer using the GitHub browser interface:

1. Navigate to your repository on GitHub.
2. Click the **Wiki** tab.
3. Click **New Page** in the top right.
4. **Page 1 (Home)**:
   - Title: `Home`
   - Content: Copy the content from [`wiki/Home.md`](Home.md)
   - Click **Save Page**.
5. **Page 2 (_Sidebar)**:
   - Click **New Page** or edit the sidebar.
   - Title: `_Sidebar`
   - Content: Copy the content from [`wiki/_Sidebar.md`](_Sidebar.md)
   - Click **Save Page**.
6. **Page 3 (_Footer)**:
   - Click **New Page**.
   - Title: `_Footer`
   - Content: Copy the content from [`wiki/_Footer.md`](_Footer.md)
   - Click **Save Page**.
7. **Remaining Pages**:
   - Create pages titled exactly:
     - `The-9-Solution-Layers` (from [`wiki/The-9-Solution-Layers.md`](The-9-Solution-Layers.md))
     - `TRI-SU-ELLA-Engine-Triad` (from [`wiki/TRI-SU-ELLA-Engine-Triad.md`](TRI-SU-ELLA-Engine-Triad.md))
     - `CLI-Tooling-and-DevSecOps` (from [`wiki/CLI-Tooling-and-DevSecOps.md`](CLI-Tooling-and-DevSecOps.md))
     - `Multi-Standard-Compliance-Crosswalk` (from [`wiki/Multi-Standard-Compliance-Crosswalk.md`](Multi-Standard-Compliance-Crosswalk.md))
     - `Multi-Agent-Lifecycle-Architecture` (from [`wiki/Multi-Agent-Lifecycle-Architecture.md`](Multi-Agent-Lifecycle-Architecture.md))
     - `Quickstart-and-Scaffolding` (from [`wiki/Quickstart-and-Scaffolding.md`](Quickstart-and-Scaffolding.md))
     - `TriSuElla-AIDLCA-Framework-Wiki` (from [`wiki/TriSuElla-AIDLCA-Framework-Wiki.md`](TriSuElla-AIDLCA-Framework-Wiki.md))

---

## Method 3: Instant Single-Page Wiki

If you want a single comprehensive page:
1. Click **Wiki** → Edit the `Home` page.
2. Copy and paste the entire content of [`wiki/TriSuElla-AIDLCA-Framework-Wiki.md`](TriSuElla-AIDLCA-Framework-Wiki.md).
3. Click **Save Page**.

Everything (architecture, engines, layers, commands, multi-agent pipeline, and crosswalk matrix) will be accessible in a single scrollable document!
