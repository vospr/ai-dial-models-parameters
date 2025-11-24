"""Test 6: Frequency Penalty"""
import os
import json
import requests

os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

endpoint = "https://ai-proxy.lab.epam.com/openai/deployments/applications/public/gpt-4o/chat/completions"
headers = {"api-key": os.environ['DIAL_API_KEY'], "Content-Type": "application/json"}
request_data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the water cycle in simple terms for children"}
    ],
    "frequency_penalty": 2.0
}

print("\n" + "="*70)
print("TEST 6: Frequency Penalty (frequency_penalty=2.0)")
print("="*70)
print(f"Prompt: Explain the water cycle in simple terms for children")
print(f"Parameters: frequency_penalty=2.0 (reduces repetition)")
print("-"*70)

try:
    response = requests.post(endpoint, headers=headers, json=request_data, timeout=60)
    if response.status_code == 200:
        data = response.json()
        content = data['choices'][0]['message']['content']
        print(f"\n✓ Response:\n{content}\n")
        print("Note: High frequency penalty reduces word repetition")
    else:
        print(f"✗ Error: HTTP {response.status_code}\n{response.text}")
except Exception as e:
    print(f"✗ Exception: {str(e)}")

