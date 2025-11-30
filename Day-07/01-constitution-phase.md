# SPECKit Plus: Five Core Concepts

## 1. 📜 Constitution Phase (`/sp.constitution`)

**What it is:** The Constitution defines project-wide quality standards that apply to ALL work in a project, serving as immutable rules that guide every feature and phase.

**Key Points:**
- **Global vs. Feature-Specific**: Constitution = rules for ALL features (e.g., "all papers must use APA citations"). Specification = rules for ONE feature (e.g., "this paper's thesis is X").
- **Written Once**: You create the Constitution once per project, then it cascades through all specifications, plans, and tasks.
- **Testable Standards**: Standards must be measurable, not vague (✅ "Flesch-Kincaid grade 10-12" vs. ❌ "well-written").
- **The Cascade Effect**: Clear Constitution → Clear Specification → Clear Plan → Clear Tasks → Quality Implementation.

**Workflow:**
1. Run `/sp.constitution` with project principles, standards, constraints, and success criteria
2. Review generated constitution for testability and completeness
3. Commit to git BEFORE starting feature work
4. All downstream work (specs, plans, tasks) automatically respects Constitution standards

**Example Standards:**
- Citation format (APA, MLA)
- Source quality requirements (peer-reviewed, authoritative)
- Writing clarity (reading level, tone)
- Quality gates (plagiarism checks, fact verification)

---
