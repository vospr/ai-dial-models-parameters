# How to Run Individual Tests Manually

## 🚀 Quick Start

### 1. Initialize Environment (One Time Setup)

```bash
# Navigate to project directory
cd /Users/apple/app-templates/ai-dial-models-parameters

# Activate virtual environment
source .venv/bin/activate
```

You should see `(.venv)` at the beginning of your terminal prompt.

---

## 🧪 Run Each Test Individually

Once the environment is activated, run any test you want:

### Test 1: Different Models
```bash
python test1_models.py
```
**Shows**: How GPT-4o responds to "What LLMs can do?"

---

### Test 2: Multiple Completions (n parameter)
```bash
python test2_n.py
```
**Shows**: 3 different responses to the same question  
**Parameter**: `n=3`

---

### Test 3: Temperature Control
```bash
python test3_temperature.py
```
**Shows**: Creative response with high randomness  
**Parameter**: `temperature=1.5`

---

### Test 4: Seed for Reproducibility
```bash
python test4_seed.py
```
**Shows**: 5 similar/identical responses due to seed  
**Parameter**: `seed=42, n=5`

---

### Test 5: Max Tokens Limit
```bash
python test5_max_tokens.py
```
**Shows**: Truncated response, finish_reason="length"  
**Parameter**: `max_tokens=10`

---

### Test 6: Frequency Penalty
```bash
python test6_frequency_penalty.py
```
**Shows**: Less repetitive text  
**Parameter**: `frequency_penalty=2.0`

---

### Test 7: Presence Penalty
```bash
python test7_presence_penalty.py
```
**Shows**: More diverse topics discussed  
**Parameter**: `presence_penalty=2.0`

---

### Test 8: Stop Sequences
```bash
python test8_stop.py
```
**Shows**: Response stops at double newline  
**Parameter**: `stop="\n\n"`

---

## 📸 Perfect for Screenshots!

Each test:
- ✅ Runs independently
- ✅ Shows clear output
- ✅ Displays parameter being tested
- ✅ Easy to capture in one screenshot

---

## 🔄 Run All Tests in Sequence

If you want to run all tests one after another:

```bash
cd /Users/apple/app-templates/ai-dial-models-parameters
source .venv/bin/activate

python test1_models.py
python test2_n.py
python test3_temperature.py
python test4_seed.py
python test5_max_tokens.py
python test6_frequency_penalty.py
python test7_presence_penalty.py
python test8_stop.py
```

Or use the consolidated version:
```bash
python Test.py
```

---

## 🛠️ Troubleshooting

### If you get "command not found: python"
Use `python3` instead:
```bash
python3 test1_models.py
```

### If you get module not found errors
Make sure virtual environment is activated:
```bash
source .venv/bin/activate
# You should see (.venv) in your prompt
```

### If connection times out
Ensure you're connected to EPAM VPN and have access to:
```
https://ai-proxy.lab.epam.com
```

---

## 📝 Test File Structure

```
test1_models.py              # Tests different LLM models
test2_n.py                   # Tests n parameter (multiple choices)
test3_temperature.py         # Tests temperature (randomness)
test4_seed.py                # Tests seed (reproducibility)
test5_max_tokens.py          # Tests max_tokens (output length)
test6_frequency_penalty.py   # Tests frequency_penalty (repetition)
test7_presence_penalty.py    # Tests presence_penalty (topic diversity)
test8_stop.py                # Tests stop sequences
```

Each file is self-contained and can be run independently!

