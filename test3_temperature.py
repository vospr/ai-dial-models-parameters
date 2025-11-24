"""Test 3: Temperature Control"""
import os
import json
import requests

os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

endpoint = "https://ai-proxy.lab.epam.com/openai/deployments/applications/public/gpt-4o/chat/completions"
headers = {"api-key": os.environ['DIAL_API_KEY'], "Content-Type": "application/json"}
request_data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Describe the sound that the color purple makes when it's angry"}
    ],
    "temperature": 1.5
}

print("\n" + "="*70)
print("TEST 3: Temperature Control (temperature=1.5)")
print("="*70)
print(f"Prompt: Describe the sound that the color purple makes when it's angry")
print(f"Parameters: temperature=1.5 (high creativity)")
print("-"*70)

try:
    response = requests.post(endpoint, headers=headers, json=request_data, timeout=60)
    if response.status_code == 200:
        data = response.json()
        content = data['choices'][0]['message']['content']
        print(f"\n✓ Response:\n{content}\n")
    else:
        print(f"✗ Error: HTTP {response.status_code}\n{response.text}")
except Exception as e:
    print(f"✗ Exception: {str(e)}")

