# Testing Instructions for DIAL API Parameters

## ✅ Task Completion Status

All implementation tasks have been completed and pushed to GitHub:
- **Repository**: https://github.com/vospr/ai-dial-models-parameters
- **Commit**: 21fc7c8

## 📁 Files Completed

### Individual Task Files (8 files)
1. `task/1-task-models.py` - Test different LLM models
2. `task/2-task-n.py` - Multiple completion choices (n parameter)
3. `task/3-task-temperature.py` - Control randomness
4. `task/4-task-seed.py` - Reproducibility with seed
5. `task/5-task-max_tokens.py` - Output length control
6. `task/6-task-frequency_penalty.py` - Reduce repetition
7. `task/7-task-presence_penalty.py` - Increase topic diversity
8. `task/8-task-stop.py` - Custom stop sequences

### Consolidated Test File
- **`Test.py`** - All 8 tests in one file for easy screenshot capture

## 🔧 VPN Connection Issue

**Current Status**: The DIAL API endpoint (`ai-proxy.lab.epam.com`) is not reachable.

**Troubleshooting Steps**:

1. **Verify VPN Connection**:
   ```bash
   ping ai-proxy.lab.epam.com
   ```
   Should show successful pings (not 100% packet loss)

2. **Check VPN Client**:
   - Ensure EPAM VPN client is running
   - Verify connection status shows "Connected"
   - Try disconnecting and reconnecting

3. **Test Network Access**:
   ```bash
   curl -I https://ai-proxy.lab.epam.com/openai/models
   ```
   Should return HTTP response (not timeout)

## 🚀 How to Run Tests (Once VPN is Working)

### Option 1: Run Consolidated Test File (Recommended for Screenshots)

```bash
cd /Users/apple/app-templates/ai-dial-models-parameters
source .venv/bin/activate
python Test.py
```

**Expected Output**:
- All 8 tests will run sequentially
- Clear headers for each test
- Parameter values displayed
- API responses shown
- Perfect for one comprehensive screenshot

### Option 2: Run Individual Task Files

```bash
cd /Users/apple/app-templates/ai-dial-models-parameters
source .venv/bin/activate

# Run individual tasks (each requires user input and 'exit' to finish)
python -m task.1-task-models
python -m task.2-task-n
python -m task.3-task-temperature
python -m task.4-task-seed
python -m task.5-task-max_tokens
python -m task.6-task-frequency_penalty
python -m task.7-task-presence_penalty
python -m task.8-task-stop
```

## 📸 What to Capture in Screenshot

When `Test.py` runs successfully, you'll see:

1. **Test 1**: GPT-4o response about LLM capabilities
2. **Test 2**: 3 different completions for the same question (n=3)
3. **Test 3**: Creative response with high temperature (1.5)
4. **Test 4**: 5 similar responses due to seed=42
5. **Test 5**: Truncated response (max_tokens=10) with finish_reason="length"
6. **Test 6**: Less repetitive text (frequency_penalty=2.0)
7. **Test 7**: More diverse topics (presence_penalty=2.0)
8. **Test 8**: Response stopped at double newline (stop="\n\n")

## ✅ Task Completion Summary

### Completed:
- ✅ Forked repository from khshanovskyi to vospr
- ✅ Set up virtual environment
- ✅ Installed dependencies
- ✅ Completed all 8 task files with API key configuration
- ✅ Created Test.py for simplified testing
- ✅ Pushed all changes to GitHub
- ✅ Modified task 1 for simplified testing

### Remaining:
- ⏳ Successfully run tests (requires working VPN connection)
- ⏳ Capture screenshots of test results

## 📝 Next Steps

1. **Fix VPN Connection**:
   - Contact EPAM IT support if VPN issues persist
   - Ensure you're using the correct VPN profile
   - Try different VPN servers if available

2. **Run Tests**:
   ```bash
   python Test.py
   ```

3. **Capture Screenshot**:
   - Run the test in a terminal with good font size
   - Capture the full output showing all 8 tests
   - Save as evidence of successful completion

4. **Alternative**: Run individual task files interactively for more detailed testing

## 🔗 Resources

- **Repository**: https://github.com/vospr/ai-dial-models-parameters
- **DIAL API Docs**: https://dialx.ai/dial_api
- **EPAM VPN Support**: https://support.epam.com/
- **Available Models**: https://ai-proxy.lab.epam.com/openai/models (requires VPN)

---

**Note**: All code is complete and ready to test. The only blocker is the VPN connection to EPAM's internal network.

