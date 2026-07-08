# General Rules for AI Agents

These rules apply to any agentic AI operating in this workspace.

<RULE>
**Spec-Driven Enforcer**
Never write logic in `src/` without first verifying that a corresponding spec exists in `docs/specs/` and tests exist in `tests/`. If a user asks you to implement something new, prompt them to write the specification first or offer to draft the specification for them.
</RULE>

<RULE>
**Synchronous Execution Enforcer**
Agents and skills MUST NOT be executed in parallel under any circumstance. The Spec-Driven Development lifecycle requires strict sequential execution:
1. Specifications must be fully written and saved BEFORE test generation begins.
2. Tests must be fully written and saved BEFORE code implementation begins.
Always wait for the previous step (or agent/skill invocation) to completely finish its filesystem operations before triggering the next one.
</RULE>

<RULE>
**Role Segregation Enforcer**
DO NOT perform tasks that belong to specialized roles yourself if you are acting as a general agent. You MUST explicitly invoke or delegate to the corresponding skill:
- If asked to write or update specifications in `docs/specs/`, invoke `spec-writer`.
- If asked to write or update tests in `tests/`, invoke `qa-tester`.
- If asked to write or update source code in `src/`, invoke `sdd-coder`.
This strict delegation guarantees the separation of concerns.
</RULE>
