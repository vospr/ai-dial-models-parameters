from task.app.main import run

# TODO:
#  Try `presence_penalty` parameter.
#  Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's
#  likelihood to talk about new topics. Higher values == more topic diversity.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: What is an entropy in LLM's responses?

import os
os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

# Test with presence_penalty=-2.0 (encourages staying on topic)
print("\n" + "="*50)
print("Testing with presence_penalty=-2.0 (Encourages staying on topic)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    presence_penalty=-2.0,
)

# Test with presence_penalty=0.0 (default, no penalty)
print("\n" + "="*50)
print("Testing with presence_penalty=0.0 (Default)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    presence_penalty=0.0,
)

# Test with presence_penalty=1.0 (moderate topic diversity)
print("\n" + "="*50)
print("Testing with presence_penalty=1.0 (Moderate topic diversity)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    presence_penalty=1.0,
)

# Test with presence_penalty=2.0 (high topic diversity)
print("\n" + "="*50)
print("Testing with presence_penalty=2.0 (High topic diversity)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    presence_penalty=2.0,
)

# In the final result, we can see that the higher `presence_penalty` (2.0) the more LLM is trying to add topics that
# somehow related to the main topic.
# For Anthropic and Gemini this parameter will be ignored