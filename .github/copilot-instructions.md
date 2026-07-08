# GitHub Copilot Instructions

You are assisting with a Spec-Driven Development (SDD) Python project.

## Global Rules
1. **Read Specs First**: ALWAYS read the markdown files inside `docs/specs/` before writing code for new features. The spec is the source of truth.
2. **Test-Driven**: When writing a feature based on a spec, ensure tests in `tests/` are generated to cover all scenarios defined in the spec.
3. **Code Quality**: Follow PEP 8 guidelines. Use type hints (`typing`) for all functions and methods.
4. **No Assumptions**: If a spec does not mention a specific edge case, ask the developer for clarification instead of guessing.

## Example Workflow
- User: "Implement the task creation feature."
- Copilot: Read `docs/specs/task_management.md`, write `tests/test_task_manager.py` cases, and finally update `src/task_manager/models.py`.
