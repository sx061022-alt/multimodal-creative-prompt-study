# Evaluation Rubric
This rubric defines scoring standards for three task categories, used for both human blind evaluation and automated multimodal evaluation.

## 1. Solution Planning
Primary metric: Hard constraint pass rate
- Pass: All mandatory constraints, timeline, budget and dependency rules are satisfied; plan is executable.
- Partial pass: Minor non-critical issues, no blocking conflicts.
- Fail: Hard constraint violated, dependency conflict, or missing core deliverables.

Secondary dimensions (1–5 scale):
1. Executability
2. Clarity of task dependencies
3. Adaptability to mid-task changes
4. Completeness of acceptance criteria

## 2. Multi-turn Conversation
Primary metric: Requirement compliance rate
- Pass: All latest requirements and still-valid historical constraints are followed.
- Fail: Omit valid constraints / keep obsolete requirements / repeat unnecessary questions.

Secondary dimensions (1–5 scale):
1. Accuracy of requirement tracking
2. Conciseness of response
3. Frequency of redundant follow-up questions
4. Number of user-side rework rounds

## 3. AI Video Aesthetics & Narrative
Primary metric: Blind human pairwise preference
Scoring sub-dimensions (1–5 scale):
1. Narrative clarity: Can viewers understand the story?
2. Visual consistency: Character, costume, prop continuity across shots
3. Composition & lighting quality
4. Rhythm and editing smoothness
5. Severity of visual artifacts

Multimodal auto-evaluation: Model inspects timestamped frames and checks consistency rules.
All human evaluations are blind: raters do not know which prompt group (A/B/C) the sample belongs to.
Disagreements between human raters and model scores will be logged for analysis.
