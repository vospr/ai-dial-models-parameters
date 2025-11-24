from task.app.main import run

# TODO:
#  Try `stop` parameter.
#  `stop` (str or list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  Like setting custom "end of response" triggers.
#       Default: None
#  User massage: Explain the key components of a Large Language Model architecture

import os
os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

# Test with stop="\n\n" (stop at double newline)
print("\n" + "="*50)
print("Testing with stop='\\n\\n' (Stop at double newline)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    stop="\n\n",
)

# Test with multiple stop sequences
print("\n" + "="*50)
print("Testing with multiple stop sequences")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"],
)

# Test with stop sequences and full JSON output to see finish_reason
print("\n" + "="*50)
print("Testing with stop sequences (Full JSON to see finish_reason)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=False,
    stop=["**Embedding Layer**", "**Transformer Blocks**"],
)

# Test without stop parameter (for comparison)
print("\n" + "="*50)
print("Testing without stop parameter (Full response)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
)

# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).
# The `finish_reason` will be set as `stop`. So, the users won't know what is the real reason why LLM has stopped generation.