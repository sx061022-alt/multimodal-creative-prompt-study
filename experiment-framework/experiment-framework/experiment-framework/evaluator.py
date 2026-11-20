"""
Evaluation module, implement the rubric
"""

def evaluate_plan(result: str, hard_constraints: list):
    """Evaluate solution planning task"""
    score_info = {
        "pass_status": None,
        "executability": 0,
        "dependency_clarity": 0,
        "adaptability": 0,
        "acceptance_completeness": 0
    }
    return score_info

def evaluate_conversation(result: str, req_list: list):
    """Evaluate multi-turn conversation task"""
    score_info = {
        "compliance_pass": None,
        "track_accuracy": 0,
        "conciseness": 0,
        "redundant_question": 0
    }
    return score_info

def evaluate_video(storyboard: str):
    """Evaluate video storyboard"""
    score_info = {
        "narrative_clarity": 0,
        "visual_consistency": 0,
        "composition_light": 0,
        "rhythm": 0,
        "artifact_severity": 0
    }
    return score_info
