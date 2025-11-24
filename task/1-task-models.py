from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

import os
os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

# Test with gpt-4o
print("\n" + "="*50)
print("Testing with gpt-4o")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_request=False,
    print_only_content=True,
)

# Test with claude-3-7-sonnet
print("\n" + "="*50)
print("Testing with claude-3-7-sonnet@20250219")
print("="*50)
run(
    deployment_name='applications/public/claude-3-7-sonnet@20250219',
    print_request=False,
    print_only_content=True,
)

# Test with gemini-2.5-pro
print("\n" + "="*50)
print("Testing with gemini-2.5-pro")
print("="*50)
run(
    deployment_name='applications/public/gemini-2.5-pro',
    print_request=False,
    print_only_content=True,
)

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API