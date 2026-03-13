# 🚀 SimSecure - Global Installation Complete!

## Now Works Like Nmap!

SimSecure can now work globally, just like professional security tools like Nmap.

---

## 🔧 How It Works Globally

The tool now has a batch file wrapper (`simsecure.bat`) that can be installed to be accessible from anywhere.

---

## ⚡ Windows - Global Setup (Quick)

### Option 1: Using Install Script (Easiest)

1. **Navigate to SimSecure folder:**
   ```cmd
   cd C:\Programming\RTRP\simsecure
   ```

2. **Right-click `install_global.bat`**

3. **Select "Run as administrator"**

4. **Wait for success message**

5. **Open new terminal and test:**
   ```cmd
   simsecure -ls
   ```

✅ Done! Now works from anywhere!

---

### Option 2: Manual Installation

1. **Get admin access to Command Prompt**
   - Press `Win + X`
   - Select "Command Prompt (Admin)" or "Terminal (Admin)"

2. **Copy the batch file to System32:**
   ```cmd
   copy "C:\Programming\RTRP\simsecure\simsecure.bat" "C:\Windows\System32\simsecure.bat"
   ```

3. **Test:**
   ```cmd
   simsecure -ls
   ```

---

## 🐧 Linux - Global Setup

```bash
# Copy to system bin directory
sudo cp /path/to/simsecure/simsecure /usr/local/bin/simsecure

# Make executable
sudo chmod +x /usr/local/bin/simsecure

# Edit to set correct path
sudo nano /usr/local/bin/simsecure

# Change SIMSECURE_PATH to your path
# Example: SIMSECURE_PATH="/home/user/simsecure"

# Test
simsecure -ls
```

---

## 🍎 macOS - Global Setup

```bash
# Copy to system bin directory
sudo cp /path/to/simsecure/simsecure /usr/local/bin/simsecure

# Make executable
sudo chmod +x /usr/local/bin/simsecure

# Edit to set correct path
sudo nano /usr/local/bin/simsecure

# Change SIMSECURE_PATH to your path
# Example: SIMSECURE_PATH="$HOME/simsecure"

# Test
simsecure -ls
```

---

## ✅ Verification Commands

### Windows
```cmd
# Should work from any folder
cd Desktop
simsecure -ls

cd Documents
simsecure password "test123"

cd Downloads
simsecure web https://example.com
```

### Linux/macOS
```bash
# Should work from any folder
cd ~
simsecure -ls

cd /tmp
simsecure password "test123"

cd /usr/local
simsecure port example.com
```

---

## 🎯 Usage Examples (Global)

Now you can use it like Nmap from anywhere!

### List All Commands
```bash
$ simsecure -ls

=== AVAILABLE SECURITY CHECKS ===

1. Website Security Scanner
2. Port Scanner
3. Password Strength Tester
```

### Interactive Menu
```bash
$ simsecure
# Shows menu to select security checks
```

### Test Password From Anywhere
```bash
$ pwd
/home/user/Desktop

$ simsecure password "MyPass#2026"

[*] Analyzing Password Strength
Security Score: 10/10 ✓
```

### Scan Website From Anywhere
```bash
$ pwd
/home/user/Documents

$ simsecure web https://example.com --report

[*] Scanning Website: https://example.com
Security Score: 7/10
[+] Report saved!
```

### Scan Ports From Anywhere
```bash
$ pwd  
C:\Users\User\Downloads

$ simsecure port example.com

[*] Scanning Ports on: example.com
Security Score: 6/10
```

---

## 📋 Global Commands Reference

| Task | Command | Works Globally |
|------|---------|---|
| Interactive menu | `simsecure` | ✅ Yes |
| List commands | `simsecure -ls` | ✅ Yes |
| Show help | `simsecure -h` | ✅ Yes |
| Test password | `simsecure password "Pass"` | ✅ Yes |
| Scan website | `simsecure web https://ex.com` | ✅ Yes |
| Scan ports | `simsecure port example.com` | ✅ Yes |
| Save report | Add `--report` flag | ✅ Yes |

---

## 🎓 Professional Workflows (Now Possible)

### Security Audit from Any Directory

```bash
# From home
cd ~
simsecure password "AdminPass#2026" --report

# From projects  
cd ~/projects
simsecure web https://company.com --report

# From downloads
cd ~/Downloads
simsecure port company-server --report

# From anywhere
cd /any/path
simsecure -ls
```

---

### Automated Scheduled Checks

#### Windows - Task Scheduler
```batch
:: Create weekly security check
schtasks /create /tn "SimSecure Weekly" ^
  /tr "simsecure port myserver --report" ^
  /sc WEEKLY /d MON /st 09:00
```

