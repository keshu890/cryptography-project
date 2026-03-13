# SimSecure - Installation and Usage Complete Guide

## What is SimSecure?

SimSecure is a **professional cybersecurity command-line tool** for ethical security testing. Like Nmap, it can be installed as a system-wide command and used from anywhere.

**Key Features:**
- ✅ Website Security Scanner
- ✅ Port Scanner  
- ✅ Password Strength Tester
- ✅ Security Reports (with timestamps)
- ✅ Interactive Menu Mode
- ✅ Command-Line Interface
- ✅ Professional Output (colored)

---

## Installation

### Step 1: Install SimSecure

Navigate to the SimSecure directory and install:

```bash
# Windows - Command Prompt or PowerShell
cd C:\Programming\RTRP\simsecure
pip install -e .

# Linux/macOS - Terminal
cd /path/to/simsecure
sudo pip install -e .
# OR (user-only installation, no sudo)
pip install -e .
```

### Step 2: Verify Installation

```bash
# Check if simsecure command works
simsecure --version

# Should output: SimSecure v1.0
```

**If command not found:**
```bash
# Try with python module directly
python -m simsecure.simsecure --version

# Or use full path
python C:\Programming\RTRP\simsecure\simsecure.py -ls
```

---

## Usage After Installation

### Option 1: Interactive Menu (Easiest)

Simply run simsecure with no arguments:

```bash
simsecure
```

Output:
```
=== SIMSECURE SECURITY SCANNER ===

Available Security Checks:

  1) Website Security Scanner
     - Check HTTPS, security headers, vulnerabilities

  2) Port Scanner
     - Scan open ports on target host

  3) Password Strength Tester
     - Analyze password security strength

  4) Help & Examples
     - Display detailed help information

  5) Exit

Select an option (1-5):
```

**Then:**
1. Enter your choice (1-5)
2. System prompts for target/password
3. Choose to save report (y/n)
4. View results
5. Repeat or exit

---

### Option 2: List Available Commands

```bash
simsecure -ls
```

Output:
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

Add --report flag to generate security reports
```

---

### Option 3: Command-Line Mode

#### Check Password Strength
```bash
# Quick test
simsecure password "MyPassword123!"

# Save report
simsecure password "MyPassword123!" --report
```

Output includes:
- Length check
- Uppercase/lowercase letters
- Numbers and special characters
- Security score (0-10)
- Recommendations

---

#### Scan Website Security
```bash
# Quick scan
simsecure web https://example.com

# Save report
simsecure web https://example.com --report
```

Checks:
- HTTPS enabled
- Security headers (CSP, X-Frame-Options, HSTS)
- XSS protection
- Server information leakage
- Content-Type validation

---

#### Scan for Open Ports
```bash
# Quick scan
simsecure port example.com

# Save report
simsecure port example.com --report
```

Scans for open ports and identifies services:
- SSH (22)
- HTTP (80)
- HTTPS (443)
- MySQL (3306)
- And 13 more ports

---

## Security Scoring

### Password Strength (0-10)
```
6 = WEAK           - Add more requirements
8 = STRONG         - Good security
10 = EXCELLENT     - Optimal password
```

**Password must have:**
- ✓ 8+ characters
- ✓ Uppercase letters
- ✓ Lowercase letters
- ✓ Numbers
- ✓ Special characters

---

### Website Security (0-10)
```
10 = Excellent     - All security headers present
8 = Good           - Most headers present
5 = Fair           - Some headers missing
0 = Poor           - Multiple vulnerabilities
```

**Checks:**
- HTTPS encryption
- CSP (Content Security Policy)
- X-Frame-Options
- X-XSS-Protection
- Strict-Transport-Security
- Server information

---

### Port Scanner (0-10)
```
10 = Secure        - All ports closed
8 = Good           - 1-2 ports open
6 = Fair           - 3-4 ports open
4 = Vulnerable     - 5+ ports open
```

---

## Real-World Examples

### Example 1: Test Your Password

```bash
$ simsecure password "MySecure#Pass2026" --report

[*] Analyzing Password Strength
----------------------------------------------------------------------
[+] Password Length: PASS (20 characters)
[+] Uppercase Letters: PASS
[+] Lowercase Letters: PASS
[+] Numbers: PASS
[+] Special Characters: PASS
[+] BONUS: Very Strong Length (16+ characters)
----------------------------------------------------------------------

Overall Password Strength: EXCELLENT
Security Score: 10/10

[+] Report saved to: reports/scan_report_PASSWORD_20260309_131851.txt
```

---

### Example 2: Check Website Security

```bash
$ simsecure web https://httpbin.org --report

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

[+] Report saved to: reports/scan_report_WEB_20260309_120530.txt
```

---

### Example 3: Scan Server Ports

```bash
$ simsecure port example.com

