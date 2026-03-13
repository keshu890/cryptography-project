# SimSecure - Complete Detailed Architecture & File Map

## 📋 Table of Contents
1. [Folder Structure Overview](#folder-structure-overview)
2. [Root Level Files](#root-level-files)
3. [SimSecure Folder Structure](#simsecure-folder-structure)
4. [Core Module Files](#core-module-files)
5. [Documentation Files](#documentation-files)
6. [Configuration Files](#configuration-files)
7. [Data Flow & Workflow](#data-flow--workflow)
8. [File Dependencies](#file-dependencies)

---

## 📁 Folder Structure Overview

```
C:\Programming\RTRP\
│
├── simsecure/                          ← Main tool folder
│   ├── Core Application Files
│   │   ├── simsecure.py               ← Main entry point
│   │   ├── simsecure.bat              ← Windows command wrapper
│   │   ├── simsecure                  ← Unix/Linux/macOS wrapper
│   │   └── setup.py                   ← Python package configuration
│   │
│   ├── modules/                        ← Core security scanning modules
│   │   ├── __init__.py                ← Package initialization
│   │   ├── web_scan.py                ← Website security scanner
│   │   ├── port_scan.py               ← Network port scanner
│   │   ├── password_test.py           ← Password strength analyzer
│   │   └── report.py                  ← Report generation engine
│   │
│   ├── reports/                        ← Generated report storage
│   │   └── scan_report_*.txt          ← Timestamped security reports
│   │
│   ├── Documentation Files
│   │   ├── README.md                  ← Quick start guide
│   │   ├── INSTALL.md                 ← Installation instructions
│   │   ├── QUICK_START.md             ← Quick reference examples
│   │   ├── INSTALL_AND_USE.md         ← Combined guide
│   │   ├── HOW_TO_USE.md              ← Detailed usage guide
│   │   ├── GLOBAL_INSTALL.md          ← Global setup guide
│   │   ├── SETUP_GLOBAL.md            ← Global setup reference
│   │   ├── GLOBAL_SETUP_COMPLETE.md   ← Setup completion guide
│   │   └── PROJECT_SUMMARY.md         ← Project overview
│   │
│   ├── Configuration Files
│   │   ├── requirements.txt           ← Python dependencies
│   │   ├── install_global.bat         ← Windows global installer
│   │   └── setup.py                   ← Python package metadata
│   │
│   ├── Generated Folders
│   │   ├── __pycache__/               ← Python bytecode cache
│   │   ├── simsecure.egg-info/      ← pip package metadata
│   │   └── reports/                   ← Generated report files
│   │
└── summary_of_simsecure.md            ← Complete tool documentation

```

---

## 📄 Root Level Files (C:\Programming\RTRP\)

### summary_of_simsecure.md
**Purpose**: Complete comprehensive reference documentation for the entire SimSecure tool

**Contents**:
- Project overview and features
- Installation instructions (all platforms)
- Technology stack details
- Project structure with detailed descriptions
- Core features breakdown
- Module-by-module technical details
- Security scoring system documentation
- Step-by-step usage guide
- Example commands
- File structure details
- Troubleshooting guide
- 22+ FAQ questions and answers
- Next steps and learning path

**When to Use**: Users wanting deep technical understanding of the tool, complete reference material

**Related Files**: All files in simsecure/ folder

---

## 🔧 SimSecure Folder Structure (C:\Programming\RTRP\simsecure\)

### Main Application Files

#### 1. **simsecure.py** (Main Entry Point - ~14 KB)
**Purpose**: The primary orchestrator and command-line interface for the entire tool

**Key Functions**:
- `print_banner()` - Displays ASCII art startup banner
- `print_disclaimer()` - Shows legal/ethical warnings
- `print_menu()` - Interactive menu display
- `print_help_menu()` - Detailed help information
- `interactive_mode()` - Main loop for menu-driven interface
- `handle_web_scan()` - Routes to web_scan module
- `handle_port_scan()` - Routes to port_scan module
- `handle_password_test()` - Routes to password_test module
- `main()` - argparse configuration and command dispatch

**Imports**:
- `colorama` - Cross-platform colored terminal output
- `modules` - All four core security modules
- `argparse` - Command-line argument parsing
- `os`, `sys` - System operations

**Available Commands**:
```
simsecure web <URL>              - Scan website security
simsecure port <HOST>            - Scan network ports
simsecure password <PASSWORD>    - Test password strength
simsecure -ls / --list          - List all commands
simsecure -h / --help           - Show help
simsecure --report              - Save results to file
```

**Flow**:
1. Parse command-line arguments
2. Call appropriate module function
3. Receive (score, findings) tuple
4. Display results with colors
5. Optionally generate report

---

#### 2. **simsecure.bat** (Windows Command Wrapper - ~663 bytes)
**Purpose**: Enable `simsecure` command to work from any directory on Windows

**Content**:
```batch
@echo off
python "C:\Programming\RTRP\simsecure\simsecure.py" %*
```

**How It Works**:
1. User types: `simsecure password "test123"` (from anywhere)
2. Windows executes this batch file
3. Batch file runs Python with simsecure.py
4. All command-line arguments passed through via `%*`
5. Output displays in terminal

**Installation**: Copy to `C:\Windows\System32\` for global access

**Related Files**: 
- simsecure.py (actual tool)
- install_global.bat (automated installer)

---

#### 3. **simsecure** (Unix/Linux/macOS Wrapper - ~1.2 KB)
**Purpose**: Enable `simsecure` command on Unix-like systems

**Content** (Bash script):
```bash
#!/bin/bash
SIMSECURE_PATH="/path/to/simsecure.py"

if [ -f "$SIMSECURE_PATH" ]; then
    python3 "$SIMSECURE_PATH" "$@"
else
    echo "Error: simsecure.py not found"
fi
```

**Installation Steps**:
1. Copy to `/usr/local/bin/simsecure`
2. Make executable: `chmod +x /usr/local/bin/simsecure`
3. Edit SIMSECURE_PATH to point to actual simsecure.py location
4. Use globally: `simsecure -ls`

**Related Files**:
- simsecure.py (actual tool)
- SETUP_GLOBAL.md (setup instructions)

---

#### 4. **setup.py** (Python Package Configuration - ~1.8 KB)
**Purpose**: Allows installation of SimSecure as a pip package

**Key Components**:
- **name**: "simsecure" - Package name
- **version**: "1.0.0" - Current version
- **author**: Security Research Team
- **entry_points**: Console command definition
  - Allows `pip install -e .` to create `simsecure` command
- **install_requires**: Dependencies
  - `requests>=2.25.0` - HTTP requests
  - `colorama>=0.4.3` - Colored terminal output
- **packages**: Auto-discovers everything in `modules/`
- **classifiers**: Python 3.7+ support, MIT License

**Usage**:
```bash
cd C:\Programming\RTRP\simsecure
pip install -e .
# Now 'simsecure' command available globally
```

**Related Files**:
- requirements.txt (dependency list)
- simsecure.py (main module)

---

### Core Module Files (modules/ folder)

#### 5. **modules/__init__.py** (Package Initialization - ~500 bytes)
**Purpose**: Makes `modules` a Python package and exports functions

**Content**:
```python
from .web_scan import scan_website
from .port_scan import scan_ports
from .password_test import test_password
from .report import generate_report
```

**Enables**:
```python
from modules import scan_website, test_password, etc.
```

**Dependency Chain**:
- Used by: simsecure.py
- Imports from: All four module files

---

#### 6. **modules/web_scan.py** (Website Security Scanner - ~6 KB)

**Purpose**: Analyze websites for security vulnerabilities and misconfigurations

**Main Function**: `scan_website(url)`

**Input**: 
- `url` (string): Website URL to scan

**Process Flow**:
1. Validate and normalize URL
2. Send HTTP request with timeout
3. Extract response headers
4. Check 7 security criteria
5. Calculate security score (0-10)
6. Compile findings list
7. Return (score, findings) tuple

**Security Checks Performed**:
1. **HTTPS Enabled** - Verifies encrypted connection
2. **X-Frame-Options** - Prevents clickjacking attacks
3. **Content-Security-Policy** - Restricts resource loading
4. **X-XSS-Protection** - Legacy XSS protection
5. **Strict-Transport-Security** - Forces HTTPS
6. **X-Content-Type-Options** - Prevents MIME sniffing
7. **Server Header** - Detects information leakage

**Scoring Logic**:
- Maximum 10 points (1 point per check + 3 bonus)
- Points awarded for security headers detected
- Deductions for vulnerabilities found

**Output Example**:
```
Security Score: 2/10 - WEAK
Findings:
  - HTTPS is enabled ✓
  - X-Frame-Options header is missing ✗
  - Content-Security-Policy header is missing ✗
  [etc...]
```

**Error Handling**:
- Connection timeouts (5 seconds)
- Invalid URLs
- DNS failures
- SSL certificate errors
- Network unreachability

**Dependencies**:
- `requests` - HTTP library
- `colorama` - Colored output

**Related Files**:
- simsecure.py (calls this module)
- report.py (receives output for reports)

---

#### 7. **modules/port_scan.py** (Network Port Scanner - ~4.6 KB)

**Purpose**: Identify open network ports and discover services

**Main Functions**:
- `check_port(host, port)` - Check single port (internal)
- `scan_ports(host)` - Main scanning function

**Input**:
- `host` (string): Domain name or IP address

**Process Flow**:
1. Resolve hostname to IP address
2. Create 17 concurrent threads (one per port)
3. Each thread attempts TCP connection (2-second timeout)
4. Collect results from all threads
5. Identify services for open ports
6. Calculate security score based on port count
7. Return (score, findings) tuple

**Ports Scanned** (17 total):
| Port | Service | Purpose |
|------|---------|---------|
| 21 | FTP | File Transfer (Unencrypted) |
| 22 | SSH | Secure Remote Access |
| 23 | Telnet | Remote Access (Unencrypted) |
| 25 | SMTP | Email Sending |
| 53 | DNS | Domain Resolution |
| 80 | HTTP | Web Traffic (Unencrypted) |
| 110 | POP3 | Email Retrieval |
| 139 | NetBIOS | Windows File Sharing |
| 143 | IMAP | Email Retrieval |
| 443 | HTTPS | Web Traffic (Encrypted) |
| 3306 | MySQL | Database |
| 5432 | PostgreSQL | Database |
| 5984 | CouchDB | NoSQL Database |
| 6379 | Redis | Cache/Session Storage |
| 8080 | HTTP Proxy | Alternative HTTP |
| 27017 | MongoDB | NoSQL Database |
| 8443 | HTTPS Alt | Alternative HTTPS |

**Scoring Logic**:
```
0 ports open  → 10/10 (Excellent)
1 port open   → 9/10 (Very Good)
2 ports open  → 8/10 (Good)
3-4 ports     → 6/10 (Fair)
5+ ports      → 4/10 (Poor)
```

**Output Example**:
```
Security Score: 6/10 - MODERATE
Found 4 open ports:
  - Port 80 (HTTP): Open
  - Port 443 (HTTPS): Open
  - Port 8080 (HTTP Proxy): Open
  - Port 8443 (HTTPS Alt): Open
```

**Implementation Detail** - Threading:
```python
import threading
threads = []
for port in ports_list:
    t = threading.Thread(target=check_port, args=(host, port), daemon=True)
    t.start()
    threads.append(t)
for t in threads:
    t.join(timeout=2)  # Wait max 2 seconds per thread
```

**Error Handling**:
- Network unreachability
- DNS resolution failure
- Connection refused (handled as "closed")
- Socket timeout (handled as "unreachable")

**Dependencies**:
- `socket` - TCP connections
- `threading` - Concurrent scanning
- `colorama` - Colored output

**Related Files**:
- simsecure.py (calls this module)
- report.py (receives output for reports)

---

#### 8. **modules/password_test.py** (Password Strength Analyzer - ~4.6 KB)

**Purpose**: Analyze password strength and provide security recommendations

**Main Function**: `test_password(password)`

**Input**:
- `password` (string): Password to analyze

**Process Flow**:
1. Initialize score counter (0 points)
2. Perform regex validation for 5 criteria
3. Increment score for each criterion met
4. Check for 16+ character bonus
5. Cap score at 10 points
6. Determine strength rating
7. Generate recommendations
8. Return (score, findings_with_recommendations) tuple

**Validation Criteria** (Using Regex):

| Criterion | RegEx Pattern | Points | Description |
|-----------|---------------|--------|-------------|
| Minimum Length | `len >= 8` | +2 | At least 8 characters required |
| Uppercase | `[A-Z]` | +2 | At least 1 uppercase letter |
| Lowercase | `[a-z]` | +2 | At least 1 lowercase letter |
| Numbers | `[0-9]` | +2 | At least 1 digit |
| Special Chars | `[!@#$%^&*]` | +2 | At least 1 special character |
| Length Bonus | `len >= 16` | +1 | Extra point if 16+ characters |

**Scoring Breakdown**:
```
0-3 points   → VERY WEAK   (Red)
4-5 points   → WEAK        (Red/Yellow)
6-7 points   → MODERATE    (Yellow)
8-9 points   → STRONG      (Green)
10+ points   → EXCELLENT   (Green)
```

**Output Examples**:

**Weak Password** ("hello"):
```
Score: 2/10 - VERY WEAK
✗ Length: 5 characters (need 8+)
✓ Uppercase: Not found
✓ Lowercase: Yes
✗ Numbers: Not found
✗ Special Characters: Not found

Recommendations:
→ Increase length to 8+ characters
→ Add at least one number
→ Add special characters (!@#$%)
→ Add at least one uppercase letter
```

**Strong Password** ("MySecure#2026Pass"):
```
Score: 10/10 - EXCELLENT
✓ Length: 17 characters
✓ Uppercase: Yes (M, S, P)
✓ Lowercase: Yes (y, e, c, u, r, e, etc.)
✓ Numbers: Yes (2, 0, 2, 6)
✓ Special Characters: Yes (#)
✓ Bonus: Length 16+

Recommendations:
→ Your password meets all security requirements!
→ Consider using in password manager
```

**Dependencies**:
- `re` - Regular expressions for pattern matching
- `colorama` - Colored output

**Related Files**:
- simsecure.py (calls this module)
- report.py (receives output for reports)

---

#### 9. **modules/report.py** (Report Generation Engine - ~4 KB)

**Purpose**: Generate professional security assessment reports with timestamps

**Main Functions**:
- `generate_report(scan_type, target, score, findings)` - Create timestamped report
- `generate_report_content()` - Format report text

**Input Parameters**:
- `scan_type` (string): "website", "port", or "password"
- `target` (string): What was scanned (URL, hostname, etc.)
- `score` (integer): Security score 0-10
- `findings` (list): List of finding strings

**Process Flow**:
1. Create reports/ directory if missing
2. Generate filename with timestamp
3. Format professional report content
4. Write to text file
5. Display completion message
6. Return file path

**Filename Format**:
```
scan_report_[TYPE]_[TIMESTAMP].txt

Examples:
- scan_report_web_2026-03-09_14-23-45.txt
- scan_report_port_2026-03-09_15-10-30.txt
- scan_report_password_2026-03-09_16-45-12.txt
```

**Storage Location**:
```
C:\Programming\RTRP\simsecure\reports\
/path/to/simsecure/reports/
```

**Report Structure**:
```
═════════════════════════════════════════════════════════════
    SimSecure - Professional Security Report
═════════════════════════════════════════════════════════════

Scan Type: Website Security
Target: https://example.com
Scan Date: 2026-03-09 14:23:45

FINDINGS:
─────────────────────────────────────────────────────────
- HTTPS is enabled
- X-Frame-Options header is missing
- Content-Security-Policy header is missing
[... more findings ...]

SECURITY SCORE: 6/10
Rating: MODERATE

RECOMMENDATIONS:
─────────────────────────────────────────────────────────
- Add X-Frame-Options header
- Implement Content-Security-Policy
- Review server configuration

DISCLAIMER:
This tool is for authorized testing only.
Unauthorized access is illegal.
═════════════════════════════════════════════════════════════
```

**Usage**:
```bash
# From command line - automatically called with --report flag
simsecure web https://example.com --report

# From Python code
from modules.report import generate_report
generate_report("password", "Test123!", 9, ["Length: ✓", "Uppercase: ✓", ...])
```

**Error Handling**:
- Directory creation failure
- File write permission errors
- Disk space issues

**Dependencies**:
- `datetime` - Timestamp generation
- `os` - Directory operations

**Related Files**:
- simsecure.py (calls this when --report flag used)
- web_scan.py, port_scan.py, password_test.py (provide data)

---

## 📚 Documentation Files

### Installation & Setup Documents

#### **INSTALL.md** (~3.5 KB)
**Purpose**: Step-by-step installation instructions for all platforms

**Sections**:
- Prerequisites (Python 3.7+, pip)
- Installation methods (local, global, pip)
- Bash/Zsh on Mac/Linux
- Windows Command Prompt/PowerShell
- Troubleshooting common issues
- Verification steps

**Audience**: First-time users, deployment engineers

---

#### **QUICK_START.md** (~4 KB)
**Purpose**: Quick reference with practical examples

**Sections**:
- 5-minute quick start
- Basic commands
- Real-world examples
- Common troubleshooting
- Next steps

**Audience**: Users wanting quick practical examples

---

#### **INSTALL_AND_USE.md** (~5 KB)
**Purpose**: Combined installation and usage guide

**Sections**:
- What is SimSecure
- Step-by-step installation
- Interactive menu mode
- All commands with examples
- Troubleshooting
- Removal instructions

**Audience**: Users wanting complete all-in-one guide

---

#### **HOW_TO_USE.md** (~6 KB)
**Purpose**: Detailed professional usage guide

**Sections**:
- Initial setup verification
- How to use website scanner
- How to use port scanner
- How to use password tester
- Report generation
- Professional use cases
- Compliance and auditing

**Audience**: Security professionals, administrators

---

### Global Installation Guides

#### **GLOBAL_INSTALL.md** (~5 KB)
**Purpose**: Make SimSecure accessible from anywhere

**Sections**:
- Windows global installation
- Linux/macOS global installation
- PowerShell profile setup
- Systemwide accessibility
- Verification checks
- Global usage examples
- Scheduled tasks/cron jobs

**Audience**: Users wanting system-wide access

---

#### **SETUP_GLOBAL.md** (~3.5 KB)
**Purpose**: Quick reference for global setup

**Sections**:
- Windows setup
- Linux/macOS setup
- Verification
- Usage after setup
- Quick examples

**Audience**: Users wanting quick global setup

---

#### **GLOBAL_SETUP_COMPLETE.md** (~6 KB)
**Purpose**: Comprehensive global setup completion guide

**Sections**:
- Installation methods (Windows/Linux/macOS)
- Command examples
- Features after installation
- Using globally
- Real-world scenarios
- Automation examples
- Troubleshooting

**Audience**: Administrators setting up globally

---

### Reference Documents

#### **README.md** (~2 KB)
**Purpose**: First file users see, quick intro and links

**Sections**:
- What is SimSecure
- Key features
- Installation link
- Quick usage
- Documentation links
- License info

**Audience**: All users (entry point)

---

#### **PROJECT_SUMMARY.md** (~4 KB)
**Purpose**: Project overview and status

**Sections**:
- Project structure
- Installation status
- Features
- Commands
- File organization
- Next steps

**Audience**: Project stakeholders, new developers

---

## ⚙️ Configuration Files

### **requirements.txt** (~50 bytes)
**Purpose**: List all Python package dependencies

**Content**:
```
requests>=2.25.0
colorama>=0.4.3
```

**Usage**:
```bash
pip install -r requirements.txt
```

**Why These Packages**:
- **requests**: Industry-standard HTTP library for website scanning
- **colorama**: Cross-platform terminal colors (Windows/Linux/macOS compatible)

---

### **install_global.bat** (~1.5 KB)
**Purpose**: Automated Windows global installation script

**What It Does**:
1. Checks for administrator privileges
2. Copies simsecure.bat to C:\Windows\System32\
3. Tests if simsecure command works globally
4. Displays success message with examples

**Usage**:
```bash
# Right-click → Run as Administrator
install_global.bat
```

**Result**: 
- `simsecure` command available from any directory
- Works like Nmap or any professional tool

**Related Files**:
- simsecure.bat (the file being installed)
- SETUP_GLOBAL.md (manual alternatives)

---

### **setup.py** (~1.8 KB)
**Purpose**: Python package metadata for pip installation

**Key Sections**:
- Package name and version
- Dependencies declaration
- Entry point definition
- Author/license information
- Python version compatibility

**Allows**:
```bash
pip install -e C:\Programming\RTRP\simsecure
# Creates simsecure command globally
```

**Related Files**:
- requirements.txt (dependency list)
- simsecure.py (main module being packaged)

---

## 🗂️ Generated Folders

### **reports/** (Auto-created)
**Purpose**: Store all generated security assessment reports

**Content**: Timestamped .txt files from scans

**File Naming**: `scan_report_[TYPE]_[TIMESTAMP].txt`

**Usage**:
```bash
# Scan websiteand save report
simsecure web https://example.com --report

# Report saved to: reports/scan_report_web_2026-03-09_14-23-45.txt
```

---

### **__pycache__/** (Auto-created)
**Purpose**: Python bytecode cache for faster imports

**Auto-generated**: Yes (created on first run)

**Content**: .pyc files (compiled Python)

**Safe to Delete**: Yes (will be recreated automatically)

---

### **simsecure.egg-info/** (Auto-created)
**Purpose**: pip package metadata directory

**Auto-generated**: When running `pip install -e .`

**Contains**:
- PKG-INFO (package metadata)
- top_level.txt (list of modules)
- requires.txt (dependencies)
- entry_points.txt (console commands)

---

## 🔄 Data Flow & Workflow

### Workflow 1: Website Scan

```
User Input
    ↓
simsecure.py main()
    ↓
Parse "web https://example.com" command
    ↓
Call modules.web_scan.scan_website()
    ↓
web_scan.py:
    → Send HTTP request
    → Extract headers
    → Check 7 security criteria
    → Calculate score (0-10)
    → Compile findings
    ↓
Return (score=6, findings=[...])
    ↓
simsecure.py
    → Display score and findings with colors
    → Optional: Call modules.report.generate_report()
    ↓
Report file created (if --report flag)
    → Saved to: reports/scan_report_web_[timestamp].txt
    ↓
Terminal Output (or file output)
```

### Workflow 2: Port Scan

```
User Input
    ↓
simsecure.py main()
    ↓
Parse "port example.com" command
    ↓
Call modules.port_scan.scan_ports()
    ↓
port_scan.py:
    → Resolve hostname to IP
    → Create 17 threads (one per port)
    → Each thread: Attempt TCP connection (2-sec timeout)
    → Collect results
    → Map ports to services
    → Calculate score based on open count
    → Compile findings
    ↓
Return (score=8, findings=[...])
    ↓
simsecure.py
    → Display score and findings with colors
    → Optional: Call modules.report.generate_report()
    ↓
Report file created (if --report flag)
    → Saved to: reports/scan_report_port_[timestamp].txt
    ↓
Terminal Output (or file output)
```

### Workflow 3: Password Test

```
User Input
    ↓
simsecure.py main()
    ↓
Parse "password MyPass#123" command
    ↓
Call modules.password_test.test_password()
    ↓
password_test.py:
    → Check regex: len >= 8 [+2]
    → Check regex: [A-Z] found [+2]
    → Check regex: [a-z] found [+2]
    → Check regex: [0-9] found [+2]
    → Check regex: [!@#$%^&*] found [+2]
    → Check bonus: len >= 16 [+1]
    → Cap at 10 points
    → Determine rating (WEAK/MODERATE/STRONG/EXCELLENT)
    → Generate recommendations
    ↓
Return (score=10, findings=[...])
    ↓
simsecure.py
    → Display score and findings with colors
    → Optional: Call modules.report.generate_report()
    ↓
Report file created (if --report flag)
    → Saved to: reports/scan_report_password_[timestamp].txt
    ↓
Terminal Output (or file output)
```

### Workflow 4: Report Generation

```
User adds --report flag
    ↓
simsecure.py capture (scan_type, target, score, findings)
    ↓
Call modules.report.generate_report()
    ↓
report.py:
    → Check if reports/ directory exists
    → Create if missing (os.makedirs)
    → Generate filename with timestamp
    → Format professional report content
    → Write to .txt file
    → Display success message with file path
    ↓
File saved
    → Location: C:\Programming\RTRP\simsecure\reports\
    → Filename: scan_report_[TYPE]_[TIMESTAMP].txt
    → Accessible: Yes (readable text file)
```

---

## 📌 File Dependencies

### Dependency Graph

```
simsecure.py (main entry)
    ├→ modules/__init__.py
    │   ├→ modules/web_scan.py
    │   │   ├→ requests (external library)
    │   │   └→ colorama (external library)
    │   │
    │   ├→ modules/port_scan.py
    │   │   ├→ socket (built-in)
    │   │   ├→ threading (built-in)
    │   │   └→ colorama (external library)
    │   │
    │   ├→ modules/password_test.py
    │   │   ├→ re (built-in - regex)
    │   │   └→ colorama (external library)
    │   │
    │   └→ modules/report.py
    │       ├→ datetime (built-in)
    │       ├→ os (built-in)
    │       └→ pathlib (built-in)
    │
    ├→ colorama (external library)
    ├→ argparse (built-in)
    ├→ sys (built-in)
    └→ os (built-in)

setup.py (packaging)
    ├→ simsecure.py (entry point)
    └→ modules/ (package_data)

Wrapper Scripts
    ├→ simsecure.bat → simsecure.py
    ├→ simsecure → simsecure.py (Unix/Linux)
    └→ install_global.bat → simsecure.bat
```

### Import Chain

```
1. User runs: simsecure web https://example.com

2. simsecure.py imports:
   from modules.web_scan import scan_website
   from modules.port_scan import scan_ports
   from modules.password_test import test_password
   from modules.report import generate_report
   from colorama import init, Fore, Style

3. When web_scan.py imported, IT imports:
   import requests
   from urllib.parse import urlparse
   from colorama import Fore, Style

4. When port_scan.py imported, IT imports:
   import socket
   import threading
   from colorama import Fore, Style

5. When password_test.py imported, IT imports:
   import re
   from colorama import Fore, Style

6. When report.py imported, IT imports:
   import datetime
   import os
   from pathlib import Path

Result: All dependencies loaded, ready to use
```

---

## 💡 Key Design Patterns

### 1. **Modular Architecture**
- Each scanner is independent in its own module
- Each returns consistent (score, findings) tuple
- Easy to add new scanners without modifying core

### 2. **Color-Coded Output**
- Uses colorama for cross-platform compatibility
- Green = Good/Pass
- Yellow = Warning/Caution
- Red = Critical/Fail

### 3. **Threading for Efficiency**
- Port scanner uses threads for concurrent scanning
- Scans 17 ports simultaneously (not sequentially)
- 2-second timeout per thread

### 4. **Regex Pattern Matching**
- Password validation uses proven regex patterns
- Security header checks use string matching
- Port identification uses known port-service mapping

### 5. **Timestamped Reports**
- Every report has unique timestamp filename
- Enables historical tracking of security posture
- Automated organization in reports/ folder

---

## 🔐 Security Considerations

### Input Validation
- Sanitize URLs before sending requests
- Validate domain names before port scanning
- Mask passwords in output (not displayed)

### Error Handling
- Timeouts on all network operations
- Try-catch blocks on file operations
- Graceful handling of unreachable hosts

### Ethical Use
- Built-in disclaimers at startup
- Requires explicit user action for each scan
- Not automated without user initiation
- Terms of service warnings included

---

## 🚀 Execution Paths

### Path 1: Direct Python Execution
```bash
python C:\Programming\RTRP\simsecure\simsecure.py password "test"
```

### Path 2: Batch File Wrapper (Windows)
```bash
simsecure password "test"
# (if C:\Windows\System32\simsecure.bat installed)
```

### Path 3: Unix Wrapper Script
```bash
simsecure password "test"
# (if /usr/local/bin/simsecure configured)
```

### Path 4: Interactive Mode
```bash
simsecure
# Displays menu, user selects option
```

### Path 5: Pip Package Install
```bash
pip install -e C:\Programming\RTRP\simsecure
simsecure web https://example.com
```

---

## 📊 Quick Reference Table

| File | Type | Size | Purpose | Language |
|------|------|------|---------|----------|
| simsecure.py | Code | 14 KB | Main CLI entry point | Python |
| modules/web_scan.py | Code | 6 KB | Website security analysis | Python |
| modules/port_scan.py | Code | 4.6 KB | Network port scanning | Python |
| modules/password_test.py | Code | 4.6 KB | Password strength analysis | Python |
| modules/report.py | Code | 4 KB | Report generation | Python |
| simsecure.bat | Script | 663 B | Windows command wrapper | Batch |
| simsecure | Script | 1.2 KB | Unix wrapper script | Bash |
| setup.py | Config | 1.8 KB | Pip package metadata | Python |
| requirements.txt | Config | 50 B | Python dependencies | Text |
| install_global.bat | Script | 1.5 KB | Windows installer | Batch |
| *.md (11 files) | Docs | 40+ KB | Documentation | Markdown |

---

## 🎯 File Usage Scenarios

### Scenario 1: First-Time User
1. Read: README.md
2. Install: INSTALL.md
3. Try: QUICK_START.md
4. Reference: HOW_TO_USE.md

### Scenario 2: System Administrator
1. Read: PROJECT_SUMMARY.md
2. Global Setup: SETUP_GLOBAL.md OR GLOBAL_INSTALL.md
3. Deploy: install_global.bat (Windows) or shell commands (Unix)
4. Monitor: Use with --report flag regularly

### Scenario 3: Security Auditor
1. Install SimSecure
2. Use: HOW_TO_USE.md for professional scenarios
3. Generate Reports: --report flag for all scans
4. Store: Reports auto-saved in reports/ folder
5. Archive: Copy reports for compliance

### Scenario 4: Developer
1. Read: PROJECT_SUMMARY.md
2. Explore: simsecure.py source code
3. Extend: Add new module following pattern
4. Test: Run existing modules individually

---

## ✅ File Checklist

**Core Application** ✓
- [ ] simsecure.py - Main tool
- [ ] simsecure.bat - Windows wrapper
- [ ] simsecure - Unix wrapper
- [ ] setup.py - Package config

**Modules** ✓
- [ ] modules/__init__.py - Package init
- [ ] modules/web_scan.py - Website scanner
- [ ] modules/port_scan.py - Port scanner
- [ ] modules/password_test.py - Password analyzer
- [ ] modules/report.py - Report generator

**Configuration** ✓
- [ ] requirements.txt - Dependencies
- [ ] install_global.bat - Windows installer

**Documentation** (11 files) ✓
- [ ] README.md - Welcome/quick intro
- [ ] INSTALL.md - Installation guide
- [ ] QUICK_START.md - Quick reference
- [ ] INSTALL_AND_USE.md - Combined guide
- [ ] HOW_TO_USE.md - Detailed guide
- [ ] GLOBAL_INSTALL.md - Global setup
- [ ] SETUP_GLOBAL.md - Global reference
- [ ] GLOBAL_SETUP_COMPLETE.md - Setup complete
- [ ] PROJECT_SUMMARY.md - Project overview
- [ ] summary_of_simsecure.md - Complete reference

---

## 🔗 File Relationships Summary

```
End User
    ↓
[Command Input]
    ↓
simsecure.py
    ├→ Parses arguments
    ├→ Imports from modules/
    ├→ Calls appropriate scanner
    ├→ Receives (score, findings)
    ├→ Displays with colors (colorama)
    └→ Optional: Report generation
        ├→ Calls report.py
        ├→ Creates timestamped file
        └→ Saves to reports/
            ├→ scan_report_web_[time].txt
            ├→ scan_report_port_[time].txt
            └→ scan_report_password_[time].txt

Installation:
    ├→ setup.py (pip install)
    ├→ requirements.txt (dependencies)
    ├→ install_global.bat (Windows automation)
    └→ Documentation files (guides)
```

---

## 📝 Complete File Inventory

**Total Files**:
- 1 Main script (simsecure.py)
- 5 Module files (modules/)
- 2 Wrapper scripts (Windows/Unix)
- 1 Package configuration (setup.py)
- 11 Documentation files (.md)
- 1 Dependency file (requirements.txt)
- 1 Installation script (install_global.bat)
- Auto-generated: __pycache__/, reports/, .egg-info/

**Total Lines of Code**: ~3,500 lines
**Total Documentation**: ~40+ KB in markdown files
**External Dependencies**: 2 (requests, colorama)
**Built-in Module Imports**: 10+ (argparse, sys, os, datetime, re, socket, threading, urllib, pathlib, etc.)

---

**End of Complete Architecture Map**

This document provides complete visibility into every file, its purpose, and how everything works together. For specific questions about any file, refer to the section above or check the file directly in the simsecure folder.
