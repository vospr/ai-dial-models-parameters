from task.app.main import run

# TODO:
#  Try the `n` parameter with different models (`deployment_name`). With the parameter `n`, we can configure how many
#       chat completion choices to generate for each input message
#  User massage: Why is the snow white?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

import os
os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

# Test with gpt-4o and n=3
print("\n" + "="*50)
print("Testing with gpt-4o and n=3")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    n=3,
    print_request=False,
    print_only_content=False,
)

# Test with claude-3-7-sonnet and n=2
print("\n" + "="*50)
print("Testing with claude-3-7-sonnet@20250219 and n=2")
print("="*50)
run(
    deployment_name='applications/public/claude-3-7-sonnet@20250219',
    n=2,
    print_request=False,
    print_only_content=False,
)

# Test with gemini-2.5-pro and n=4
print("\n" + "="*50)
print("Testing with gemini-2.5-pro and n=4")
print("="*50)
run(
    deployment_name='applications/public/gemini-2.5-pro',
    n=4,
    print_request=False,
    print_only_content=False,
)

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.
