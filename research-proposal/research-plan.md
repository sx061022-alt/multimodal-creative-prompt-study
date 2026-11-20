## I. Research Objectives
This study investigates whether structured prompting, multi‑turn constraint management, and evidence‑based review can improve the output reliability of large language models and reduce user rework in real‑world tasks. Three application scenarios are covered: solution planning, multi‑turn conversation, and AI‑assisted video creation. Beyond measuring quality improvements, I will also document conditions under which the proposed methods fail, additional API invocation overhead, and tasks that still require human judgment.

| Research Area | Research Question | Hypothesis to be Verified |
|---|---|---|
| **Solution Planning** | When tasks involve simultaneous targets, timelines, resources, sequential dependencies and ad‑hoc changes, can the model produce executable plans? | Explicitly listing constraints, dependencies and acceptance criteria raises the pass rate of hard constraints. Key checks include dependency conflicts and the plan’s adaptability to mid‑task modifications. |
| **Multi‑turn Conversation** | When users supplement preferences, correct misunderstandings or narrow task scope, can the model follow updated requirements while preserving still‑valid historical constraints? | Tracking active requirements, revised items and pending confirmations reduces mis‑application of outdated requirements, omission of valid constraints and redundant follow‑up questions. |
| **AI‑Video Aesthetics** | With fixed video‑generator and rendering configurations, can refined storyboard & shot‑level prompts enhance narrative clarity, visual consistency and human preference scores of generated footage? | Decomposing creative requirements into camera movements, character‑prop continuity, composition and lighting improves alignment between outputs and creative intent. This study also measures agreement between multimodal model evaluation and human raters. |

## II. API Utilization
I will implement a reproducible experimental pipeline in Python. Each sample and experimental condition receives a unique identifier. Prompt templates, evaluation rubrics and model outputs are version‑controlled. Model snapshots will be locked for formal experiments if available; model ID, timestamps and request parameters are logged. In case of model updates during experimentation, results will be reported separately and paired retests will be conducted on key samples.

| Experimental Module | API / Processing Approach | Implementation Details |
|---|---|---|
| **Plan Generation & Multi‑turn Dialogue** | Responses API | Submit task briefs or full conversation history. Multi‑turn logic is managed locally. New constraints or corrections are injected at predefined turns. Model compliance with updated deliverables is logged. |
| **Structured Output & Rule Validation** | Structured Outputs + local scripts | Define typed fields for task steps, dependencies and acceptance criteria. Local code validates budgets, timelines, formats and mandatory deliverables. Refusals, incomplete outputs and API errors are separately recorded. |
| **Storyboard & Video Prompt Generation** | Responses API + fixed video renderer | OpenAI models generate storyboards and shot‑wise prompts. All videos are rendered by the identical local/authorized video generator with fixed resolution, duration limits, reference assets and rendering parameters. Where seeds are supported, paired seeds are used across experimental groups. |
| **Multimodal Evaluation** | Responses API with image inputs; audio transcription for dialogue‑containing clips | Generated videos are sampled into timestamped frames for inspection of characters, costumes, props, composition and camera specifications. Human raters watch full videos to assess action continuity, editing rhythm and lip‑sync performance where applicable. |
| **Batch Execution & Cost Tracking** | Batch API + local experiment logger | Independent planning, storyboard and evaluation requests are submitted in batches. Dialogue workflows with sequential dependencies run turn‑by‑turn. Input/output token counts, latency, retry counts and estimated costs are persistently logged. |

## III. Experimental Plan
### 1. Controlled Study Design
Identical source requirements, reference materials and task context are supplied across three experimental arms for each task instance:
- **Group A (Baseline: Vanilla Prompting):** Raw task instructions are directly submitted to generate plans, replies or storyboards.
- **Group B (Structured Prompting):** Hard constraints, preferences, output specifications and acceptance criteria are explicitly provided. For video tasks, shot‑by‑shot descriptions plus character‑costume‑prop continuity rules are appended.
- **Group C (Structured Prompting + Evidence‑Based Review):** On top of Group‑B inputs, an extra review pass checks for constraint violations, internal contradictions and missing deliverables before final revision. For multi‑turn tasks, currently‑active requirements are maintained and updated upon user revisions.

Primary comparisons are **B vs A** and the incremental gain of **C vs B**. All dialogue groups share the maximum allowed turn count. To isolate whether quality gains stem specifically from the review logic rather than extra compute budget, an additional equal‑cost plain‑rewrite control subset is included for review‑heavy workflows.

