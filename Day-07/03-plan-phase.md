## 3. 🧠 Plan Phase (`/sp.plan`)

**What it is:** The Plan Phase transforms the "WHAT" of your specification into the "HOW" of architecture and implementation strategy.

**Key Points:**
- **Architecture Blueprint**: Breaks specification into components, phases, and dependencies while identifying design decisions
- **ADRs (Architectural Decision Records)**: Documents WHY choices were made, including context, alternatives considered, rationale, and consequences (positive AND negative)
- **ADR Significance Test**: Create ADR only if (1) long-term consequences, (2) multiple alternatives existed, (3) someone will question it later
- **Three-Layer Hierarchy**: Spec defines WHAT (success criteria) → Plan defines HOW (architecture) → Tasks define WORK UNITS (atomic pieces)

**Workflow:**
1. Run `/sp.plan` to generate implementation plan with components, phases, dependencies
2. Review plan for architecture completeness and specification alignment
3. Run `/sp.adr` to document key architectural decisions
4. Verify ADRs include context, alternatives, rationale, and consequences

**Example ADR Decision:**
- **Decision**: Use research-concurrent approach (research while writing each section)
- **Alternatives**: Research-first (gather all sources before writing)
- **Rationale**: Keeps research focused and relevant to sections being written
- **Consequences**: (+) Faster initial writing, (-) May need additional research passes

---
