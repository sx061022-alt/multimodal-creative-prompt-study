"""
Experiment global configuration
"""

# Model setting
MODEL_NAME = "deepseek-v4.1-flash"
API_KEY = ""  # Fill your key later
BASE_URL = ""

# Experiment groups
GROUP_A = "baseline"
GROUP_B = "structured"
GROUP_C = "structured_review"

# Experiment scale
SAMPLE_COUNT_PLAN = 60
SAMPLE_COUNT_CONVERSATION = 60
SAMPLE_COUNT_VIDEO = 30

# Output path
OUTPUT_DIR = "./experiment_output"
LOG_DIR = "./logs"
