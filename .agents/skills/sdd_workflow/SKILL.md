---
name: sdd-workflow
description: Validates the SDD development lifecycle (Spec -> Test -> Code). Use when starting a new feature.
---

# SDD Workflow Skill

## Instructions

This skill acts as the master orchestrator for the SDD lifecycle.
When the user wants to implement a new feature:
1. DO NOT implement anything directly.
2. Delegate the task immediately by invoking the **`spec-writer`** skill, passing along the user's requirements.
3. The `spec-writer` will automatically chain to `tester`, which will automatically chain to `sdd-coder`.

## Examples
- User: "Use sdd-workflow to add due dates to tasks."
- Agent Action: You internally invoke the `spec-writer` skill to start the autonomous SDD chain.
