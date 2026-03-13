# SimSecure - Complete Detailed Summary

---

## TABLE OF CONTENTS

1. [Project Overview](#project-overview)
2. [Installation Instructions](#installation-instructions)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Core Features](#core-features)
6. [Module-by-Module Breakdown](#module-by-module-breakdown)
7. [Security Scoring System](#security-scoring-system)
8. [How to Use - Step by Step](#how-to-use---step-by-step)
9. [Example Commands](#example-commands)
10. [File Structure Details](#file-structure-details)
11. [Troubleshooting Guide](#troubleshooting-guide)
12. [Frequently Asked Questions](#frequently-asked-questions)

---

## PROJECT OVERVIEW

### What is SimSecure?

SimSecure is a **professional-grade cybersecurity command-line tool** written in Python 3 that performs automated security assessments on websites, systems, and passwords. It works like industry-standard tools such as Nmap, providing ethical security checks and generating security scores on a 0-10 scale.

### Primary Purpose

SimSecure enables security professionals and system administrators to:
- Scan websites for missing security headers and misconfigurations
- Detect open network ports and identify services
- Analyze password strength and provide recommendations
- Generate professional security reports
- Automate security assessments
- Evaluate security posture with standardized scoring

### Key Characteristics

- **Language**: Python 3.11+
- **Execution**: Command-line interface (CLI)
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Global Installation**: Can be installed globally to work from any directory
- **Multi-threaded**: Uses threading for efficient port scanning
- **Colored Output**: Professional colored terminal output for better readability
- **Report Generation**: Creates timestamped security reports
- **Interactive Mode**: User-friendly menu-driven interface
- **License**: Open source for educational and professional use

### Target Users

- Security professionals
- System administrators
- DevSecOps engineers
- Students learning cybersecurity
- Compliance auditors
- IT technicians

---

## INSTALLATION INSTRUCTIONS

### Step 1: Prerequisites

Before installing SimSecure, ensure you have:

1. **Python 3.7 or higher** installed on your system
   - Check version: `python --version`
   - Download from: https://www.python.org/

2. **pip** (Python package manager) installed
   - Typically included with Python
   - Check: `pip --version`

3. **Required Python Libraries**:
   - requests (for HTTP requests)
   - colorama (for colored terminal output)

### Step 2: Local Installation (Development/Testing)

Navigate to the SimSecure directory and install in editable mode:

```bash
# Navigate to project directory
cd C:\Programming\RTRP\simsecure

# Install with pip in editable mode
pip install -e .

# Verify installation
python simsecure.py -h
```

### Step 3: Install Required Dependencies

The tool requires two external Python libraries:

```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install individually
pip install requests>=2.25.0
pip install colorama>=0.4.3
```

### Step 4: Global Installation (Windows)

To make `simsecure` accessible from any directory on Windows:

#### Method 1: Automated Installation (Recommended)

1. **Open Command Prompt as Administrator**:
   - Press `Windows Key + X`
   - Select "Command Prompt (Admin)" or "PowerShell (Admin)"
   - Windows will ask for permission - click "Yes"

2. **Navigate to SimSecure folder**:
   ```powershell
   cd C:\Programming\RTRP\simsecure
   ```

3. **Run the installer**:
   ```powershell
   install_global.bat
   ```

4. **Verify installation**:
   ```powershell
   simsecure -ls
   ```
   
   If successful, you'll see the list of available security checks.

#### Method 2: Manual Installation

1. Open the simsecure folder: `C:\Programming\RTRP\simsecure`
2. Find the file: `simsecure.bat`
3. Copy this file
4. Navigate to: `C:\Windows\System32\`
5. Paste the file there
6. Open a new Command Prompt and test: `simsecure -ls`

### Step 5: Global Installation (Linux/macOS)

To make `simsecure` accessible from any directory on Unix-like systems:

1. **Copy the script**:
   ```bash
   sudo cp /path/to/simsecure /usr/local/bin/simsecure
   ```

2. **Make it executable**:
   ```bash
   sudo chmod +x /usr/local/bin/simsecure
   ```

3. **Edit the configuration** (open the copied file):
   ```bash
   sudo nano /usr/local/bin/simsecure
   ```
   
   Find the line: `SIMSECURE_PATH="/path/to/simsecure.py"`
   
   Replace with actual path to simsecure.py (e.g., `/home/user/Programming/RTRP/simsecure/simsecure.py`)

4. **Save and exit** (Ctrl+O, Enter, Ctrl+X)

5. **Verify installation**:
   ```bash
   simsecure -ls
   ```

---

## TECHNOLOGY STACK

### Core Technologies

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.11+ | Primary programming language |
| requests | 2.25.0+ | HTTP requests for website scanning |
| colorama | 0.4.3+ | Cross-platform colored terminal output |
| socket | Built-in | TCP port communication |
| threading | Built-in | Multi-threaded concurrent operations |
| argparse | Built-in | Command-line argument parsing |
| re | Built-in | Regular expressions for pattern matching |
| datetime | Built-in | Timestamp generation and formatting |

### Why These Libraries?

- **requests**: Handles HTTP/HTTPS connections safely and provides response headers analysis
- **colorama**: Ensures colored output works consistently on Windows, Linux, and macOS
- **socket**: Low-level TCP connections for port scanning accuracy
- **threading**: Allows checking multiple ports in parallel for speed
- **argparse**: Professional CLI argument parsing with help documentation
- **re**: Pattern matching for password validation rules

### Platform Support

- **Windows 10/11**: Full support with batch file wrapper
- **Linux (Ubuntu, Debian, CentOS)**: Full support with shell script
- **macOS**: Full support with shell script
- **Python 3.7+**: Compatible with all versions (tested on 3.11)

---

## PROJECT STRUCTURE

### Root Directory Organization

```
C:\Programming\RTRP\simsecure\
├── simsecure.py                      # Main entry point and CLI orchestrator
├── setup.py                          # Package configuration for pip
├── requirements.txt                  # Python dependencies list
├── simsecure.bat                     # Windows global command wrapper
├── simsecure                         # Linux/macOS global command wrapper
├── install_global.bat                # Windows global installation script
│
├── modules/                          # Core functionality modules
│   ├── __init__.py                  # Package initialization
│   ├── web_scan.py                  # Website security scanner
│   ├── port_scan.py                 # Network port scanner
│   ├── password_test.py             # Password strength analyzer
│   └── report.py                    # Report generation engine
│
├── reports/                          # Generated security reports (auto-created)
│   └── scan_report_*.txt            # Report files with timestamps
│
├── simsecure.egg-info/              # pip package metadata
│
└── Documentation/
    ├── README.md                     # Quick start guide
    ├── SETUP_GLOBAL.md              # Global installation guide
    ├── QUICK_START.md               # Quick start examples
    ├── INSTALL.md                   # Installation details
    ├── HOW_TO_USE.md                # Usage instructions
    ├── INSTALL_AND_USE.md           # Combined guide
    ├── GLOBAL_INSTALL.md            # Global install details
    ├── GLOBAL_SETUP_COMPLETE.md     # Setup completion guide
    └── PROJECT_SUMMARY.md           # Project overview
```

### Directory Details

**Root Folder**: Contains all main executable files and configuration.

**modules/**: Contains the four core Python modules:
- Each module handles one specific security check function
- All modules work independently but are orchestrated by simsecure.py
- Data is passed between modules using tuples: (security_score, findings_list)

**reports/**: Auto-created when first report is generated:
- Stores all generated security assessment reports
- File naming: `scan_report_[TYPE]_[TIMESTAMP].txt`
- Example: `scan_report_web_2026-03-09_14-23-45.txt`

**Documentation/**: Nine comprehensive markdown files explaining every aspect of the tool.

---

## CORE FEATURES

### Feature 1: Website Security Scanner

**Purpose**: Analyzes websites for security vulnerabilities and misconfigurations.

**What It Does**:
- Connects to a website via HTTPS (when available)
- Checks for 7 critical security headers
- Identifies missing security configurations
- Detects information leakage (server header)
- Provides security score (0-10)
- Lists specific findings and recommendations

**Security Headers Checked**:
1. HTTPS Protocol Enabled
2. X-Frame-Options (prevents clickjacking)
3. Content-Security-Policy (protects against XSS)
4. X-XSS-Protection (legacy XSS protection)
5. Strict-Transport-Security (HSTS - forces HTTPS)
6. X-Content-Type-Options (prevents MIME sniffing)
7. Server Header (information leakage check)

**Usage**:
```bash
simsecure web https://example.com
```

---

### Feature 2: Port Scanner

**Purpose**: Identifies open network ports and potential services on a target host.

**What It Does**:
- Connects to a target host (domain or IP address)
- Scans 17 common and critical ports concurrently
- Identifies which ports are open, closed, or unreachable
- Maps ports to common services
- Provides security score based on port count
- Uses multi-threading for fast scanning

**Ports Scanned**:

| Port | Service | Purpose |
|------|---------|---------|
| 21 | FTP | File Transfer Protocol |
| 22 | SSH | Secure Shell (remote access) |
| 23 | Telnet | Unencrypted remote access |
| 25 | SMTP | Email sending |
| 53 | DNS | Domain name resolution |
| 80 | HTTP | Web traffic (unencrypted) |
| 110 | POP3 | Email retrieval |
| 139 | NetBIOS | Windows file sharing |
| 143 | IMAP | Email retrieval |
| 443 | HTTPS | Web traffic (encrypted) |
| 3306 | MySQL | Database |
| 5432 | PostgreSQL | Database |
| 5984 | CouchDB | NoSQL database |
| 6379 | Redis | Cache/session storage |
| 8080 | HTTP Proxy | Alternative HTTP port |
| 27017 | MongoDB | NoSQL database |
| 8443 | HTTPS Alt | Alternative HTTPS port |

**Usage**:
```bash
simsecure port example.com
```

---

### Feature 3: Password Strength Tester

**Purpose**: Analyzes password strength and provides recommendations for improvement.

**What It Does**:
- Validates password against 5 security criteria
- Calculates security score (0-10)
- Identifies missing requirements
- Provides specific improvement recommendations
- Detects common weakness patterns
- Awards bonus points for extra length

**Validation Criteria**:

| Criteria | Requirement | Points |
|----------|-------------|--------|
| Length | 8 characters minimum | +2 |
| Uppercase | At least 1 uppercase letter (A-Z) | +2 |
| Lowercase | At least 1 lowercase letter (a-z) | +2 |
| Numbers | At least 1 digit (0-9) | +2 |
| Special Chars | At least 1 special character (!@#$%^&*) | +2 |
| Bonus | 16+ characters (bonus point) | +1 |

**Scoring**:
- 0-3 points: VERY WEAK
- 4-5 points: WEAK
- 6-7 points: MODERATE
- 8-9 points: STRONG
- 10+ points: EXCELLENT

**Usage**:
```bash
simsecure password "MyPassword123!"
```

---

### Feature 4: Report Generation

**Purpose**: Creates professional security assessment reports with timestamps.

**What It Does**:
- Automatically generates timestamped report files
- Includes scan details and findings
- Adds security score and recommendations
- Includes legal disclaimer
- Stores in dedicated reports/ folder
- Supports all scanner types

**Report Contents**:
```
- SimSecure Banner
- Scan Type (Website/Port/Password)
- Target Information
- Scan Timestamp
- All Findings (bulleted list)
- Security Score
- Security Rating
- Legal Disclaimer
```

**Report Naming Convention**:
- Format: `scan_report_[TYPE]_[TIMESTAMP].txt`
- Example: `scan_report_web_2026-03-09_14-23-45.txt`
- Storage: `C:\Programming\RTRP\simsecure\reports\`

**Usage** (add --report flag to any command):
```bash
simsecure web https://example.com --report
```

---

### Feature 5: Interactive Menu Mode

**Purpose**: Provides user-friendly menu-driven interface for non-CLI users.

**How It Works**:
1. Run tool with no arguments: `simsecure`
2. Select option from interactive menu (1-5)
3. Enter target information when prompted
4. View security score and findings
5. Option to save report
6. Option to scan another target or exit

**Menu Options**:
```
1. Website Security Scanner
2. Port Scanner
3. Password Strength Tester
4. View Help
5. Exit
```

**Usage**:
```bash
simsecure
# Then follow on-screen prompts
```

---

### Feature 6: List Available Checks

**Purpose**: Shows all available security checks and tool capabilities.

**What It Shows**:
- All 3 security scanner types
- Report generation capability
- Basic usage information

**Usage**:
```bash
simsecure -ls
# or
simsecure --list
```

---

## MODULE-BY-MODULE BREAKDOWN

### Module 1: web_scan.py (~6 KB)

**Location**: `C:\Programming\RTRP\simsecure\modules\web_scan.py`

**Purpose**: Website security analysis and HTTP header inspection.

**Main Function**: `scan_website(url)`

**Input Parameters**:
- `url` (string): Complete website URL (e.g., "https://example.com")

**Output Format**:
- Returns tuple: `(security_score, findings_list)`
- security_score: Integer 0-10
- findings_list: List of strings describing each finding

**Security Checks Performed**:

1. **HTTPS Protocol Check**
   - Verifies connection uses HTTPS (encrypted)
   - Action: If HTTPS missing, recommends immediate upgrade
   - Impact: Critical for data protection

2. **X-Frame-Options Header**
   - Prevents clickjacking attacks
   - Recommended value: "DENY" or "SAMEORIGIN"
   - Impact: Protects against UI redressing

3. **Content-Security-Policy (CSP)**
   - Restricts resource loading (scripts, styles, etc.)
   - Prevents XSS attacks
   - Recommended: Strict policy with specific sources

4. **X-XSS-Protection Header**
   - Legacy XSS protection mechanism
   - Modern alternative: Strong CSP policy
   - Recommended value: "1; mode=block"

5. **Strict-Transport-Security (HSTS)**
   - Forces HTTPS for all future connections
   - Recommended: max-age=31536000 (1 year)
   - Impact: Prevents downgrade attacks

6. **X-Content-Type-Options Header**
   - Prevents MIME type sniffing
   - Recommended value: "nosniff"
   - Impact: Stops browser from misinterpreting content

7. **Server Header Leakage**
   - Checks if server reveals software information
   - Risk: Helps attackers identify exploitable versions
   - Recommendation: Hide or use generic value

**Error Handling**:
- Connection timeouts (5 seconds)
- Invalid URLs
- DNS resolution failures
- SSL certificate errors
- Network connectivity issues

**Example Usage**:
```python
from modules.web_scan import scan_website

score, findings = scan_website("https://httpbin.org")
print(f"Score: {score}/10")
for finding in findings:
    print(f"  - {finding}")
```

**Expected Output Example**:
```
Score: 2/10
  - ✓ HTTPS is enabled
  - ✗ X-Frame-Options header is missing
  - ✗ Content-Security-Policy header is missing
  - ✗ X-XSS-Protection header is missing
  - ✗ Strict-Transport-Security header is missing
  - ✗ X-Content-Type-Options header is missing
  - ✗ Server header is exposed: gunicorn/19.9.0
```

---

### Module 2: port_scan.py (~4.6 KB)

**Location**: `C:\Programming\RTRP\simsecure\modules\port_scan.py`

**Purpose**: Network port scanning and service detection using multi-threading.

**Main Functions**:

#### Function 1: `check_port(host, port)`
- Checks single port availability
- Timeouts after 2 seconds
- Used internally by scan_ports()

#### Function 2: `scan_ports(host)`
- Main scanning function
- Scans all 17 predefined ports concurrently
- Returns combined results

**Input Parameters**:
- `host` (string): Domain name or IP address

**Output Format**:
- Returns tuple: `(security_score, findings_list)`
- security_score: Integer 0-10
- findings_list: List of open ports with services

**Scanning Process**:

1. **Target Resolution**: Converts domain to IP if needed
2. **Multi-threaded Connection**: Spawns 17 concurrent threads
3. **Timeout Management**: 2-second timeout per port
4. **Result Collection**: Gathers all results
5. **Score Calculation**: Based on open port count
6. **Report Generation**: Lists all open ports with services

**Security Scoring Logic**:

| Open Ports | Score | Risk Level |
|-----------|-------|-----------|
| 0 ports | 10 | Excellent |
| 1 port | 9 | Very Good |
| 2 ports | 8 | Good |
| 3-4 ports | 6 | Fair |
| 5+ ports | 4 | Poor |

**Port Risk Assessment**:

**High Risk Ports** (immediate concern):
- Port 23 (Telnet) - Unencrypted, no longer recommended
- Port 139 (NetBIOS) - Windows file sharing vulnerability risk
- Port 21 (FTP) - Unencrypted file transfer

**Medium Risk Ports** (should be restricted):
- Port 25 (SMTP) - Can allow spam relay
- Port 3306 (MySQL) - Direct database access dangerous
- Port 5432 (PostgreSQL) - Direct database access dangerous
- Port 27017 (MongoDB) - Typically should not be exposed

**Low Risk Ports** (usually acceptable):
- Port 22 (SSH) - If properly configured
- Port 80 (HTTP) - Expected for web servers
- Port 443 (HTTPS) - Expected for web servers
- Port 53 (DNS) - If intentional

**Error Handling**:
- Network unreachability
- Host not found (DNS failure)
- Connection refused
- Timeout conditions

**Example Usage**:
```python
from modules.port_scan import scan_ports

score, findings = scan_ports("example.com")
print(f"Score: {score}/10")
for finding in findings:
    print(f"  - {finding}")
```

**Expected Output Example**:
```
Score: 6/10
  - Port 80 is open (HTTP)
  - Port 443 is open (HTTPS)
  - Port 8080 is open (HTTP Proxy)
  - Port 8443 is open (HTTPS Alt)
```

---

### Module 3: password_test.py (~4.6 KB)

**Location**: `C:\Programming\RTRP\simsecure\modules\password_test.py`

**Purpose**: Password strength analysis using regex pattern matching.

**Main Function**: `test_password(password)`

**Input Parameters**:
- `password` (string): Password to analyze

**Output Format**:
- Returns tuple: `(security_score, findings_list)`
- security_score: Integer 0-10
- findings_list: List of results and recommendations

**Validation Mechanism**:

Each criterion uses regular expression (regex) patterns to validate:

1. **Length Check**: `len(password) >= 8`
   - Pattern: Counts characters
   - Requirement: Minimum 8 characters
   - Points: +2

2. **Uppercase Check**: `[A-Z]` exists
   - Pattern: Searches for A-Z
   - Requirement: At least 1 uppercase letter
   - Points: +2

3. **Lowercase Check**: `[a-z]` exists
   - Pattern: Searches for a-z
   - Requirement: At least 1 lowercase letter
   - Points: +2

4. **Number Check**: `[0-9]` exists
   - Pattern: Searches for 0-9
   - Requirement: At least 1 digit
   - Points: +2

5. **Special Characters Check**: `[!@#$%^&*()_+{}\[\]:;<>,.?/~-]`
   - Pattern: Matches special characters
   - Requirement: At least 1 special character
   - Points: +2

6. **Bonus for Length**: `len(password) >= 16`
   - Requirement: 16+ characters
   - Bonus: +1 point (max score stays 10)

**Strength Rating System**:

```
Points 0-3:   VERY WEAK    (Red) - Easily cracked
Points 4-5:   WEAK         (Red) - Vulnerable
Points 6-7:   MODERATE     (Yellow) - Acceptable but improvable
Points 8-9:   STRONG       (Green) - Good security
Points 10+:   EXCELLENT    (Green) - Optimal security
```

**Recommendations Generated**:

Based on missing criteria, specific recommendations provided:
- "Add at least one uppercase letter"
- "Include at least one number"
- "Include special characters like !@#$%"
- "Increase length to at least 8 characters"
- "Consider using 16+ characters for extra security"

**Example Usage**:
```python
from modules.password_test import test_password

score, findings = test_password("MyP@ssw0rd#123")
print(f"Score: {score}/10")
for finding in findings:
    print(f"  {finding}")
```

**Expected Output Examples**:

**Example 1 - Weak Password**:
```
Score: 3/10 - VERY WEAK
  ✗ Length is less than 8 characters
  ✓ Contains uppercase letters
  ✓ Contains lowercase letters
  ✗ No numbers found
  ✗ No special characters found

Recommendations:
  → Add numbers (0-9) to your password
  → Include special characters (!@#$%)
  → Increase length to at least 8 characters
```

**Example 2 - Strong Password**:
```
Score: 10/10 - EXCELLENT
  ✓ Length is 8 or more characters (14 chars)
  ✓ Contains uppercase letters (M, P)
  ✓ Contains lowercase letters (y, s, s, w, r, d, o, r, d)
  ✓ Includes numbers (1, 2, 3)
  ✓ Includes special characters (#, @)
  ✓ Bonus: Length 16+ characters

Recommendations:
  → Your password meets all security requirements!
```

---

### Module 4: report.py (~4 KB)

**Location**: `C:\Programming\RTRP\simsecure\modules\report.py`

**Purpose**: Professional security report generation with timestamps.

**Main Functions**:

#### Function 1: `generate_report(scan_type, target, score, findings)`
- Primary report generation function
- Creates timestamped file
- Stores in reports/ directory
- Handles directory creation

#### Function 2: `generate_report_content()`
- Generates formatted report text
- Structures all findings
- Includes banner and disclaimer

**Input Parameters**:
- `scan_type` (string): "website", "port", or "password"
- `target` (string): What was scanned
- `score` (integer): Security score 0-10
- `findings` (list): List of finding strings

**Report Structure**:

```
═══════════════════════════════════════════════════
    SimSecure - Professional Security Report
═══════════════════════════════════════════════════

Scan Type: [WEBSITE/PORT/PASSWORD]
Target: [target details]
Scan Date: [YYYY-MM-DD HH:MM:SS]

FINDINGS:
─────────────────────────────────────────────────
[Each finding on separate line with bullet]

SECURITY SCORE: [X]/10
Rating: [EXCELLENT/STRONG/MODERATE/WEAK/VERY WEAK]

RECOMMENDATIONS:
─────────────────────────────────────────────────
[Security recommendations based on findings]

DISCLAIMER:
This tool is designed for authorized security testing only.
Unauthorized access to computer systems is illegal.
```

**File Naming Convention**:
- Pattern: `scan_report_[TYPE]_[TIMESTAMP].txt`
- Type: web, port, or password
- Timestamp: YYYY-MM-DD_HH-MM-SS
- Examples:
  - `scan_report_web_2026-03-09_14-23-45.txt`
  - `scan_report_port_2026-03-09_15-10-30.txt`
  - `scan_report_password_2026-03-09_16-45-12.txt`

**Storage Location**:
- Primary: `C:\Programming\RTRP\simsecure\reports\`
- Auto-created: Directory created automatically if missing
- Permissions: Readable/writable by current user

**Report Generation Triggers**:
- Manual: User adds `--report` flag to any command
- Automatic: Can be called from Python code directly

**Example Usage**:
```bash
# Generate report from command line
simsecure web https://example.com --report

# From Python code
from modules.report import generate_report

generate_report(
    scan_type="password",
    target="Test123!@#",
    score=9,
    findings=["Length ≥ 8: ✓", "Uppercase: ✓", "etc..."]
)
```

**Report Example Output**:
```
═══════════════════════════════════════════════════
    SimSecure - Professional Security Report
═══════════════════════════════════════════════════

Scan Type: Website Security
Target: https://httpbin.org
Scan Date: 2026-03-09 14:23:45

FINDINGS:
─────────────────────────────────────────────────
- HTTPS is enabled
- X-Frame-Options header is missing
- Content-Security-Policy header is missing
- X-XSS-Protection header is missing
- Strict-Transport-Security header is missing
- X-Content-Type-Options header is missing
- Server header is exposed: gunicorn/19.9.0

SECURITY SCORE: 2/10
Rating: WEAK

RECOMMENDATIONS:
- Add X-Frame-Options header to prevent clickjacking
- Implement Content-Security-Policy
- Hide server information in HTTP headers

DISCLAIMER:
This tool is designed for authorized security testing only.
```

---

## SECURITY SCORING SYSTEM

### Overall Scoring Philosophy

SimSecure uses a standardized **0-10 scale** for all security assessments, allowing consistent evaluation and comparison across different scan types.

### Score Interpretation

| Score | Rating | Color | Meaning | Action |
|-------|--------|-------|---------|--------|
| 10 | EXCELLENT | Green | Optimal security posture | Maintain current practices |
| 8-9 | STRONG | Green | Good security measures | Minor improvements beneficial |
| 6-7 | MODERATE | Yellow | Acceptable but improvable | Implement recommendations |
| 4-5 | WEAK | Yellow/Red | Significant vulnerabilities | Address issues promptly |
| 0-3 | VERY WEAK | Red | Critical security issues | Urgent action required |

### Website Scanner Scoring

**Scoring Mechanism**: Points awarded for each security header detected/enabled.

**Point Distribution** (Maximum 10):
- HTTPS enabled: +1 point
- X-Frame-Options present: +1 point
- Content-Security-Policy present: +1 point
- X-XSS-Protection present: +1 point
- Strict-Transport-Security present: +1 point
- X-Content-Type-Options present: +1 point
- Server header hidden: +1 point
- Bonus points for extra measures: Up to +3 points

**Scoring Examples**:
- All headers present: 10/10 - EXCELLENT
- 5-6 headers present: 6-7/10 - MODERATE
- 2-3 headers present: 2-3/10 - VERY WEAK
- HTTPS only: 1/10 - VERY WEAK

### Port Scanner Scoring

**Scoring Mechanism**: Points deducted based on number of open ports.

**Point Distribution**:
- 0 open ports: 10/10 - EXCELLENT (hardened system)
- 1 open port: 9/10 - STRONG
- 2 open ports: 8/10 - STRONG
- 3-4 open ports: 6/10 - MODERATE
- 5-6 open ports: 4/10 - WEAK
- 7+ open ports: 2/10 - VERY WEAK

**Risk Assessment**:
High-risk ports are flagged for immediate attention:
- Any Telnet (23) open: Major concern
- Any FTP (21) open: Major concern
- Database ports (3306, 5432, 27017) open: Significant concern
- Only web ports (80, 443) open: Low concern

### Password Strength Scoring

**Scoring Mechanism**: Points awarded for each validation criterion met.

**Point Distribution** (Maximum 11, capped at 10):
- Minimum 8 characters: +2 points
- Uppercase letter (A-Z): +2 points
- Lowercase letter (a-z): +2 points
- Number (0-9): +2 points
- Special character (!@#$%^&*): +2 points
- 16+ characters bonus: +1 point (extra)

**Scoring Breakdown**:
- 0-3 points: VERY WEAK - Add missing requirements
- 4-5 points: WEAK - Missing 2+ requirements
- 6-7 points: MODERATE - Missing 1-2 requirements
- 8-9 points: STRONG - Meeting 4 requirements
- 10+ points: EXCELLENT - All requirements met

### Comparative Security Scoring

**Same Score, Different Contexts**:
- Website 5/10: Has HTTPS but missing 5 headers = Moderate risk
- Port 5/10: Has 5 ports open = Higher practical risk
- Password 5/10: Missing multiple validation rules = Weak but acceptable

**Score Weighting**:
Each scanner uses same 0-10 scale but different criteria:
- Website: Focuses on security headers/configuration
- Port: Based on surface area (open ports)
- Password: Based on entropy/complexity

---

## HOW TO USE - STEP BY STEP

### Initial Setup

#### Step 1: Verify Installation

Open Command Prompt or PowerShell and check if tool is installed globally:

```powershell
simsecure -ls
```

**If it works**, you'll see:
```
=== AVAILABLE SECURITY CHECKS ===
1. Website Security Scanner
2. Port Scanner
3. Password Strength Tester
Add --report flag to generate security reports
```

**If it doesn't work**, complete global installation first (see Installation section).

#### Step 2: Understand Your Options

SimSecure offers multiple usage modes:

1. **Interactive Mode**: Menu-driven interface
2. **Command-line Mode**: Direct command execution
3. **Batch Mode**: Automated scanning (scripting)
4. **Report Generation**: Save results to files

### Using the Website Security Scanner

#### Method 1: Interactive Prompt

```bash
simsecure web
# Then enter URL when prompted
```

#### Method 2: Direct Command

```bash
simsecure web https://example.com
```

#### Method 3: With Report Generation

```bash
simsecure web https://example.com --report
```

**Step-by-Step Process**:

1. **Enter the command** with target URL
2. **Tool connects** to the website (5-second timeout)
3. **Analyzes response headers** for 7 security checks
4. **Calculates security score** (0-10)
5. **Displays findings** on terminal
6. **Optionally saves** report to reports/ folder

**Output Interpretation**:

```
Website Security Assessment Results
Target: https://example.com
Time: 2026-03-09 14:23:45

HTTPS Status: Enabled (✓)
Security Headers Check:
  X-Frame-Options: Missing (✗)
  CSP: Missing (✗)
  HSTS: Present (✓)
  ... [other headers]

Security Score: 6/10 - MODERATE

Next Steps:
  - Implement missing security headers
  - Configure CSP policy
  - Review server configuration
```

### Using the Port Scanner

#### Method 1: Interactive Prompt

```bash
simsecure port
# Then enter hostname/IP when prompted
```

#### Method 2: Direct Command

```bash
simsecure port example.com
```

#### Method 3: With Report

```bash
simsecure port 192.168.1.1 --report
```

**Step-by-Step Process**:

1. **Enter command** with target host
2. **Tool spawns 17 threads** (one per port)
3. **Each thread attempts connection** with 2-second timeout
4. **Collects results** from all threads
5. **Identifies services** for open ports
6. **Calculates security score** based on open count
7. **Displays findings** with risk assessment

**Output Interpretation**:

```
Port Scan Assessment
Target: example.com (93.184.216.34)
Scan Start: 2026-03-09 14:25:10

SCAN RESULTS:
  Port 80 (HTTP): OPEN - Warning: Unencrypted web traffic
  Port 443 (HTTPS): OPEN - Standard HTTPS port
  Port 22 (SSH): CLOSED - Access restricted (good)
  Port 3306 (MySQL): CLOSED - Database not exposed (good)
  ... [other ports]

OPEN PORTS: 2
  - Port 80 (HTTP): Web server
  - Port 443 (HTTPS): Web server

Security Score: 8/10 - STRONG

Risk Assessment:
  - Both open ports are expected (web server)
  - No dangerous services detected
  - Firewall appears properly configured
```

### Using the Password Strength Tester

#### Method 1: Interactive Prompt

```bash
simsecure password
# Then enter password when prompted
```

#### Method 2: Direct Command

```bash
simsecure password "MyPassword123!"
```

**IMPORTANT**: When using direct command, wrap password in quotes!

#### Method 3: With Report

```bash
simsecure password "SecureP@ss123" --report
```

**Step-by-Step Process**:

1. **Enter command** with password
2. **Tool validates** against 5 criteria
3. **Performs regex matching** for each rule
4. **Calculates score** (0-10 based on criteria met)
5. **Determines strength rating**
6. **Provides specific recommendations**
7. **Displays results** with color coding

**Output Interpretation**:

```
Password Strength Analysis
Password: [hidden for security]
Analysis Date: 2026-03-09 14:27:32

VALIDATION RESULTS:
  Length (≥8 chars): ✓ PASS (14 characters)
  Uppercase (A-Z): ✓ PASS (My, P)
  Lowercase (a-z): ✓ PASS (y, a, s, s, w, r, d)
  Numbers (0-9): ✓ PASS (123)
  Special (!@#$): ✓ PASS (!)
  
BONUS CHECKS:
  Length ≥16 chars: ✗ (14 characters) - Nearly qualified

Security Score: 10/10 - EXCELLENT

Strength Rating: EXCELLENT
Color: Green - This is a strong password

Recommendations:
  ✓ Your password meets all security requirements
  → Consider increasing to 16+ characters for extra security
  → Avoid using personal information
  → Use different passwords for different services
```

### Using the Interactive Menu Mode

#### Method 1: Launch Interactive Mode

```bash
simsecure
# or
simsecure --interactive
```

**Step-by-Step**:

1. **Displays main menu** with 5 options:
   ```
   === SimSecure Main Menu ===
   1. Website Security Scanner
   2. Port Scanner
   3. Password Strength Tester
   4. Help
   5. Exit
   ```

2. **Enter your choice** (1-5)

3. **Tool prompts** for target information:
   ```
   Enter website URL (e.g., https://example.com):
   https://example.com
   ```

4. **Performs scan** and displays results

5. **Asks to save report**:
   ```
   Save this report to file? (yes/no):
   yes
   ```

6. **Offers to scan another** or exit

### Using Report Generation

#### Adding Report Flag

Any command can include `--report` to save results:

```bash
# All of these save reports
simsecure web https://example.com --report
simsecure port example.com --report
simsecure password "test123" --report
```

#### Finding Generated Reports

Reports are saved in: `C:\Programming\RTRP\simsecure\reports\`

**Filenames include timestamp**:
- `scan_report_web_2026-03-09_14-23-45.txt`
- `scan_report_port_2026-03-09_15-10-30.txt`
- `scan_report_password_2026-03-09_16-45-12.txt`

#### Using Reports

```bash
# View report in terminal
type C:\Programming\RTRP\simsecure\reports\scan_report_web_2026-03-09_14-23-45.txt

# Or open in text editor
notepad C:\Programming\RTRP\simsecure\reports\scan_report_web_2026-03-09_14-23-45.txt
```

---

## EXAMPLE COMMANDS

### Website Scanner Examples

**Example 1: Scan a government website**
```bash
simsecure web https://www.whitehouse.gov
```
Expected: High score (government sites typically have good security)

**Example 2: Scan with report**
```bash
simsecure web https://httpbin.org --report
```
Expected: Lower score (httpbin is testing tool, not hardened)

**Example 3: Scan local development server**
```bash
simsecure web http://localhost:3000
```
Expected: May show warnings (dev servers often skip security headers)

### Port Scanner Examples

**Example 1: Scan a domain**
```bash
simsecure port google.com
```
Expected: Only find ports 80 and 443 (score 8/10)

**Example 2: Scan localhost**
```bash
simsecure port localhost
```
Expected: May show various ports depending on services running

**Example 3: Scan IP address**
```bash
simsecure port 8.8.8.8
```
Expected: Google's public DNS - likely minimal open ports

### Password Strength Examples

**Example 1: Weak password**
```bash
simsecure password "hello"
```
Expected: 0/10 - VERY WEAK (too short, no diversity)

**Example 2: Moderate password**
```bash
simsecure password "Hello123"
```
Expected: 8/10 - STRONG (missing special characters)

**Example 3: Excellent password**
```bash
simsecure password "Tr0p1c@lThunderst0rm#2026"
```
Expected: 10/10 - EXCELLENT (meets all criteria + length bonus)

### Batch Processing Examples

**Example 1: Scan multiple websites**
```bash
for /f %i in (websites.txt) do simsecure web %i --report
```

**Example 2: Scan multiple hosts**
```bash
for /f %i in (hosts.txt) do simsecure port %i --report
```

**Example 3: Create compliance report**
```bash
simsecure web https://example.com --report
simsecure port example.com --report
simsecure password "AdminPass123!" --report
```

---

## FILE STRUCTURE DETAILS

### Main Entry Point: simsecure.py

**Size**: ~14 KB
**Type**: Python executable module
**Shebang**: `#!/usr/bin/env python3`

**Purpose**: Orchestrates all security scanning operations through command-line interface.

**Key Components**:

1. **Banner and Disclaimer Functions**
   - `print_banner()`: Displays ASCII art banner with app name
   - `print_disclaimer()`: Shows legal warnings about authorized use
   - Unicode characters replaced with ASCII for Windows compatibility

2. **Menu Functions**
   - `print_menu()`: Displays interactive menu options
   - `print_help_menu()`: Shows detailed help information
   - `interactive_mode()`: Main loop for menu-driven interface

3. **Command Handlers**
   - `handle_web_scan()`: Routes to web_scan module
   - `handle_port_scan()`: Routes to port_scan module
   - `handle_password_test()`: Routes to password_test module

4. **Main Entry Point**
   - `main()`: argparse configuration and dispatch logic
   - Handles subcommands: web, port, password
   - Handles flags: -ls/--list, -h/--help, --report, --interactive

### Module Files

#### modules/__init__.py
**Size**: ~500 bytes
**Purpose**: Package initialization and imports

**Contains**:
```python
from .web_scan import scan_website
from .port_scan import scan_ports
from .password_test import test_password
from .report import generate_report
```

Allows direct imports: `from modules import scan_website`

#### modules/web_scan.py
**Size**: ~6 KB
**Purpose**: Website security analysis

**Key Components**:
- Imports: requests, colorama
- Main function: `scan_website(url)`
- Returns: (score: int, findings: list)
- Timeout: 5 seconds per request

#### modules/port_scan.py
**Size**: ~4.6 KB
**Purpose**: TCP port scanning

**Key Components**:
- Imports: socket, threading, colorama
- Functions: `check_port()`, `scan_ports()`
- Threading: 17 concurrent threads
- Timeout: 2 seconds per port

#### modules/password_test.py
**Size**: ~4.6 KB
**Purpose**: Password strength analysis

**Key Components**:
- Imports: re (regex), colorama
- Main function: `test_password(password)`
- Returns: (score: int, findings: list)
- Regex patterns for 5 validation rules

#### modules/report.py
**Size**: ~4 KB
**Purpose**: Report generation and formatting

**Key Components**:
- Imports: datetime, os
- Functions: `generate_report()`, `generate_report_content()`
- Creates: Text files with timestamps
- Location: reports/ directory (auto-created)

### Configuration Files

#### requirements.txt
**Purpose**: Python package dependencies

**Content**:
```
requests>=2.25.0
colorama>=0.4.3
```

Used for: `pip install -r requirements.txt`

#### setup.py
**Purpose**: Package metadata and installation configuration

**Key Settings**:
- Version: 1.0.0
- Author: Developer name (customizable)
- Packages: ['modules']
- Console scripts entry point: simsecure = simsecure:main
- Dependencies: requests, colorama

Used for: `pip install -e .`

### Wrapper and Installation Files

#### simsecure.bat
**Size**: ~300 bytes
**Platform**: Windows only
**Purpose**: Global command wrapper on Windows

**Contents**:
```batch
@echo off
python C:\Programming\RTRP\simsecure\simsecure.py %*
```

**Mechanism**: Calls Python with full path to script, passes all arguments

#### simsecure (shell script)
**Size**: ~400 bytes
**Platform**: Linux/macOS
**Purpose**: Global command wrapper on Unix systems

**Key Elements**:
- Shebang: #!/bin/bash
- SIMSECURE_PATH variable: Path to simsecure.py
- Searches multiple standard locations
- Passes all arguments through

#### install_global.bat
**Size**: ~500 bytes
**Platform**: Windows only
**Purpose**: Automated global installation

**Process**:
1. Checks for admin privileges
2. Copies simsecure.bat to C:\Windows\System32\
3. Verifies successful copy
4. Tests installation with simsecure -ls

### Documentation Files

#### README.md
**Quick start guide** with installation steps and basic usage

#### SETUP_GLOBAL.md
**Complete global setup** instructions for all platforms

#### QUICK_START.md
**Examples and quick reference** for common tasks

#### HOW_TO_USE.md
**Detailed usage guide** for each scanner type

#### INSTALL.md
**Installation procedures** for different scenarios

#### PROJECT_SUMMARY.md
**Project overview** and feature descriptions

### Generated Folders

#### reports/
**Purpose**: Stores generated security reports
**Files**: Timestamped report files (scan_report_*.txt)
**Created**: Automatically on first report generation
**Access**: Read/write permissions for current user

#### simsecure.egg-info/
**Purpose**: pip package metadata
**Created**: Automatically on `pip install -e .`
**Files**: PKG-INFO, top_level.txt, requires.txt, etc.

#### __pycache__/
**Purpose**: Python bytecode cache
**Created**: Automatically on first execution
**Purpose**: Speed up Python imports on subsequent runs

---

## TROUBLESHOOTING GUIDE

### Installation Issues

#### Problem: "Python is not recognized"

**Cause**: Python not installed or not in PATH

**Solution**:
1. Install Python from https://www.python.org
2. During installation, **check "Add Python to PATH"**
3. Restart Command Prompt
4. Test: `python --version`

#### Problem: "pip is not recognized"

**Cause**: pip not installed with Python

**Solution**:
```bash
# Reinstall pip
python -m pip install --upgrade pip

# Verify
pip --version
```

#### Problem: "Module not found: requests"

**Cause**: requests library not installed

**Solution**:
```bash
pip install requests>=2.25.0
```

#### Problem: "Permission denied" on global installation

**Cause**: Not running as administrator

**Solution** (Windows):
1. Right-click Command Prompt
2. Select "Run as administrator"
3. Run install_global.bat
4. Click "Yes" when Windows asks for permission

### Runtime Issues

#### Problem: "simsecure not found" after global installation

**Cause**: PATH not updated or installation incomplete

**Solution**:
1. Open new Command Prompt/PowerShell window
2. Verify installation: `simsecure -ls`
3. If still fails, try manual installation:
   ```bash
   copy simsecure.bat C:\Windows\System32\
   ```

#### Problem: "Connection timeout" when scanning

**Cause**: Target unreachable or network issue

**Solutions**:
1. Verify target is accessible: `ping target.com`
2. Check internet connection
3. Try different target
4. Extend timeout (edit source code if needed)

#### Problem: Website scan returns score 0/10

**Cause**: Connection refused or SSL error

**Solutions**:
1. Check URL is correct with https://
2. Try without https:// to use http://
3. Verify SSL certificate is valid
4. Check firewall/proxy not blocking

#### Problem: Port scan shows all ports closed

**Cause**: Firewall blocking all ports (expected)

**Solution**: This is secure behavior - firewall is working
- If ports SHOULD be open, check firewall rules
- If this is expected, score 10/10 is actually excellent

#### Problem: Password test not working

**Cause**: Special characters not recognized

**Solution**: Verify password is in quotes:
```bash
# Wrong
simsecure password MyPassword!

# Correct
simsecure password "MyPassword!"
```

#### Problem: Unicode/Encoding errors

**Cause**: Terminal not using correct encoding

**Solutions** (Windows):
```bash
# Set console encoding
chcp 65001

# Then run tool
simsecure -ls
```

### Report Generation Issues

#### Problem: "Permission denied" when saving report

**Cause**: No write access to reports/ folder

**Solutions**:
1. Check folder permissions
2. Run as administrator
3. Create reports/ folder manually:
   ```bash
   mkdir C:\Programming\RTRP\simsecure\reports
   ```

#### Problem: Reports folder not created

**Cause**: Tool hasn't generated first report yet

**Solution**: Generate a report - folder will auto-create:
```bash
simsecure password "test" --report
```

#### Problem: Report file is empty or incomplete

**Cause**: Scan was interrupted or failed

**Solutions**:
1. Try scan again
2. Check console for error messages
3. Ensure target is accessible

### Platform-Specific Issues

#### Windows: "Cannot find batch file"

**Cause**: Batch file path incorrect or not in PATH

**Solution**:
1. Full path: `C:\Programming\RTRP\simsecure\simsecure.bat web https://example.com`
2. Or add to PATH and try: `simsecure web https://example.com`

#### Linux/macOS: "Command not found"

**Cause**: Script not in PATH or not executable

**Solution**:
```bash
# Make executable
chmod +x /usr/local/bin/simsecure

# Verify location
which simsecure

# Test
simsecure -ls
```

#### Linux/macOS: "Python: command not found"

**Cause**: Python not installed or wrong version

**Solution**:
```bash
# Install Python
sudo apt install python3  # Ubuntu/Debian
brew install python3      # macOS

# Verify
python3 --version
```

---

## FREQUENTLY ASKED QUESTIONS

### General Questions

**Q1: Is SimSecure free?**
A: Yes, SimSecure is open source and completely free to use for authorized security testing.

**Q2: Can I use SimSecure on production systems?**
A: Yes, but with caution. Website and password testing is safe. Port scanning may trigger alerts - ensure you have proper authorization.

**Q3: Does SimSecure require internet?**
A: For website and port scanning, yes. For password testing, no - it works offline.

**Q4: Is my data sent to remote servers?**
A: No. SimSecure only connects directly to your specified targets. No data is logged or sent elsewhere.

### Usage Questions

**Q5: Can I scan multiple targets at once?**
A: Not directly in one command, but you can create a batch script:
```bash
for /f %i in (targets.txt) do simsecure web %i --report
```

**Q6: How do I scan behind a proxy?**
A: Edit the source code to add proxy support to requests:
```python
proxies = {"http": "http://proxy:port", "https": "http://proxy:port"}
response = requests.get(url, proxies=proxies, timeout=5)
```

**Q7: Can I customize the security checks?**
A: Yes, the source code is modular. Edit modules/web_scan.py, modules/port_scan.py, etc.

**Q8: How often should I scan?**
A: For production systems: Monthly for websites, quarterly for ports, regularly for passwords (when changed).

### Technical Questions

**Q9: What's the difference between HTTP and HTTPS?**
A: HTTP is unencrypted, HTTPS is encrypted. Always use HTTPS for sensitive data.

**Q10: Why does the port scanner only check 17 ports?**
A: These 17 ports are the most commonly exploited. You can add more ports by editing port_scan.py.

**Q11: How strong must a password be?**
A: Aim for 10/10. At minimum, require all 5 criteria (uppercase, lowercase, number, special, 8+ chars).

**Q12: Can site owners detect my scan?**
A: Yes, the website scanner makes HTTP requests that may appear in server logs. Port scanning is more noticeable.

### Security Questions

**Q13: Is scanning websites without permission illegal?**
A: Yes. Only scan websites you own or have written permission to test.

**Q14: Can SimSecure be used for malicious purposes?**
A: Like any security tool, it can be misused. Only use for authorized testing.

**Q15: Does SimSecure have vulnerabilities?**
A: It's designed for basic security checks. For production use, consider additional tools.

**Q16: How often is SimSecure updated?**
A: Updates available as new security standards emerge. Check documentation regularly.

### Performance Questions

**Q17: How long does a port scan take?**
A: Typically 10-30 seconds for 17 ports, depending on network speed and timeout settings.

**Q18: Why is the website scan sometimes slow?**
A: Network latency. Some servers respond slowly. Timeout is 5 seconds per request.

**Q19: Can I increase scanning speed?**
A: Edit the timeout values in the source code for faster scanning (less reliable).

### Integration Questions

**Q20: Can I import SimSecure into my own Python scripts?**
A: Yes:
```python
from modules import scan_website, scan_ports, test_password

score, findings = scan_website("https://example.com")
```

**Q21: Can I use SimSecure in CI/CD pipelines?**
A: Yes, it's command-line based so can be integrated into automated testing.

**Q22: Does SimSecure have an API?**
A: Currently CLI-only, but the modules can be imported programmatically.

---

## NEXT STEPS

### Immediate Actions

1. **Verify Installation**: Run `simsecure -ls` to confirm
2. **Read SETUP_GLOBAL.md**: Complete guide for your platform
3. **Try First Scan**: `simsecure web https://example.com`
4. **Explore Features**: Try each scanner type

### Learning Path

1. **Week 1**: Learn all three scanners and their purpose
2. **Week 2**: Practice on your own systems
3. **Week 3**: Set up global installation
4. **Week 4**: Integrate into workflows

### Advanced Usage

1. Create batch scripts for regular scanning
2. Parse reports for automation
3. Customize scoring criteria
4. Add additional ports to scanner
5. Extend with additional security checks

### Contributing

Want to improve SimSecure?

1. Identify missing features
2. Test thoroughly
3. Document changes
4. Submit updates

### Support

For issues:
1. Check Troubleshooting Guide (this document)
2. Review FAQ (above)
3. Check source code comments
4. Consult error messages carefully

---

## CONCLUSION

SimSecure is a professional security tool that brings industry-standard security scanning to anyone who needs it. Whether you're a security professional, system administrator, or student learning cybersecurity, SimSecure provides:

- **Professional-grade security assessments**
- **Standardized security scoring**
- **Easy-to-use command-line interface**
- **Comprehensive security reporting**
- **Cross-platform compatibility**
- **Worldwide accessibility after global setup**

Remember: **Always scan only systems you own or have explicit permission to test.** SimSecure is a tool for authorized security testing only.

For questions, review this document thoroughly, or consult the other documentation files (README.md, SETUP_GLOBAL.md, etc.).

**Happy scanning!**

---

Generated: 2026-03-09
Version: 1.0.0
Location: C:\Programming\RTRP\summary_of_simsecure.md
