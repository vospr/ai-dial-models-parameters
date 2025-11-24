from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

import os
os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

# Test with max_tokens=10 (very short response)
print("\n" + "="*50)
print("Testing with max_tokens=10 (Response will be truncated)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    max_tokens=10,
    print_request=False,
    print_only_content=False,
)

# Test with max_tokens=50 (moderate response)
print("\n" + "="*50)
print("Testing with max_tokens=50 (Moderate response)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    max_tokens=50,
    print_request=False,
    print_only_content=False,
)

# Test without max_tokens limit (full response)
print("\n" + "="*50)
print("Testing without max_tokens (Full response)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_request=False,
    print_only_content=False,
)

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.