### 2. Dataset Scale & Test Protocol

| Task Type | Development Set | Held‑out Test Set | Formal Experiment Scale |
|---|---:|---:|---|
| Solution Planning | 20 tasks | 60 tasks | 3 groups × 3 repetitions per task = **540 total plans** |
| Multi‑turn Conversation | 20 scenarios | 60 scenarios | 3 groups × 3 repetitions per scenario = **540 dialogues**, maximum 5 model‑response turns per dialogue |
| Video Creation | 10 creative briefs | 30 creative briefs | 3 groups × 2 render repetitions per brief = **180 short clips** |

The development set is used for iterative prompt refinement and rubric calibration. The held‑out test set is partitioned by theme and source; rewritten variants of one brief only appear within one partition. Prompts, primary metrics and exclusion criteria are frozen prior to running formal experiments. Final sample sizes are finalized after pilot runs and before observing main‑study results.

Pre‑written user scripts and branching logic drive multi‑turn dialogues. For instance, budget information is only fed when the model correctly identifies missing budget parameters. Intended requirement updates are injected at identical dialogue turns across all arms. Video briefs cover character‑driven short drama, knowledge explanation and spatial‑narrative scenarios using original or properly‑licensed assets. One example use‑case: a street‑reunion sequence requiring three shots capturing passing‑by, turning‑back and evasive avoidance while preserving consistent character costumes and movement directions. Human raters separately score narrative clarity and visual aesthetics under blind conditions.

### 3. Scoring & Analysis
- **Solution Planning:** Primary metric is the pass rate of hard constraints. Executability, clarity of dependencies and adaptability to changes are further assessed via blind human sampling evaluation.
- **Multi‑turn Conversation:** Primary metric is the fraction of final outputs satisfying both updated requirements and still‑valid legacy constraints. Secondary metrics include requirement omissions, stale‑requirement mis‑application, unnecessary follow‑ups, completion turns and user‑equivalent rework frequency.
- **Video Aesthetics:** Primary outcome is blind human pairwise preference under shuffled playback order; ties are permitted. At least two independent raters evaluate each full clip along sub‑dimensions: composition‑lighting, narrative intelligibility, character‑prop consistency, pacing and visual artifacts. Automatic multimodal evaluation outputs are compared against human judgments, and high‑disagreement cases are documented.
- **Statistical Analysis:** Paired comparisons are performed at the original‑task / brief level; effect sizes and 95% confidence intervals are reported. Repeated runs per task quantify output stability; aggregation or resampling is performed at the task level. Outcomes are stratified by task difficulty, theme and model. Failure cases together with associated cost overhead are summarized.

### 4. Timeline

| Period | Activities & Deliverables |
|---|---|
| **Weeks 1‑2** | Build task corpus & asset licensing inventory; define evaluation rubrics, experimental pipelines and data retention policies; complete institutional ethics review as required by graduate‑school regulations. |
| **Weeks 3‑4** | End‑to‑end validation of API and video rendering workflows; pilot three prompting conditions on the development set; assess inter‑rater reliability, real‑world token consumption and video‑rendering overhead; lock formal‑experiment configuration. |
| **Weeks 5‑8** | Execute held‑out‑test‑set experiments; persist model outputs, errors and cost logs; run reproducibility validation on selected items using a second model. |
| **Weeks 9‑10** | Complete blind human evaluation, paired statistical analysis, cost accounting and failure‑case dissection; compare discrepancies between automatic scoring and human assessment. |
| **Weeks 11‑12** | Write experimental chapters for graduate thesis; release prompt templates, evaluation rubrics and reproducible scripts. Only properly‑licensed content is used for public demonstrations. |

## IV. Grant Request & Expected Deliverables
**Proposed initial request: 800 USD in OpenAI API credits, subject to adjustment based on pilot‑study measured consumption.**
The full experiment comprises roughly **3,510 text‑and‑multimodal API requests** covering plan generation, multi‑turn dialogue, storyboard drafting and frame‑based video evaluation. For rough budgeting illustration using published GPT‑6.2 Sol pricing assumptions: average 3,500 input tokens + 1,000 output tokens per request yields an estimated core‑experiment spend of **60 USD**. Remaining credits cover pilot experimentation, review‑pass overhead, second‑model reproducibility testing and natural usage variance. Video‑rendering expenses and human‑rater compensation are tracked separately and do not draw from this API grant.
