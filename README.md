# SDD Copilot Example - Task Manager

This project demonstrates a development flow using **Spec-Driven Development (SDD)** guided by artificial intelligence (GitHub Copilot and Gemini).

## Orchestrated Workflow

This project includes an advanced configuration that divides the Artificial Intelligence into three distinct **roles** (skills), ensuring that the SDD/TDD process is strictly respected:

1. **`spec-writer`** (Product Owner): Generates the requirements document (Markdown) in `docs/specs/`.
2. **`tester`** (QA Engineer): Reads the specification and creates the automated tests in `tests/`.
3. **`sdd-coder`** (Developer): Writes the code in `src/` to make the tests pass successfully.

Check `docs/agent_orchestration.md` for more information on how to invoke each agent.

---

# Ejemplo SDD Copilot - Gestor de Tareas

Este proyecto demuestra un flujo de desarrollo utilizando **Desarrollo Guiado por Especificaciones (SDD por sus siglas en inglés)** asistido por inteligencia artificial (GitHub Copilot y Gemini).

## Flujo de Trabajo Orquestado

Este proyecto incluye una configuración avanzada que divide la Inteligencia Artificial en tres **roles** (habilidades o skills) distintos, asegurando que el proceso SDD/TDD se respete estrictamente:

1. **`spec-writer`** (Product Owner): Genera el documento de requisitos (Markdown) en `docs/specs/`.
2. **`tester`** (QA Engineer): Lee la especificación y crea las pruebas automatizadas en `tests/`.
3. **`sdd-coder`** (Desarrollador): Escribe el código en `src/` para que las pruebas pasen con éxito.

Consulta `docs/agent_orchestration.md` para obtener más información sobre cómo invocar a cada agente.
