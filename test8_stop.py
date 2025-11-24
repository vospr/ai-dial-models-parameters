"""Test 8: Stop Sequences"""
import os
import json
import requests

os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

endpoint = "https://ai-proxy.lab.epam.com/openai/deployments/applications/public/gpt-4o/chat/completions"
headers = {"api-key": os.environ['DIAL_API_KEY'], "Content-Type": "application/json"}
request_data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the key components of a Large Language Model architecture"}
    ],
    "stop": "\n\n"
}

print("\n" + "="*70)
print("TEST 8: Stop Sequences (stop='\\n\\n')")
print("="*70)
print(f"Prompt: Explain the key components of a Large Language Model architecture")
print(f"Parameters: stop='\\n\\n' (stops at double newline)")
print("-"*70)

try:
    response = requests.post(endpoint, headers=headers, json=request_data, timeout=60)
    if response.status_code == 200:
        data = response.json()
        content = data['choices'][0]['message']['content']
        finish_reason = data['choices'][0]['finish_reason']
        print(f"\n✓ Response:\n{content}\n")
        print(f"Finish reason: {finish_reason} (should be 'stop')")
        print("Note: Response stopped at first double newline")
    else:
        print(f"✗ Error: HTTP {response.status_code}\n{response.text}")
except Exception as e:
    print(f"✗ Exception: {str(e)}")

