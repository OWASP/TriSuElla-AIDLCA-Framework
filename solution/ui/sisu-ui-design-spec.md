# Sisu Codespace Explorer: Design Specification

## 🎨 Aesthetic Profile: "Cyber-Nordic"
A high-fidelity dashboard designed for elite developers, prioritizing visual depth, glassmorphism, and glowing neon accents.

### Color Palette
- **Primary Background**: Deep Navy / Space Black (`#0a0b1e`)
- **Glass Surface**: Semi-transparent dark blue with subtle blur (`rgba(16, 18, 35, 0.7)`)
- **Primary Glow (Cyan)**: `#00f2ff` / `rgba(0, 242, 255, 1)`
- **Secondary Accent (Purple)**: `#bd00ff` / `rgba(189, 0, 255, 1)`
- **Success/Safety (Green)**: `#00ff85`
- **Warning/Error (Red/Orange)**: `#ff3d00`
- **Border/Grid**: Low-opacity white or cyan (`rgba(0, 242, 255, 0.1)`)

### Typography
- **Headings**: 'Space Grotesk' or similar geometric sans-serif.
- **Body/System**: 'Inter' or 'Roboto Mono' for data-heavy sections.

---

## 🏗️ Layout Components

### 1. Navigation Sidebar (Left)
- **Icons**: Outlined, glowing icons for core modules.
- **Labels**: 
    - 📁 **Explorer** (Active)
    - 📊 **Analysis**
    - 💬 **Chat**
    - 💻 **Terminal**
- **Bottom**: ⚙️ **Settings** (Gear icon)

### 2. Main Workspace: Explorer Tab
- **Repository Tree**: Sidebar within the workspace showing folder structure (e.g., `src/`, `main.py`, `config.yaml`).
- **Node-Based Visualization**:
    - Central interactive graph visualizing the "Brain" of the project.
    - Large "Folder" nodes (e.g., `src/`, `utils/`, `data/`) connected to smaller "File" nodes (e.g., `api.py`, `main.py`).
    - **Links**: Glowing cyan and purple lines representing imports or data flow.
    - **Particle Effects**: Subtle "data particles" moving along the links.

### 3. Repository Metadata (Right)
- **Project Name**: `SisuHub-Core`
- **Stats**:
    - Project: **SisuHub**
    - Last Commit: **3h ago**
    - Files: **1450**
    - Language: **Python/JS**

### 4. Code Preview Overlay (Bottom-Center)
- A floating glass card titled "CODE PREVIEW: main.py".
- **Syntax Highlighting**:
    ```python
    def main():
        ...
        data = load_config()
        run_analysis(data)
        ...
    ```
- **Contextual Glow**: Subtle purple/cyan border reflecting the active file's node in the graph.

---

## 📄 Lore & Symbolic Meaning
- **Sisu**: Intelligence and autonomous execution (The Brain).
- **Tillit**: Governance and security enforcement (The Shield).
- **Dugnad**: Orchestration and human-AI collaboration (The Trident).

> "TriSuElla ensures that AI systems execute with intelligence (Sisu), operate with trust (Tillit), and collaborate with purpose (Dugnad)."
