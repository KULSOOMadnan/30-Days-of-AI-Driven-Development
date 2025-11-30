
## 5. ⚙️ Implement Phase (`/sp.implement`)

**What it is:** The Implementation Phase executes your tasks with AI collaboration, using checkpoints to maintain human decision-making and validate against specification criteria.

**Key Points:**
- **Orchestrated Execution**: Implementation = you directing, AI executing, both validating (NOT autonomous code generation)
- **Specification as Standard**: Success criteria from your spec become objective measures of task completion
- **Checkpoint Decisions**: At each checkpoint: (1) Commit and proceed, (2) Iterate current task, or (3) Revise plan (rare)
- **Iteration as Solution**: When tasks don't meet spec, iteration refines output based on your feedback—this is normal and productive

**Workflow:**
1. Run `/sp.implement` to begin orchestrated task execution
2. AI executes tasks in dependency order, showing outputs at checkpoints
3. At each checkpoint, validate against specification success criteria
4. Make checkpoint decision (commit/iterate/revise) and explicitly authorize next phase

**Checkpoint Review Process:**
- **Success Criteria Met?** Does output match task acceptance criteria?
- **Specification Fulfilled?** Does output advance toward spec's success evals?
- **Quality Standards?** Meets constitutional standards (rigor, clarity)?
- **Ready for Next Task?** Can next task safely build on this output?

**Example Iteration:**
- AI delivers 450-word introduction (spec requires 500-700)
- You identify gap: "Below spec limit. Which argument needs expansion?"
- AI revises with expanded second argument to 520 words
- You validate: meets spec criteria ✓
- Decision: Commit and proceed

---



## Summary: The Complete Workflow


1. **Constitution**: Define project-wide quality standards (once per project)
2. **Specify**: Transform ideas into clear, measurable requirements (WHAT)
3. **Plan**: Design architecture and document decisions (HOW)
4. **Tasks**: Break plan into atomic 15-30 minute work units with checkpoints
5. **Implement**: Execute tasks with AI collaboration and checkpoint validation

**Key Principle**: Each phase builds on the previous, creating a cascade of clarity from high-level standards down to atomic execution units, with human control maintained through checkpoints at every critical boundary.