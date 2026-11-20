# Group C — Structured Prompt + Evidence-based Review
Two-stage workflow: first generate structured output, then run independent review to check for violations, missing items and contradictions.

## Stage 1: Generate (same as Group B structured prompt)
> You are a planning assistant.
> Task brief: {task_brief}
> Hard constraints: {constraints}
> Required deliverables: {deliverables}
> Output a structured plan including objectives, timeline, resources, sequential dependencies and acceptance criteria.

## Stage 2: Review Prompt
> Review the generated plan below against all constraints and requirements.
> Generated content: {model_output}
> Checklist:
> 1. Are all hard constraints satisfied?
> 2. Any conflicting dependencies or impossible arrangements?
> 3. Missing required deliverables?
> 4. Outdated or invalid requirements retained incorrectly?
> List all issues, then revise the final version.

## Multi-turn & Video versions follow the same two-stage logic: generate → constraint review → revise
