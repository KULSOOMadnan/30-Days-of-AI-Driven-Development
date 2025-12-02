<!--
Sync Impact Report:
Version change: N/A -> 0.1.0
Modified principles: None (all new)
Added sections: Core Principles, Key Standards, Error Handling, Testing Requirements, Constraints, Success Criteria, Governance
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ⚠ pending
- .specify/templates/spec-template.md ⚠ pending
- .specify/templates/tasks-template.md ⚠ pending
- .gemini/commands/sp.adr.toml ⚠ pending
- .gemini/commands/sp.analyze.toml ⚠ pending
- .gemini/commands/sp.checklist.toml ⚠ pending
- .gemini/commands/sp.clarify.toml ⚠ pending
- .gemini/commands/sp.constitution.toml ⚠ pending
- .gemini/commands/sp.git.commit_pr.toml ⚠ pending
- .gemini/commands/sp.implement.toml ⚠ pending
- .gemini/commands/sp.phr.toml ⚠ pending
- .gemini/commands/sp.plan.toml ⚠ pending
- .gemini/commands/sp.specify.toml ⚠ pending
- .gemini/commands/sp.tasks.toml ⚠ pending
Follow-up TODOs: None
-->
# Basic Calculator using Python with Test-Driven Development (TDD) Constitution

## Core Principles

### Test-First Development
Write failing tests before any production code. This ensures that features are designed with testability in mind and that all code is covered by automated tests.

### Code Quality
Clean, readable Python following PEP 8. Adherence to style guides promotes consistency, maintainability, and collaboration within the codebase.

### Reliability
Handle errors gracefully with clear messages. The system must provide informative feedback for unexpected situations, preventing crashes and guiding users to correct usage.

### Simplicity
One function, one purpose. Each component should have a single, well-defined responsibility, making the code easier to understand, test, and debug.

## Key Standards
- RED-GREEN-REFACTOR cycle mandatory: Write test first, make it pass, then refactor.
- 100% test coverage for all operations.
- PEP 8 compliance (use flake8 or pylint).
- Type hints required for all functions.
- Docstrings required for all functions.
- pytest as testing framework.

## Error Handling
- Division by zero MUST raise `ZeroDivisionError`.
- Invalid inputs MUST raise `TypeError` with clear messages.
- All exceptions MUST be documented in docstrings.

## Testing Requirements
- Test naming convention: `test_<function>_<scenario>`.
- Tests MUST cover happy path, edge cases, and error conditions.
- Use Arrange-Act-Assert pattern for clear test structure.

## Constraints
- Python 3.10+ MUST be used.
- Command-line interface only; no graphical user interface (GUI).
- Only basic operations are supported: Add, Subtract, Multiply, Divide.
- No external calculation libraries are permitted.
- Functions MUST return numeric results, not print them.

## Success Criteria
- All tests pass (100% green).
- 100% test coverage achieved.
- Zero linting errors.
- Type hints pass mypy checks.
- Clear documentation in `README.md`.

## Governance
This Constitution outlines the foundational principles and standards for the project.
Amendments to this document require a documented proposal, team approval, and a plan for migrating existing practices if necessary.
Compliance with these principles will be reviewed periodically to ensure ongoing adherence and project health.

**Version**: 0.1.0 | **Ratified**: 2025-12-02 | **Last Amended**: 2025-12-02