#### Linux/macOS - Cron Job
```bash
# Edit crontab
crontab -e

# Add: Run every Monday at 9 AM
0 9 * * 1 simsecure port company-server --report
```

---

### Batch Processing Multiple Targets

```bash
#!/bin/bash
# Audit multiple servers

targets=(
  "server1.company.com"
  "server2.company.com"
  "api.company.com"
  "db.company.com"
)

for target in "${targets[@]}"; do
  echo "Scanning $target..."
  simsecure port "$target" --report
  simsecure web "https://$target" --report
done

echo "All scans complete!"
```

---

## 📂 File Locations

### Windows
- **Batch file:** `C:\Programming\RTRP\simsecure\simsecure.bat`
- **Install location:** `C:\Windows\System32\simsecure.bat`
- **Reports:** `C:\Programming\RTRP\simsecure\reports\`

### Linux
- **Script file:** `/path/to/simsecure/simsecure`
- **Install location:** `/usr/local/bin/simsecure`
- **Reports:** `/path/to/simsecure/reports/`

### macOS
- **Script file:** `/path/to/simsecure/simsecure`
- **Install location:** `/usr/local/bin/simsecure`
- **Reports:** `/path/to/simsecure/reports/`

---

## 🔧 Troubleshooting Global Installation

### Windows: "simsecure not found"

**Quick Fix:**
```cmd
# Run the install script again
cd C:\Programming\RTRP\simsecure
install_global.bat
```

**Manual Fix:**
```cmd
# Copy manually with admin
copy simsecure.bat C:\Windows\System32\

# Or add to PATH
echo C:\Programming\RTRP\simsecure >> %PATH%
```

---

### Linux/macOS: "simsecure: command not found"

**Check Installation:**
```bash
ls -la /usr/local/bin/simsecure
which simsecure
```

**Fix Path Variable:**
```bash
# Edit the script
sudo nano /usr/local/bin/simsecure

# Update SIMSECURE_PATH
# It should point to where simsecure.py is
```

---

## 🌟 Features of Global Installation

✅ Works from ANY directory
✅ Works from ANY terminal/PowerShell
✅ Works in scripts and automation
✅ Works in scheduled tasks/cron jobs
✅ Works like professional tools (Nmap, etc.)
✅ No need to navigate to installation folder
✅ Professional-grade security tool

---

## 🎉 Comparison

### Before Global Installation
```bash
# Had to navigate
cd C:\Programming\RTRP\simsecure
python simsecure.py password "test"
```

### After Global Installation
```bash
# Works from anywhere!
simsecure password "test"

# No navigation needed!
# Works on Desktop, Documents, anywhere!
```

---

## 🚀 Next Steps

1. **Install Globally:**
   - Windows: Run `install_global.bat` as admin
   - Linux/macOS: Follow setup steps above

2. **Test It:**
   ```bash
   simsecure -ls
   ```

3. **Use from Anywhere:**
   ```bash
   cd Desktop
   simsecure password "test123"
   
   cd Downloads
   simsecure web https://example.com
   ```

4. **Save Reports:**
   ```bash
   simsecure port example.com --report
   ```

---

## 📖 Documentation Files

- `SETUP_GLOBAL.md` - Quick setup guide
- `GLOBAL_INSTALL.md` - Detailed installation
- `HOW_TO_USE.md` - Professional usage
- `QUICK_START.md` - 5-minute intro

---

## 💡 Pro Tips

✅ Add to scripts for automation
✅ Create scheduled security audits
✅ Use in CI/CD pipelines
✅ Monitor multiple servers
✅ Generate compliance reports
✅ Integrate with monitoring tools

---

## 🎓 Example: Weekly Security Audit Script

```bash
#!/bin/bash
# weekly_security_audit.sh

echo "Starting weekly security audit..."
echo "Generated: $(date)" > audit_report.txt

# Check critical servers
echo "Checking servers..." >> audit_report.txt
simsecure port prod-server --report >> audit_report.txt
simsecure port db-server --report >> audit_report.txt

# Check websites
echo "Checking websites..." >> audit_report.txt
simsecure web https://company.com --report >> audit_report.txt

# Check policies
echo "Checking policies..." >> audit_report.txt
simsecure password "RequiredPolicy#123" --report >> audit_report.txt

echo "Audit complete!"
cat audit_report.txt
```

---

**SimSecure is now globally installed!** 🌍

Use `simsecure` from anywhere, just like Nmap! 🚀

Start with: `simsecure -ls` 🔒
