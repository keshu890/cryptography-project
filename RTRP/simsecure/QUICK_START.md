# SimSecure Quick Start Guide

## Installation (One-Time Setup)

```bash
# Navigate to SimSecure directory
cd C:\Programming\RTRP\simsecure

# Install the tool
pip install -e .

# Verify installation
simsecure --version
```

---

## After Installation - Use from Anywhere

Once installed, you can use `simsecure` from any directory:

### 1. Show Available Commands
```bash
simsecure -ls
```

**Output:**
```
=== AVAILABLE SECURITY CHECKS ===

1. Website Security Scanner
   - Checks HTTPS, security headers, CSP, XSS protection
   - Usage: simsecure web https://example.com [--report]

2. Port Scanner
   - Scans 17 common ports for open services
   - Usage: simsecure port example.com [--report]

3. Password Strength Tester
   - Analyzes password security strength (0-10 score)
   - Usage: simsecure password "YourPassword" [--report]
```

---

### 2. Interactive Menu Mode (Recommended for Beginners)

Simply run without any arguments:

```bash
simsecure
```

This opens an interactive menu where you can:
1. Select "1" for Website Security Scanner
2. Select "2" for Port Scanner
3. Select "3" for Password Strength Tester
4. Select "4" for Help
5. Select "5" to Exit

Menu will prompt you for:
- Target URL/Hostname/Password
- Whether to save report

---

### 3. Command-Line Mode

#### Test Password Strength
```bash
# Quick test
simsecure password "MyPassword123!"

# Test and save report
simsecure password "SuperSecure#Pass2026" --report
```

**Example Output:**
```
[*] Analyzing Password Strength
----------------------------------------------------------------------
[+] Password Length: PASS (Length: 20 characters)
[+] Uppercase Letters: PASS
[+] Lowercase Letters: PASS
[+] Numbers: PASS
[+] Special Characters: PASS
[+] BONUS: Very Strong Length (16+ characters)
----------------------------------------------------------------------

Overall Password Strength: EXCELLENT
Security Score: 10/10
```

---

#### Scan Website for Security Issues
```bash
# Quick scan
simsecure web https://example.com

# Scan without protocol (auto adds https)
simsecure web example.com

# Scan and save report
simsecure web https://example.com --report
```

**Example Output:**
```
[*] Scanning Website: https://example.com
----------------------------------------------------------------------
[+] HTTPS: Enabled
[+] X-Frame-Options: Present
[! ] Content-Security-Policy: Missing
[+] X-XSS-Protection: Present
----------------------------------------------------------------------

Security Score: 7/10
[+] Report saved to: reports/scan_report_WEB_20260309_120530.txt
```

---

#### Scan Ports on Target
```bash
# Scan hostname
simsecure port example.com

# Scan IP address
simsecure port 192.168.1.1

# Scan and save report
simsecure port example.com --report
```

**Example Output:**
```
[*] Scanning Ports on: example.com
[*] Resolved IP: 104.18.26.120
----------------------------------------------------------------------
[+] Port 80 is OPEN (HTTP)
[+] Port 443 is OPEN (HTTPS)
----------------------------------------------------------------------

Open Ports Found: 2
Open ports: 80, 443

Security Score: 8/10
[+] Report saved to: reports/scan_report_PORT_20260309_120615.txt
```

---

## Security Scores Explained

### Password Strength (0-10)
```
Score 0-3:   VERY WEAK - Too short, missing requirements
Score 4-6:   WEAK - Needs more complexity
Score 7-8:   STRONG - Good security
Score 9-10:  EXCELLENT - Optimal security
```

**Requirements (2 points each):**
- ✓ Length ≥ 8 characters
- ✓ Uppercase letters (A-Z)
- ✓ Lowercase letters (a-z)
- ✓ Numbers (0-9)
- ✓ Special characters (!@#$%^&*)

### Port Scanner (0-10)
```
Score 10:  All ports closed (SECURE)
Score 9:   1 port open
Score 8:   2 ports open
Score 6:   3-4 ports open
Score 4:   5+ ports open (VULNERABLE)
```

### Website Security (0-10)
```
Score 9-10: Excellent - Most headers present
Score 7-8:  Good - Some headers missing
Score 5-6:  Fair - Multiple issues
Score 0-4:  Poor - Critical vulnerabilities
```

---

## Report Files

All reports are saved with timestamps:

```
reports/
├── scan_report_PASSWORD_20260309_121810.txt
├── scan_report_WEB_20260309_120530.txt
└── scan_report_PORT_20260309_120615.txt
```

### View a Report
```bash
# Windows
type reports\scan_report_PASSWORD_*.txt

# Linux/macOS
cat reports/scan_report_PASSWORD_*.txt
```

---

## Common Tasks

### Task 1: Check if Your Password is Secure
```bash
simsecure password "YourPassword123!" --report
```

---

### Task 2: Check Website for Security Issues
```bash
simsecure web https://yourwebsite.com --report
```

---

### Task 3: Scan a Server for Open Ports
```bash
simsecure port yourserver.com --report
```

---

### Task 4: Full Security Audit (Save All Reports)
```bash
simsecure password "P@ss#123" --report
simsecure web https://example.com --report
simsecure port example.com --report
```

---

## Troubleshooting

### "simsecure: command not found"
```bash
# Reinstall the tool
pip install -e C:\Programming\RTRP\simsecure

# Or use python directly
cd C:\Programming\RTRP\simsecure
python simsecure.py password "test"
```

### "Connection Error" during web scan
- Check your internet connection
- Website might be down
- Firewall might be blocking requests

### "Invalid hostname" during port scan
```bash
# Make sure hostname is valid
simsecure port 8.8.8.8  # Use IP instead
```

---

## Getting Help

```bash
# Show all commands
simsecure -ls

# Show detailed help
simsecure -h

# Show legal disclaimer
simsecure disclaimer

# Interactive help
simsecure
# Select option 4
```

---

## Advanced Usage

### Using Environment Variables (Optional)
```bash
# Save target to variable
set TARGET=example.com

# Use in command
simsecure port %TARGET% --report
```

---

## Tips & Tricks

✅ **Always use quotes for passwords with spaces:**
```bash
simsecure password "My Pass #123"
```

✅ **Use --report to save findings:**
```bash
simsecure web https://example.com --report
```

✅ **Port scanning takes time (30 seconds):**
```bash
# Be patient - scanning 17 ports concurrently
simsecure port example.com
```

✅ **Check localhost services:**
```bash
simsecure port localhost
simsecure port 127.0.0.1
```

---

## Next Steps

1. ✅ Install SimSecure
2. ✅ Run `simsecure -ls` to see available options
3. ✅ Try interactive mode: `simsecure`
4. ✅ Test a password: `simsecure password "test123"`
5. ✅ Scan a website: `simsecure web https://httpbin.org`
6. ✅ Check reports: `reports/scan_report_*.txt`

---

## Important Notes

⚠️ **Legal Notice:**
- This tool is for educational and authorized testing only
- Obtain permission before scanning systems you don't own
- Unauthorized access is illegal

🔒 **Security:**
- Keep your passwords safe
- Don't share reports containing sensitive data
- Use --report for documentation

---

**Ready to go! Start with `simsecure -ls` or `simsecure` for interactive mode.** 🚀
