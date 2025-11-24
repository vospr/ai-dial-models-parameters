from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

import os
os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

# Test with temperature=0.0 (deterministic)
print("\n" + "="*50)
print("Testing with temperature=0.0 (Deterministic)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    temperature=0.0,
)

# Test with temperature=0.5 (balanced)
print("\n" + "="*50)
print("Testing with temperature=0.5 (Balanced)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    temperature=0.5,
)

# Test with temperature=1.0 (default - creative)
print("\n" + "="*50)
print("Testing with temperature=1.0 (Creative)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    temperature=1.0,
)

# Test with temperature=1.5 (very creative)
print("\n" + "="*50)
print("Testing with temperature=1.5 (Very Creative)")
print("="*50)
run(
    deployment_name='applications/public/gpt-4o',
    print_only_content=True,
    temperature=1.5,
)

# Optional: Test with temperature=2.1 (exceeds recommended range)
print("\n" + "="*50)
print("Testing with temperature=2.1 (Exceeds recommended range)")
print("="*50)
try:
    run(
        deployment_name='applications/public/gpt-4o',
        print_only_content=True,
        temperature=2.1,
    )
except Exception as e:
    print(f"Error: {e}")