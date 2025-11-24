"""
Test file with manual pauses for screenshot capture
Press Enter after each test to continue to the next one
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

def pause_for_screenshot(test_number, total_tests):
    """Pause and wait for user to press Enter"""
    print("\n" + "-"*70)
    if test_number < total_tests:
        input(f"📸 Take screenshot, then press ENTER to continue to Test {test_number + 1}...")
    else:
        input("📸 Take final screenshot, then press ENTER to finish...")

# Run all 8 tests with pauses
print("\n" + "="*70)
print("DIAL API PARAMETER EXPLORATION - SCREENSHOT MODE")
print("="*70)
print("This script will run each test and pause for screenshots.")
print("Press ENTER after taking each screenshot to continue.")
input("\nPress ENTER to start...")

# Test 1: Different Models
test_api(
    model="gpt-4o",
    prompt="What LLMs can do?",
    description="Task 1 - Different Models (GPT-4o)"
)
pause_for_screenshot(1, 8)

# Test 2: n parameter (multiple completions)
test_api(
    model="gpt-4o",
    prompt="Why is the snow white?",
    description="Task 2 - Multiple Completions (n=3)",
    n=3
)
pause_for_screenshot(2, 8)

# Test 3: temperature parameter
test_api(
    model="gpt-4o",
    prompt="Describe the sound that the color purple makes when it's angry",
    description="Task 3 - Temperature Control (temperature=1.5)",
    temperature=1.5
)
pause_for_screenshot(3, 8)

# Test 4: seed parameter
test_api(
    model="gpt-4o",
    prompt="Name a random animal",
    description="Task 4 - Seed for Reproducibility (seed=42, n=5)",
    seed=42,
    n=5
)
pause_for_screenshot(4, 8)

# Test 5: max_tokens parameter
test_api(
    model="gpt-4o",
    prompt="What is a token when we are working with LLM?",
    description="Task 5 - Max Tokens Limit (max_tokens=10)",
    max_tokens=10
)
pause_for_screenshot(5, 8)

# Test 6: frequency_penalty parameter
test_api(
    model="gpt-4o",
    prompt="Explain the water cycle in simple terms for children",
    description="Task 6 - Frequency Penalty (frequency_penalty=2.0)",
    frequency_penalty=2.0
)
pause_for_screenshot(6, 8)

# Test 7: presence_penalty parameter
test_api(
    model="gpt-4o",
    prompt="What is entropy in LLM's responses?",
    description="Task 7 - Presence Penalty (presence_penalty=2.0)",
    presence_penalty=2.0
)
pause_for_screenshot(7, 8)

# Test 8: stop parameter
test_api(
    model="gpt-4o",
    prompt="Explain the key components of a Large Language Model architecture",
    description="Task 8 - Stop Sequences (stop='\\n\\n')",
    stop="\n\n"
)
pause_for_screenshot(8, 8)

print("\n" + "="*70)
print("✅ ALL TESTS COMPLETED!")
print("="*70)