[*] Scanning Ports on: example.com
[*] Resolved IP: 104.18.26.120
----------------------------------------------------------------------
[+] Port 80 is OPEN (HTTP)
[+] Port 443 is OPEN (HTTPS)
[+] Port 8080 is OPEN (HTTP Proxy)
[+] Port 8443 is OPEN (HTTPS Alt)
----------------------------------------------------------------------

Open Ports Found: 4
Open ports: 80, 443, 8080, 8443

Security Score: 6/10
```

---

## Reports

Reports are automatically saved when using `--report` flag:

```
reports/
├── scan_report_PASSWORD_20260309_131851.txt
├── scan_report_WEB_20260309_120530.txt
└── scan_report_PORT_20260309_120615.txt
```

### View Reports

```bash
# Windows
type reports\scan_report_*.txt

# Linux/macOS
cat reports/scan_report_*.txt
```

### Report Contents
- Scan date and time
- Target information
- Detailed findings
- Security score
- Rating (Excellent/Good/Fair/Poor)
- Legal disclaimer

---

## All Commands Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `simsecure` | Interactive menu | `simsecure` |
| `simsecure -ls` | List all commands | `simsecure -ls` |
| `-h` or `--help` | Show help | `simsecure -h` |
| `web [URL]` | Scan website | `simsecure web https://example.com` |
| `port [HOST]` | Scan ports | `simsecure port example.com` |
| `password [PASS]` | Test password | `simsecure password "Pass#123"` |
| `--report` | Save report | `simsecure password "Pass" --report` |
| `version` | Show version | `simsecure version` |
| `disclaimer` | Show legal info | `simsecure disclaimer` |

---

## Troubleshooting

### Problem: "simsecure command not found"

**Solution 1: Reinstall**
```bash
cd C:\Programming\RTRP\simsecure
pip install -e .
```

**Solution 2: Use Python directly**
```bash
python C:\Programming\RTRP\simsecure\simsecure.py -ls
```

**Solution 3: Check PATH**
```bash
python -m pip show simsecure
```

---

### Problem: "Connection Error" during web scan

**Causes:**
- Internet connection down
- Target website is offline
- Firewall blocking request

**Solution:**
```bash
# Try with different URL
simsecure web https://httpbin.org

# Check internet connection
ping google.com
```

---

### Problem: "Invalid hostname" during port scan

**Solution:**
```bash
# Use IP address instead
simsecure port 8.8.8.8

# Or check hostname is correct
simsecure port localhost
```

---

### Problem: Port scanning takes too long

**Note:** This is normal - tool scans 17 ports concurrently (30 seconds typical)

**To speed up:**
```bash
# Scan just happens in background
# Be patient and wait for results
simsecure port example.com
```

---

## Advanced Usage

### Run from Any Directory

Once installed, use from anywhere:

```bash
# From home directory
cd ~
simsecure web https://example.com

# From Desktop
cd Desktop
simsecure port example.com

# From any location
simsecure password "test123"
```

---

### Save Multiple Reports

```bash
# Test and document security
simsecure password "Pass#123" --report
simsecure web https://mysite.com --report
simsecure port myserver.com --report

# All reports saved with timestamps
cd reports
dir
```

---

### Using in Scripts

```bash
# Script to run security audit
#!/bin/bash

echo "Running Security Audit..."
simsecure password "AdminPass#2026" --report
simsecure web https://company.com --report
simsecure port company-server.local --report

echo "Reports saved in the reports/ folder"
```

---

## Uninstall

To remove SimSecure:

```bash
pip uninstall simsecure
```

---

## Important Notes

⚠️ **Legal Disclaimer:**
- This tool is for **educational and authorized testing only**
- Do **NOT** use on systems you don't own without written permission
- Unauthorized access is **ILLEGAL**
- User assumes full responsibility for use

🔒 **Security Best Practices:**
- Keep strong passwords safe
- Don't share security reports
- Use `--report` for security documentation
- Only test systems you have authorization for

---

## Getting Help

```bash
# Show interactive menu
simsecure

# List all commands
simsecure -ls

# Show help
simsecure -h

# Show legal notice
simsecure disclaimer
```

---

## Next Steps

1. **Install:** `pip install -e C:\Programming\RTRP\simsecure`
2. **Verify:** `simsecure --version`
3. **Explore:** `simsecure -ls`
4. **Try:** `simsecure password "test123"`
5. **Report:** Save findings with `--report`

---

## Summary

SimSecure is now installed and ready to use!

- ✅ Works like professional security tools (Nmap, etc.)
- ✅ Can be used from anywhere after installation
- ✅ Interactive menu for easy use
- ✅ Command-line for automation
- ✅ Professional security reports
- ✅ Cross-platform (Windows, Linux, macOS)

**Start using it:**
```bash
simsecure -ls
# Or
simsecure
```

---

**SimSecure v1.0 - Professional Cybersecurity Command-Line Tool** 🔒
