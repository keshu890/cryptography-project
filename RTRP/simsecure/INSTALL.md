# SimSecure Installation Guide

## Professional Installation (System-Wide)

SimSecure can be installed as a system-wide command-line tool, just like professional cybersecurity tools such as Nmap.

---

## Installation Methods

### Method 1: Install from Source (Recommended for Development)

```bash
# Navigate to project directory
cd C:\Programming\RTRP\simsecure

# Install in development mode
pip install -e .

# On Linux/macOS with sudo
sudo pip install -e .
```

### Method 2: Install as Package

```bash
# Install the package
pip install .

# On Linux/macOS with sudo
sudo pip install .
```

### Method 3: Install from Cloned Repository

```bash
# Clone the repository (if applicable)
git clone <repository-url>
cd simsecure

# Install dependencies
pip install -r requirements.txt

# Install the tool
pip install .
```

---

## Verification

After installation, verify SimSecure is installed correctly:

```bash
# Check if simsecure command is available
simsecure --version

# Should output: SimSecure v1.0
```

---

## Usage After Installation

Once installed, you can use SimSecure from anywhere in your terminal:

### Interactive Menu Mode
```bash
# Run with no arguments to get interactive menu
simsecure
```

### List Available Commands
```bash
# Show all available security checks
simsecure -ls
```

### Command-Line Mode
```bash
# Website security scan
simsecure web https://example.com --report

# Port scan
simsecure port example.com --report

# Password strength test
simsecure password "MyPassword#123" --report
```

---

## System Requirements

- Python 3.7 or higher
- pip (Python package manager)
- pip or conda installed
- Internet connection (for web scanning)

### Check Python Version
```bash
python --version
# or
python3 --version
```

### Check pip Installation
```bash
pip --version
# or
pip3 --version
```

---

## Installation on Different Systems

### Windows

1. **Open Command Prompt or PowerShell**
2. **Navigate to SimSecure folder:**
   ```powershell
   cd C:\Programming\RTRP\simsecure
   ```

3. **Install:**
   ```powershell
   pip install -e .
   ```

4. **Use from anywhere:**
   ```powershell
   simsecure -ls
   simsecure web https://example.com
   ```

### Linux / macOS

1. **Open Terminal**
2. **Navigate to SimSecure folder:**
   ```bash
   cd /path/to/simsecure
   ```

3. **Install with sudo (system-wide):**
   ```bash
   sudo pip install -e .
   ```
   
   **Or install for current user only:**
   ```bash
   pip install -e .
   ```

4. **Use from anywhere:**
   ```bash
   simsecure -ls
   simsecure web https://example.com
   ```

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Linux/macOS:
source venv/bin/activate

# Install SimSecure
pip install -e .

# Use SimSecure (within activated environment)
simsecure -ls
```

---

## Troubleshooting

### Issue: "simsecure command not found"

**Solution:**
```bash
# Reinstall the package
pip install -e .

# Or install globally with sudo (Linux/macOS)
sudo pip install -e .

# Check if pip Scripts folder is in PATH
python -m site
```

### Issue: "No module named 'simsecure'"

**Solution:**
```bash
# Make sure you're in the correct directory
cd /path/to/simsecure

# Reinstall
pip install -e .

# Verify installation
pip list | grep simsecure
```

### Issue: Permission Denied

**Solution (Linux/macOS):**
```bash
# Install with sudo
sudo pip install -e .

# Or install for user only
pip install --user -e .
```

### Issue: Python not found

**Solution:**
```bash
# Use python3 explicitly
python3 -m pip install -e .

# Then use
python3 -m simsecure -ls
```

---

## Uninstall

To remove SimSecure from your system:

```bash
pip uninstall simsecure
```

---

## Entry Points

The installation creates the following entry point:

```
console_scripts:
  simsecure -> simsecure:main
```

This means the `simsecure` command is available globally after installation.

---

## Development Installation

For developers who want to contribute:

```bash
# Install in editable/development mode
pip install -e .

# Install with development dependencies (if available)
pip install -e ".[dev]"

# Make changes and they're immediately reflected
```

---

## Location of Installed Package

After installation, find where SimSecure is installed:

```bash
# Windows
pip show simsecure

# Linux/macOS
python -c "import simsecure; print(simsecure.__file__)"
```

Output example:
```
Name: simsecure
Version: 1.0.0
Location: C:\Users\<user>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages
```

---

## Configuration

After installation, configuration files (if needed) can be stored in:

- **Windows:** `%APPDATA%\simsecure\`
- **Linux/macOS:** `~/.simsecure/`

---

## Support & Documentation

For help using SimSecure after installation:

```bash
# Show help menu
simsecure -h

# Show all available commands
simsecure -ls

# Show legal disclaimer
simsecure disclaimer

# Interactive menu
simsecure
```

---

## Next Steps

After installation, try these commands:

```bash
# 1. Test with interactive menu
simsecure

# 2. List all commands
simsecure -ls

# 3. Test password strength
simsecure password "TestPass#123"

# 4. Scan ports
simsecure port localhost

# 5. Scan website
simsecure web https://httpbin.org --report

# 6. View reports
cd reports
cat scan_report_*.txt
```

---

## Notes

- Reports are saved in the `reports/` subfolder
- Each report has a timestamp in the filename
- The tool requires internet for website scanning
- Port scanning may require elevated privileges for ports < 1024
- Use `--report` flag to save security findings

---

**SimSecure v1.0 - Professional Cybersecurity Command-Line Tool**

Installation complete! You can now use SimSecure from anywhere in your terminal. 🔒
