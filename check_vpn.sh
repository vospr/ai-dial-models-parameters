#!/bin/bash

# VPN Connectivity Diagnostic Script
# Run this to check if your VPN is properly configured for DIAL API access

echo "======================================================================="
echo "DIAL API VPN Connectivity Diagnostic"
echo "======================================================================="
echo ""

ENDPOINT="ai-proxy.lab.epam.com"
API_KEY="dial-fxbasxs2h6t7brhnbqs36omhe2y"

# Test 1: DNS Resolution
echo "Test 1: DNS Resolution"
echo "-----------------------"
DNS_RESULT=$(nslookup $ENDPOINT 2>&1 | grep "Address:" | tail -1 | awk '{print $2}')
if [ ! -z "$DNS_RESULT" ]; then
    echo "✅ DNS resolves to: $DNS_RESULT"
else
    echo "❌ DNS resolution failed"
    echo ""
    echo "Fix: Check your DNS settings or reconnect VPN"
    exit 1
fi
echo ""

# Test 2: Ping Test
echo "Test 2: Network Connectivity (Ping)"
echo "------------------------------------"
ping -c 2 -W 3 $ENDPOINT > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Ping successful"
else
    echo "❌ Ping failed (100% packet loss)"
    echo ""
    echo "This indicates VPN routing issue"
    echo "Fix: Try different VPN profile or contact IT support"
fi
echo ""

# Test 3: Port 443 Connectivity
echo "Test 3: HTTPS Port 443 Connectivity"
echo "-------------------------------------"
nc -z -w 5 $ENDPOINT 443 > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Port 443 is reachable"
else
    echo "❌ Port 443 is blocked or unreachable"
    echo ""
    echo "Fix: Check firewall settings or VPN configuration"
fi
echo ""

# Test 4: API Endpoint Test
echo "Test 4: DIAL API Endpoint"
echo "--------------------------"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 \
    "https://$ENDPOINT/openai/models" \
    -H "api-key: $API_KEY" 2>/dev/null)

if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "401" ] || [ "$HTTP_CODE" = "403" ]; then
    echo "✅ API endpoint is reachable (HTTP $HTTP_CODE)"
    if [ "$HTTP_CODE" = "200" ]; then
        echo "   API is accessible and working!"
    elif [ "$HTTP_CODE" = "401" ]; then
        echo "   API reachable but authentication issue (check API key)"
    elif [ "$HTTP_CODE" = "403" ]; then
        echo "   API reachable but access forbidden (check permissions)"
    fi
elif [ "$HTTP_CODE" = "000" ]; then
    echo "❌ API endpoint unreachable (connection timeout)"
    echo ""
    echo "Fix: VPN is not routing traffic to internal network"
else
    echo "⚠️  API endpoint returned HTTP $HTTP_CODE"
fi
echo ""

# Test 5: Traceroute (first 10 hops)
echo "Test 5: Network Route Trace (first 5 hops)"
echo "--------------------------------------------"
echo "Tracing route to $ENDPOINT..."
traceroute -m 5 -w 2 $ENDPOINT 2>/dev/null | head -6
echo ""

# Summary
echo "======================================================================="
echo "DIAGNOSTIC SUMMARY"
echo "======================================================================="
echo ""

# Check if all critical tests passed
if [ ! -z "$DNS_RESULT" ] && nc -z -w 5 $ENDPOINT 443 > /dev/null 2>&1; then
    echo "✅ VPN appears to be working correctly!"
    echo ""
    echo "You can now run the tests:"
    echo "  cd /mnt/c/Users/AndreyPopov/ai-dial-models-parameters"
    echo "  source .venv/bin/activate"
    echo "  python test1_models.py"
else
    echo "❌ VPN connectivity issues detected"
    echo ""
    echo "RECOMMENDED ACTIONS:"
    echo "1. Disconnect and reconnect VPN"
    echo "2. Try a different VPN profile (Developer/Full Tunnel)"
    echo "3. Check VPN split tunnel settings"
    echo "4. Contact EPAM IT Support"
    echo ""
    echo "See VPN_TROUBLESHOOTING.md for detailed fix steps"
fi
echo ""
echo "======================================================================="

