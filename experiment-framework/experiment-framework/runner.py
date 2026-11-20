"""
Main experiment runner
Control three groups: A / B / C
"""
from config import *

def run_group_a(task_content: str):
    """Baseline group A"""
    prompt = f"Please write an executable project plan for the given task brief: {task_content}"
    return prompt

def run_group_b(task_content: str, constraints: str):
    """Structured group B"""
    prompt = f"""
You are a planning assistant.
Task brief: {task_content}
Hard constraints: {constraints}
Output structured plan with timeline, resources, dependencies and acceptance criteria.
Mark conflicts if found.
"""
    return prompt

def run_group_c(task_content: str, constraints: str):
    """Structured + review group C"""
    gen_prompt = run_group_b(task_content, constraints)
    review_prompt = """
Review the generated content against all constraints.
Checklist:
1. All hard constraints satisfied?
2. Any conflicting dependencies?
3. Missing deliverables?
4. Outdated requirements retained?
List issues and revise final version.
"""
    return gen_prompt, review_prompt

if __name__ == "__main__":
    print("Experiment runner loaded, ready for test")
