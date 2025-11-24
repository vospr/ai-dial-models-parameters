"""
Simplified test file for all 8 DIAL API parameter tasks
Each task runs once with one parameter and one model for easy screenshot capture
"""
import os
import json
import requests

# Set API key
os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

DIAL_ENDPOINT = "https://ai-proxy.lab.epam.com/openai/deployments/{model}/chat/completions"

def test_api(model, prompt, description, **kwargs):
    """Simple test function to call DIAL API"""
    print("\n" + "="*70)
    print(f"TEST: {description}")
    print("="*70)
    print(f"Model: {model}")
    print(f"Prompt: {prompt}")
    if kwargs:
        print(f"Parameters: {kwargs}")
    print("-"*70)
    
    endpoint = DIAL_ENDPOINT.format(model=model)
    headers = {
        "api-key": os.environ['DIAL_API_KEY'],
        "Content-Type": "application/json"
    }
    
    request_data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        **kwargs
    }
    
    try:
        response = requests.post(endpoint, headers=headers, json=request_data, timeout=60)
        
        if response.status_code == 200:
            data = response.json()
            choices = data.get("choices", [])
            
            if len(choices) > 1:
                print(f"\n✓ Generated {len(choices)} choices:")
                for i, choice in enumerate(choices, 1):
                    content = choice.get("message", {}).get("content", "")
                    print(f"\n  Choice {i}:")
                    print(f"  {content[:100]}..." if len(content) > 100 else f"  {content}")
            else:
                content = choices[0].get("message", {}).get("content", "")
                finish_reason = choices[0].get("finish_reason", "")
                print(f"\n✓ Response:")
                print(f"  {content}")
                print(f"\n  Finish reason: {finish_reason}")
                
                # Show token usage if available
                usage = data.get("usage", {})
                if usage:
                    print(f"  Tokens: {usage.get('total_tokens', 'N/A')}")
        else:
            print(f"✗ Error: HTTP {response.status_code}")
            print(f"  {response.text[:200]}")
    except Exception as e:
        print(f"✗ Exception: {str(e)}")

# Run all 8 tests
print("\n" + "="*70)
print("DIAL API PARAMETER EXPLORATION - SIMPLIFIED TESTS")
print("="*70)

# Test 1: Different Models
test_api(
    model="applications/public/gpt-4o",
    prompt="What LLMs can do?",
    description="Task 1 - Different Models (GPT-4o)"
)

# Test 2: n parameter (multiple completions)
test_api(
    model="applications/public/gpt-4o",
    prompt="Why is the snow white?",
    description="Task 2 - Multiple Completions (n=3)",
    n=3
)

# Test 3: temperature parameter
test_api(
    model="applications/public/gpt-4o",
    prompt="Describe the sound that the color purple makes when it's angry",
    description="Task 3 - Temperature Control (temperature=1.5)",
    temperature=1.5
)

# Test 4: seed parameter
test_api(
    model="applications/public/gpt-4o",
    prompt="Name a random animal",
    description="Task 4 - Seed for Reproducibility (seed=42, n=5)",
    seed=42,
    n=5
)

# Test 5: max_tokens parameter
test_api(
    model="applications/public/gpt-4o",
    prompt="What is a token when we are working with LLM?",
    description="Task 5 - Max Tokens Limit (max_tokens=10)",
    max_tokens=10
)

# Test 6: frequency_penalty parameter
test_api(
    model="applications/public/gpt-4o",
    prompt="Explain the water cycle in simple terms for children",
    description="Task 6 - Frequency Penalty (frequency_penalty=2.0)",
    frequency_penalty=2.0
)

# Test 7: presence_penalty parameter
test_api(
    model="applications/public/gpt-4o",
    prompt="What is entropy in LLM's responses?",
    description="Task 7 - Presence Penalty (presence_penalty=2.0)",
    presence_penalty=2.0
)

# Test 8: stop parameter
test_api(
    model="applications/public/gpt-4o",
    prompt="Explain the key components of a Large Language Model architecture",
    description="Task 8 - Stop Sequences (stop='\\n\\n')",
    stop="\n\n"
)

print("\n" + "="*70)
print("ALL TESTS COMPLETED!")
print("="*70)

