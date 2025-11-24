"""Test 4: Seed for Reproducibility"""
import os
import json
import requests

os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

endpoint = "https://ai-proxy.lab.epam.com/openai/deployments/applications/public/gpt-4o/chat/completions"
headers = {"api-key": os.environ['DIAL_API_KEY'], "Content-Type": "application/json"}
request_data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Name a random animal"}
    ],
    "seed": 42,
    "n": 5
}

print("\n" + "="*70)
print("TEST 4: Seed for Reproducibility (seed=42, n=5)")
print("="*70)
print(f"Prompt: Name a random animal")
print(f"Parameters: seed=42, n=5 (should produce similar results)")
print("-"*70)

try:
    response = requests.post(endpoint, headers=headers, json=request_data, timeout=60)
    if response.status_code == 200:
        data = response.json()
        choices = data.get("choices", [])
        print(f"\n✓ Generated {len(choices)} choices with seed=42:\n")
        for i, choice in enumerate(choices, 1):
            content = choice.get("message", {}).get("content", "")
            print(f"Choice {i}: {content}")
        print("\nNote: With same seed, results should be mostly identical")
    else:
        print(f"✗ Error: HTTP {response.status_code}\n{response.text}")
except Exception as e:
    print(f"✗ Exception: {str(e)}")

