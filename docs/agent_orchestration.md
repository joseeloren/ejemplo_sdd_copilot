# Agent Orchestration for SDD

This project defines an AI-assisted workflow simulating a development team through **orchestrated roles**.

## Available Roles (Skills)

1. **`spec-writer`**: The Product Owner. Writes the specifications in `docs/specs/`.
2. **`tester`**: The QA Engineer. Writes the tests in `tests/` based on the specification, without touching the code.
3. **`sdd-coder`**: The Developer. Writes the source code in `src/` strictly to make the tests pass.

## Workflow (The "Step-by-Step")

1. **Ideation**: The user invokes the `spec-writer` ("Hey @agent or use the spec-writer skill to create a specification to add priority support").
2. **Testing**: Once the specification is created, the user calls the `tester` to generate the test suite in `tests/`.
3. **Development**: Finally, the user calls the `sdd-coder` to implement the code in `src/` that makes the QA tests pass.
4. **Validation**: The user or the agent runs `pytest`.

By segmenting the artificial intelligence by roles, we force the SDD/TDD methodology, preventing the AI from generating the implementation code before the requirements and tests are clear.
