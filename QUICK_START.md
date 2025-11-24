# 🚀 Quick Start Guide - Manual Test Execution

## ✅ Files Ready for Testing

**Repository**: https://github.com/vospr/ai-dial-models-parameters  
**Commit**: 1b4d1bf

---

## 📋 Step-by-Step Instructions

### Step 1: Open Terminal

### Step 2: Navigate to Project
```bash
cd /Users/apple/app-templates/ai-dial-models-parameters
```

### Step 3: Activate Virtual Environment
```bash
source .venv/bin/activate
```

You should see `(.venv)` at the start of your prompt.

### Step 4: Run Any Test!

Now you can run each test individually. Pick any one:

---

## 🧪 Individual Test Commands

### Test 1: Different Models
```bash
python test1_models.py
```

### Test 2: Multiple Completions
```bash
python test2_n.py
```

### Test 3: Temperature
```bash
python test3_temperature.py
```

### Test 4: Seed
```bash
python test4_seed.py
```

### Test 5: Max Tokens
```bash
python test5_max_tokens.py
```

### Test 6: Frequency Penalty
```bash
python test6_frequency_penalty.py
```

### Test 7: Presence Penalty
```bash
python test7_presence_penalty.py
```

### Test 8: Stop Sequences
```bash
python test8_stop.py
```

---

## 🎬 Run All Tests With Pauses (for Screenshots)

```bash
./run_all_tests.sh
```

This will:
- Run each test one by one
- Pause after each test (press Enter to continue)
- Perfect for capturing individual screenshots

---

## 📸 Example Workflow

```bash
# Step 1: Setup (one time)
cd /Users/apple/app-templates/ai-dial-models-parameters
source .venv/bin/activate

# Step 2: Run a test
python test1_models.py

# Step 3: Capture screenshot of the output

# Step 4: Run next test
python test2_n.py

# Step 5: Capture screenshot
# ... and so on
```

---

## ✅ Each Test File Contains:

- ✅ API key already configured
- ✅ Endpoint URL set
- ✅ Request properly formatted
- ✅ Clear output showing results
- ✅ Parameter values displayed
- ✅ No user input required

---

## 🔧 If You Get Errors

### "python: command not found"
Use `python3` instead:
```bash
python3 test1_models.py
```

### "No module named 'requests'"
Activate virtual environment:
```bash
source .venv/bin/activate
```

### "Connection timed out"
**VPN Issue** - Ensure you're connected to EPAM VPN with proper access to:
```
ai-proxy.lab.epam.com
```

---

## 📊 What Each Test Shows

| Test File | Parameter | What You'll See |
|-----------|-----------|-----------------|
| test1_models.py | Model | GPT-4o response |
| test2_n.py | n=3 | 3 different completions |
| test3_temperature.py | temperature=1.5 | Creative response |
| test4_seed.py | seed=42, n=5 | 5 similar responses |
| test5_max_tokens.py | max_tokens=10 | Truncated output |
| test6_frequency_penalty.py | frequency_penalty=2.0 | Less repetitive text |
| test7_presence_penalty.py | presence_penalty=2.0 | More diverse topics |
| test8_stop.py | stop="\n\n" | Early termination |

---

## 💡 Pro Tips

1. **Run tests one at a time** - Easier to capture clean screenshots
2. **Use a terminal with good contrast** - Makes screenshots clearer
3. **Zoom in** - Ensure text is readable in screenshots
4. **Full screen terminal** - Capture complete output

---

## 🎯 Quick Command Reference

```bash
# Setup (do once)
cd /Users/apple/app-templates/ai-dial-models-parameters
source .venv/bin/activate

# Run any test
python test1_models.py    # or test2, test3, etc.

# Run all with pauses
./run_all_tests.sh

# Check VPN connection
curl -I https://ai-proxy.lab.epam.com/openai/models
```

---

**Everything is ready! Just ensure VPN is connected and run the tests.** ✨

