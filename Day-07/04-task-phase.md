
## 4. 📝 Tasks Phase (`/sp.tasks`)

**What it is:** The Tasks Phase breaks the implementation plan into atomic work units (15-30 minute tasks) with explicit dependencies and human-controlled checkpoints.

**Key Points:**
- **Atomic Task Unit**: 15-30 minute work with a single, testable acceptance criterion that produces one verifiable output
- **Checkpoint Pattern**: Agent completes task → Human reviews → Human approves → Continue (maintains human control throughout execution)
- **Dependency Graph**: Visual representation showing which tasks must complete before others can start
- **Separation of Concerns**: Research tasks (find sources, extract points) separate from writing tasks, with checkpoints between phases

**Workflow:**
1. Run `/sp.tasks` to generate atomic task breakdown with dependencies
2. Review tasks for atomicity (15-30 min, single criterion, one output)
3. Verify clear acceptance criteria (testable, measurable)
4. Understand checkpoint sequence (where human reviews occur)

**Example Task Structure:**
- **Phase 1**: Research Foundation (3 tasks) → CHECKPOINT 1
- **Phase 2**: Content Research (4 tasks) → CHECKPOINT 2
- **Phase 3**: Writing and Synthesis (2 tasks) → CHECKPOINT 3
- **Phase 4**: Review and Finalization (1 task) → CHECKPOINT 4

**Task Example:**
- **Task 2.1**: Research Section 2 - Find Credible Sources (20 min)
- **Acceptance**: "5+ sources identified; each peer-reviewed OR from domain expert; full citations recorded"
- **Output**: Bibliography update with Section 2 sources

---
