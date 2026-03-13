# 🔒 SimSecure - Professional Use Guide

## Quick Start (5 Minutes)

### 1. Open Terminal/PowerShell

```bash
# Navigate to SimSecure
cd C:\Programming\RTRP\simsecure

# Or on Linux/macOS
cd /path/to/simsecure
```

### 2. Use the Tool

**Option A: Interactive Menu (Recommended)**
```bash
python simsecure.py
```

**Option B: List Available Commands**
```bash
python simsecure.py -ls
```

**Option C: Run Directly**
```bash
python simsecure.py password "YourPassword123!"
python simsecure.py web https://example.com
python simsecure.py port example.com
```

---

## Professional Usage Examples

### 1. Password Security Test

```bash
$ python simsecure.py password "MyStrongPass#2026" --report

=============================================================================== 
|                        SIMSECURE v1.0                              |        
=============================================================================== 

[*] Analyzing Password Strength
----------------------------------------------------------------------
[+] Password Length: PASS (Length: 17 characters)
[+] Uppercase Letters: PASS
[+] Lowercase Letters: PASS
[+] Numbers: PASS
[+] Special Characters: PASS
----------------------------------------------------------------------

Overall Password Strength: EXCELLENT
Security Score: 10/10

[+] Report saved to: reports/scan_report_PASSWORD_20260309_131923.txt
```

---

### 2. Website Security Scan

```bash
$ python simsecure.py web https://httpbin.org --report

[*] Scanning Website: https://httpbin.org
----------------------------------------------------------------------
[+] HTTPS: Enabled
[!] X-Frame-Options: Missing
[!] Content-Security-Policy: Missing
[!] X-XSS-Protection: Missing
[!] Strict-Transport-Security: Missing
[!] Server Header: gunicorn/19.9.0 (Information leakage)
[!] X-Content-Type-Options: Missing or Incorrect
----------------------------------------------------------------------

Security Score: 2/10
[+] Report saved to: reports/scan_report_WEB_20260309_131948.txt
```

---

### 3. Port Scanner

```bash
$ python simsecure.py port example.com --report

[*] Scanning Ports on: example.com
[*] Resolved IP: 104.18.26.120
----------------------------------------------------------------------
[+] Port 80 is OPEN (HTTP)
[+] Port 443 is OPEN (HTTPS)
[+] Port 8080 is OPEN (HTTP Proxy)
[+] Port 8443 is OPEN (HTTPS Alt)
----------------------------------------------------------------------

[!] Open Ports Found: 4
Open ports: 80, 443, 8080, 8443

Security Score: 6/10
[+] Report saved to: reports/scan_report_PORT_20260309_132001.txt
```

---

## Interactive Menu Mode

Just run:
```bash
python simsecure.py
```

You'll see:
```
=== SIMSECURE SECURITY SCANNER ===

Available Security Checks:

  1) Website Security Scanner
  2) Port Scanner
  3) Password Strength Tester
  4) Help & Examples
  5) Exit

Select an option (1-5): 
```

Then:
1. **Enter "1"** → Scanner asks for website URL
2. **Enter "2"** → Scanner asks for hostname/IP
3. **Enter "3"** → Scanner asks for password
4. **Enter "4"** → Shows detailed help
5. **Enter "5"** → Exit tool

---

## View Security Reports

Reports are saved in `reports/` folder with timestamps:

```bash
# List all reports
dir reports

# View a report
type reports\scan_report_PASSWORD_*.txt

# Or on Linux/macOS
cat reports/scan_report_PASSWORD_*.txt
```

---

## Commands Cheat Sheet

| Task | Command |
|------|---------|
| Show menu | `python simsecure.py` |
| List commands | `python simsecure.py -ls` |
| Show help | `python simsecure.py -h` |
| Test password | `python simsecure.py password "Pass#123"` |
| Scan website | `python simsecure.py web https://example.com` |
| Scan ports | `python simsecure.py port example.com` |
| With report | Add `--report` flag |
| Show version | `python simsecure.py version` |
| Show disclaimer | `python simsecure.py disclaimer` |

---

## Security Score Reference

### Password Strength
```
0-3:   VERY WEAK ❌
4-6:   WEAK ⚠️
7-8:   STRONG ✓
9-10:  EXCELLENT ✅
```

### Website Security
```
0-2:   POOR 🔴 Critical vulnerabilities
3-5:   FAIR 🟡 Multiple issues
6-8:   GOOD 🟢 Most protections in place
9-10:  EXCELLENT 🟢 Optimal security
```

