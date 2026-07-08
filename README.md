# SDD Copilot Example - Task Manager

This project demonstrates a development flow using **Spec-Driven Development (SDD)** guided by artificial intelligence (GitHub Copilot and Gemini).

## Orchestrated Workflow

This project includes an advanced configuration that divides the Artificial Intelligence into three distinct **roles** (skills), ensuring that the SDD/TDD process is strictly respected:

1. **`spec-writer`** (Product Owner): Generates the requirements document (Markdown) in `docs/specs/`.
2. **`qa-tester`** (QA Engineer): Reads the specification and creates the automated tests in `tests/`.
3. **`sdd-coder`** (Developer): Writes the code in `src/` to make the tests pass successfully.

Check `docs/agent_orchestration.md` for more information on how to invoke each agent.
