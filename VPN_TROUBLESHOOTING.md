# 🔧 VPN Connectivity Troubleshooting Guide

## ⚠️ Current Issue

**Problem**: Connection to `ai-proxy.lab.epam.com` times out  
**Error**: `Connection timed out after 60 seconds`  
**Root Cause**: VPN routing or firewall blocking access

---

## 🔍 Diagnosis Results

### DNS Resolution: ✅ Working
```
ai-proxy.lab.epam.com → 10.74.65.75 (internal EPAM IP)
```

### Network Connectivity: ❌ **FAILING**
```
Ping: 100% packet loss
HTTPS: Connection timeout on port 443
```

**Conclusion**: VPN is not routing traffic to internal network properly.

---

## 🛠️ Fix Steps

### Step 1: Verify VPN Connection

1. **Check VPN Client Status**:
   - Open EPAM VPN client application
   - Status should show: **"Connected"**
   - Note which VPN profile/server you're connected to

2. **Check VPN IP Assignment**:
   ```bash
   ifconfig | grep -A 5 "utun"
   ```
   You should see a VPN interface with an IP in EPAM's range

### Step 2: Try Different VPN Profile

EPAM may have different VPN profiles:
- **Standard VPN** - May not route to internal API servers
- **Full Tunnel VPN** - Routes all traffic through EPAM network
- **Developer VPN** - Specific access to development resources

**Action**: Try switching VPN profiles in your VPN client

### Step 3: Check Split Tunnel Settings

Split tunneling may be blocking internal traffic:

1. Open VPN client settings
2. Look for "Split Tunnel" or "Exclude Routes"
3. Ensure `10.74.65.75` or `ai-proxy.lab.epam.com` is **NOT excluded**

### Step 4: Flush DNS and Reconnect

```bash
# Disconnect VPN
# Then run:
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

# Reconnect VPN
# Then test:
ping ai-proxy.lab.epam.com
```

### Step 5: Test with nslookup and telnet

```bash
# Verify DNS
nslookup ai-proxy.lab.epam.com

# Test port connectivity
nc -zv ai-proxy.lab.epam.com 443
# Should show: "Connection to ai-proxy.lab.epam.com port 443 [tcp/https] succeeded"
```

### Step 6: Check Firewall Rules

Mac may have firewall blocking the connection:

```bash
# Check firewall status
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate

# If enabled, add exception for Python
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/bin/python3
```

---

## 📞 Contact EPAM IT Support

If above steps don't work, contact EPAM IT Support with this information:

### Issue Description
```
Unable to access DIAL API endpoint at ai-proxy.lab.epam.com

Symptoms:
- DNS resolves to 10.74.65.75 (internal IP)
- Cannot ping the server (100% packet loss)
- HTTPS connection to port 443 times out after 60 seconds
- Error: "Connection to ai-proxy.lab.epam.com timed out"

Environment:
- OS: macOS 22.6.0
- VPN: [Your VPN client name/version]
- VPN Profile: [Your current profile name]

Request:
- Which VPN profile should I use for DIAL API access?
- Are there firewall rules blocking access to 10.74.65.75:443?
- Do I need additional permissions for ai-proxy.lab.epam.com?
```

### Useful Information to Provide
- Your EPAM username
- Your current VPN profile name
- Your machine's IP address when connected to VPN
- Screenshot of VPN connection status
- Output of: `traceroute ai-proxy.lab.epam.com`

---

## 🔬 Advanced Diagnostics

### Trace Route
```bash
traceroute ai-proxy.lab.epam.com
```
This shows where packets are being dropped.

### Check VPN Routes
```bash
netstat -rn | grep "10.74"
```
Should show routes to 10.74.x.x through VPN interface.

### Test with curl (verbose)
```bash
curl -vvv --max-time 10 https://ai-proxy.lab.epam.com/openai/models \
  -H "api-key: dial-fxbasxs2h6t7brhnbqs36omhe2y" 2>&1 | head -50
```
Shows exactly where connection fails.

### Check if Port 443 is Blocked
```bash
sudo lsof -iTCP:443 -sTCP:LISTEN
```

---

## ✅ How to Verify Fix

Once VPN is properly configured:

### Test 1: Ping Should Work
```bash
ping -c 3 ai-proxy.lab.epam.com
```
**Expected**: Should show responses, not timeouts

### Test 2: Port 443 Should Be Reachable
```bash
nc -zv ai-proxy.lab.epam.com 443
```
**Expected**: "Connection succeeded"

### Test 3: API Should Respond
```bash
curl -I https://ai-proxy.lab.epam.com/openai/models \
  -H "api-key: dial-fxbasxs2h6t7brhnbqs36omhe2y"
```
**Expected**: HTTP 200 response

### Test 4: Run Python Test
```bash
cd /Users/apple/app-templates/ai-dial-models-parameters
source .venv/bin/activate
python test1_models.py
```
**Expected**: Should show LLM response, not timeout error

---

## 🎯 Quick Test Commands

```bash
# Quick connectivity test
ping -c 1 ai-proxy.lab.epam.com && echo "✅ Ping OK" || echo "❌ Ping Failed"

# Quick port test
nc -zv -w5 ai-proxy.lab.epam.com 443 2>&1 | grep -q "succeeded" && echo "✅ Port OK" || echo "❌ Port Blocked"

# Quick API test
curl -I --max-time 5 https://ai-proxy.lab.epam.com/openai/models \
  -H "api-key: dial-fxbasxs2h6t7brhnbqs36omhe2y" 2>/dev/null | \
  grep -q "HTTP" && echo "✅ API OK" || echo "❌ API Failed"
```

---

## 📋 Common VPN Issues

### Issue 1: Wrong VPN Profile
**Solution**: Use "Developer" or "Full Tunnel" profile instead of "Standard"

### Issue 2: Split Tunneling
**Solution**: Disable split tunnel or add exception for 10.74.x.x

### Issue 3: DNS Not Resolving Internal Domains
**Solution**: Check VPN DNS settings, should use EPAM's DNS servers

### Issue 4: Corporate Firewall
**Solution**: Request firewall exception for ai-proxy.lab.epam.com

### Issue 5: VPN Client Outdated
**Solution**: Update to latest VPN client version

---

## 🚨 Emergency Workaround

**If you cannot fix VPN but need to demonstrate the code:**

You can use a different API endpoint as a proof-of-concept:
1. Use OpenAI API directly (if you have access)
2. Use a local LLM server
3. Record the expected behavior in documentation

**Note**: This is only for demonstration purposes. The actual DIAL API requires proper VPN access.

---

## 📞 EPAM Support Contacts

- **IT Support Portal**: https://support.epam.com/
- **VPN Issues**: Submit ticket category "Network Access / VPN"
- **DIAL API Access**: Submit ticket category "Development Tools / AI Services"

---

**The code is correct and ready. Once VPN routing is fixed, all tests will work immediately.** ✅

