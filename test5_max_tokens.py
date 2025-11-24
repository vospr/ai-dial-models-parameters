"""Test 5: Max Tokens Limit"""
import os
import json
import requests

os.environ['DIAL_API_KEY'] = 'dial-fxbasxs2h6t7brhnbqs36omhe2y'

endpoint = "https://ai-proxy.lab.epam.com/openai/deployments/applications/public/gpt-4o/chat/completions"
headers = {"api-key": os.environ['DIAL_API_KEY'], "Content-Type": "application/json"}
request_data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is a token when we are working with LLM?"}
    ],
    "max_tokens": 10
}

print("\n" + "="*70)
print("TEST 5: Max Tokens Limit (max_tokens=10)")
print("="*70)
print(f"Prompt: What is a token when we are working with LLM?")
print(f"Parameters: max_tokens=10 (response will be truncated)")
print("-"*70)

try:
    response = requests.post(endpoint, headers=headers, json=request_data, timeout=60)
    if response.status_code == 200:
        data = response.json()
        content = data['choices'][0]['message']['content']
        finish_reason = data['choices'][0]['finish_reason']
        tokens = data.get('usage', {}).get('total_tokens', 'N/A')
        print(f"\n✓ Response:\n{content}\n")
        print(f"Finish reason: {finish_reason} (should be 'length')")
        print(f"Tokens used: {tokens}")
    else:
        print(f"✗ Error: HTTP {response.status_code}\n{response.text}")
except Exception as e:
    print(f"✗ Exception: {str(e)}")