### Port Scanner
```
10:    SECURE 🟢 All ports closed
8-9:   GOOD ✓ 1-2 ports open
6-7:   FAIR ⚠️ 3-4 ports open
4-5:   RISKY 🔴 5+ ports open
```

---

## Real-World Security Audit Workflow

### Audit a Website
```bash
# 1. Check website security
python simsecure.py web https://company.com --report

# 2. Scan for open ports
python simsecure.py port company.com --report

# 3. Review reports
type reports\scan_report_*.txt
```

### Create Team Documentation
```bash
# 1. Test password policies
python simsecure.py password "StandardPass#123" --report
python simsecure.py password "WeakPass123" --report

# 2. Scan target servers
python simsecure.py port server1.company.com --report
python simsecure.py port server2.company.com --report

# 3. Check public websites
python simsecure.py web https://company.com --report
python simsecure.py web https://api.company.com --report

# 4. Collect all reports
cd reports
dir scan_report_*.txt

# Send to management or archive
```

---

## Installation (One-Time Only)

```bash
# Navigate to SimSecure
cd C:\Programming\RTRP\simsecure

# Install as system package
pip install -e .

# Verify installation
python simsecure.py --version
```

---

## Tips for Professional Use

✅ **Always save reports:**
```bash
python simsecure.py [command] [target] --report
```

✅ **Document your findings:**
```bash
# Review generated reports
cat reports/scan_report_20260309_*.txt
```

✅ **Test regularly:**
```bash
# Create a weekly security check
python simsecure.py port company-server.local --report
```

✅ **Use meaningful targets:**
```bash
# Good: specific, authorized targets
python simsecure.py port webapp-server

# Avoid: random, unauthorized targets
```

✅ **Keep old reports:**
```bash
# Reports have timestamps - old ones preserved
# Good for tracking security improvements
```

---

## Common Workflows

### Weekly Security Check
```bash
echo Starting weekly security check...
python simsecure.py password "AdminPass#Current" --report
python simsecure.py web https://internal-portal.local --report
python simsecure.py port db-server.local --report
echo Done! Reports saved in reports/ folder
```

### Penetration Test Preparation
```bash
# Check website security first
python simsecure.py web https://target-domain.com --report

# Scan for exposed ports
python simsecure.py port target-domain.com --report

# Generate documentation
cd reports
echo "Security Assessment Report" > assessment.txt
echo "Generated:" >> assessment.txt
echo "Target: target-domain.com" >> assessment.txt
```

### Compliance Audit
```bash
# Test password complexity
python simsecure.py password "Policy-Required#Pass123" --report

# Verify security headers
python simsecure.py web https://critical-app.local --report

# Check port exposure
python simsecure.py port critical-app-server --report
```

---

## Troubleshooting

### "Command not found"
```bash
# Make sure you're in the right directory
cd C:\Programming\RTRP\simsecure
python simsecure.py -ls
```

### "Connection Error"
```bash
# Check if target is online
# Check if firewall allows connection
# Verify target hostname/IP is correct
```

### "Invalid hostname"
```bash
# Use IP address instead
python simsecure.py port 8.8.8.8

# Or try localhost
python simsecure.py port localhost
```

---

## Important Reminders

⚠️ **Legal Notice:**
- This tool is for **authorized testing only**
- Do NOT scan systems without permission
- Unauthorized access is **ILLEGAL**

🔒 **Security:**
- Don't share security reports publicly
- Store reports in secure location
- Use reports for improvement, not exposure

✅ **Ethics:**
- Document your authorization
- Report vulnerabilities responsibly
- Help improve security, not exploit it

---

## Getting Help

```bash
# Show interactive menu
python simsecure.py

# List available commands
python simsecure.py -ls

# Show help
python simsecure.py -h

# Show legal notice
python simsecure.py disclaimer
```

---

## Next Steps

1. **Run Interactive Mode:**
   ```bash
   python simsecure.py
   ```

2. **List Commands:**
   ```bash
   python simsecure.py -ls
   ```

3. **Test a Password:**
   ```bash
   python simsecure.py password "test123"
   ```

4. **Generate Reports:**
   ```bash
   python simsecure.py password "secure#Pass" --report
   ```

5. **Review Results:**
   ```bash
   type reports\scan_report_*.txt
   ```

---

## Professional Features

✅ Colored output for easy reading
✅ Security scoring system
✅ Timestamped reports
✅ Multi-threaded scanning
✅ Professional formatting
✅ Ethical guidelines
✅ Cross-platform support

---

**You're ready to use SimSecure professionally!** 🚀

Start with: `python simsecure.py`

Or try: `python simsecure.py -ls`
