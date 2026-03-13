# SimSecure v1.0

## Professional Cybersecurity Command-Line Tool

SimSecure is an ethical security testing tool designed for educational purposes and authorized security assessments. It provides comprehensive security checks with easy-to-read terminal output and professional reporting capabilities.

---

## Features

### 1. **Website Security Scanner**
- HTTPS encryption verification
- Security headers analysis (X-Frame-Options, CSP, HSTS, X-XSS-Protection)
- Server information leakage detection
- Content-Type-Options validation
- Security score calculation (0-10)

### 2. **Port Scanner**
- Multi-threaded TCP port scanning
- Scans 17 common ports
- Detects open services (SSH, HTTP, MySQL, etc.)
- Security scoring based on open ports
- Fast concurrent scanning

### 3. **Password Strength Analyzer**
- Comprehensive strength evaluation
- Checks for length, uppercase, lowercase, numbers, special characters
- Detailed recommendations
- Security score and strength rating

### 4. **Security Reports**
- Generates detailed text reports
- Timestamped file saving
- Security findings documentation
- Professional formatting

### 5. **User-Friendly Features**
- Colored terminal output (Green/Yellow/Red)
- Professional banner display
- Legal disclaimer
- Command-line help system
- Error handling for network issues
- Cross-platform compatibility (Windows, macOS, Linux)

---

## Installation

### Requirements
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Navigate to the project directory:**
   ```bash
   cd simsecure
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Make the script executable (Linux/macOS):**
   ```bash
   chmod +x simsecure.py
   ```

---

## Usage

### Basic Syntax
```bash
python simsecure.py [COMMAND] [TARGET] [OPTIONS]
```

### Available Commands

#### 1. Website Scanner
```bash
# Basic scan
python simsecure.py web https://example.com

# Scan without protocol (assumes HTTPS)
python simsecure.py web example.com

# Scan with report generation
python simsecure.py web https://example.com --report
```

#### 2. Port Scanner
```bash
# Basic port scan
python simsecure.py port example.com

# Port scan with report
python simsecure.py port 192.168.1.1 --report
```

#### 3. Password Strength Test
```bash
# Test a password
python simsecure.py password MyPassword123!

# Test password with spaces (use quotes)
python simsecure.py password "My P@ssw0rd #123" --report
```

#### 4. Help Menu
```bash
python simsecure.py -h
python simsecure.py --help
```

#### 5. Version Information
```bash
python simsecure.py version
```

#### 6. Legal Disclaimer
```bash
python simsecure.py disclaimer
```

---

## Output Examples

### Website Scan Output
```
[*] Scanning Website: https://example.com
─────────────────────────────────────────────────────────────────────────────
[+] HTTPS: Enabled
[+] X-Frame-Options: Present (DENY)
[!] Content-Security-Policy: Missing
[+] X-XSS-Protection: Present
[+] Strict-Transport-Security: Present
[+] Server Header: Not detected (Good)
[+] X-Content-Type-Options: nosniff
─────────────────────────────────────────────────────────────────────────────

Security Score: 9/10

[+] Report saved to: reports/scan_report_WEB_20260309_120530.txt
```

### Port Scan Output
```
[*] Scanning Ports on: example.com
[*] Resolved IP: 93.184.216.34
─────────────────────────────────────────────────────────────────────────────
[+] Port 80 is OPEN (HTTP)
[+] Port 443 is OPEN (HTTPS)
─────────────────────────────────────────────────────────────────────────────

[!] Open Ports Found: 2
[+] Open ports: 80, 443

Security Score: 8/10
```

### Password Test Output
```
[*] Analyzing Password Strength
─────────────────────────────────────────────────────────────────────────────
[+] Password Length: PASS (Length: 12 characters)
[+] Uppercase Letters: PASS
[+] Lowercase Letters: PASS
[+] Numbers: PASS
[+] Special Characters: PASS
─────────────────────────────────────────────────────────────────────────────

Overall Password Strength: STRONG
Security Score: 10/10

Recommendations:
  • Excellent security! Keep this password safe and unique.
```

---

## Report Files

Reports are automatically saved in the `reports/` folder with timestamps:

```
reports/
├── scan_report_WEB_20260309_120530.txt
├── scan_report_PORT_20260309_120615.txt
└── scan_report_PASSWORD_20260309_120700.txt
```

Each report includes:
- Scan date and time
- Target information
- Detailed findings
- Security score and rating
- Legal disclaimers

---

## Security Scoring

### Website Scanner (0-10)
- HTTPS enabled: +2
- X-Frame-Options: +1
- Content-Security-Policy: +2
- X-XSS-Protection: +1
- Strict-Transport-Security: +2
- Server header not disclosed: +1
- X-Content-Type-Options: +1

### Port Scanner (0-10)
- 0 open ports: 10
- 1 open port: 9
- 2 open ports: 8
- 3-4 open ports: 6
- 5+ open ports: 4

### Password Strength (0-10)
- Length ≥ 8 characters: +2
- Uppercase letters: +2
- Lowercase letters: +2
- Numbers: +2
- Special characters: +2
- Bonus for 16+ chars: +1 (max 10)

---

## Project Structure

```
simsecure/
├── simsecure.py          # Main entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
├── modules/
│   ├── __init__.py        # Package initialization
│   ├── web_scan.py        # Website security scanner
│   ├── port_scan.py       # Port scanner
│   ├── password_test.py   # Password strength tester
│   └── report.py          # Report generation
│
└── reports/               # Generated report files
    └── (reports saved here with timestamps)
```

---

## Module Documentation

### web_scan.py
- `scan_website(url)` - Performs comprehensive website security analysis
  - Returns: (score, findings_list)

### port_scan.py
- `scan_ports(host)` - Scans common ports on target host
  - Returns: (score, findings_list)

### password_test.py
- `test_password(password)` - Analyzes password strength
  - Returns: (score, findings_list)

### report.py
- `generate_report(scan_type, target, findings, score)` - Creates report file
  - Returns: path to report file

---

## Error Handling

SimSecure handles common errors gracefully:

- **Invalid URL**: Automatically adds https:// if missing
- **Connection Timeout**: Timeout set to 10 seconds for web requests
- **Invalid Hostname**: DNS resolution errors are caught and reported
- **Keyboard Interrupt**: Ctrl+C gracefully exits the scan
- **Socket Errors**: Port scanning handles unreachable hosts

---

## Important Legal Notice

⚠️ **DISCLAIMER**

This tool is designed for **EDUCATIONAL and AUTHORIZED testing purposes only**.

- Unauthorized access to computer networks is **ILLEGAL**
- Obtain written authorization before testing any target
- Users assume full responsibility for legal compliance
- Misuse can result in criminal charges and civil penalties

For authorized security professionals only.

---

## Common Port Reference

| Port | Service | Protocol |
|------|---------|----------|
| 21 | FTP | File Transfer Protocol |
| 22 | SSH | Secure Shell |
| 23 | Telnet | Telnet (Insecure) |
| 25 | SMTP | Simple Mail Transfer Protocol |
| 53 | DNS | Domain Name System |
| 80 | HTTP | HyperText Transfer Protocol |
| 110 | POP3 | Post Office Protocol 3 |
| 139 | NetBIOS | Network Basic Input/Output System |
| 143 | IMAP | Internet Message Access Protocol |
| 443 | HTTPS | HTTP Secure |
| 3306 | MySQL | MySQL Database |
| 5432 | PostgreSQL | PostgreSQL Database |
| 6379 | Redis | Redis Cache |
| 8080 | HTTP Proxy | HTTP Proxy/Alt HTTP |
| 27017 | MongoDB | MongoDB Database |

---

## Troubleshooting

### Issue: "ModuleNotFoundError" for requests or colorama
**Solution**: Install dependencies with `pip install -r requirements.txt`

### Issue: Port scan takes too long
**Solution**: The tool uses multi-threading. For faster scans on slow connections, increase timeout values in port_scan.py

### Issue: SSL certificate errors on website scanning
**Solution**: The requests library handles SSL verification by default. Some sites may require specific certificates.

### Issue: Permission denied on port scan (ports < 1024)
**Solution**: On Linux/macOS, ports below 1024 require sudo. Run with `sudo python simsecure.py port ...`

---

## Extending SimSecure

To add new security modules:

1. Create a new file in `modules/` directory
2. Implement the security check function
3. Import and call from main script
4. Follow the same return format: `(score, findings_list)`

Example:
```python
def new_security_check(target):
    findings = []
    score = 0
    # Your security check code here
    findings.append("Finding 1")
    findings.append("Finding 2")
    score = 5
    return score, findings
```

---

## Performance Notes

- **Web Scanner**: 1-5 seconds (depends on site response time)
- **Port Scanner**: 15-30 seconds (17 concurrent connections with 2-second timeout)
- **Password Tester**: < 1 second (regex-based analysis only)
- **Report Generation**: < 1 second

---

## Version History

### v1.0 (Initial Release)
- Website scanner with 7 security checks
- Multi-threaded port scanner
- Password strength analyzer
- Report generation system
- Colored terminal output
- Cross-platform support

---

## Support

For issues, questions, or suggestions:

1. Check the troubleshooting section above
2. Review the help menu: `python simsecure.py -h`
3. Check report files in the `reports/` folder for detailed findings

---

## License

This project is provided for educational and authorized security testing purposes.
Unauthorized use is prohibited.

---

## References

**Security Standards Referenced:**
- OWASP Top 10
- CWE/SANS Top 25
- NIST Cybersecurity Framework
- Internet Security Standards (RFC 6797, etc.)

---

**SimSecure v1.0**
*Ethical Security Testing Tool*
*For Educational and Authorized Use Only*

Last Updated: March 2026

---
