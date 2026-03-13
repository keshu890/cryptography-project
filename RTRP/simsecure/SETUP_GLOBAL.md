# ⚡ Quick Global Setup (2 Minutes)

## Make SimSecure Work Like Nmap

Use `simsecure` from ANY terminal, from ANY directory - just like Nmap!

---

## 🪟 Windows (3 Steps)

### Step 1: Right-Click to Run as Administrator

Navigate to: `C:\Programming\RTRP\simsecure`

**Right-click** on `install_global.bat`

Select **"Run as administrator"**

### Step 2: Wait for Installation

The script will:
- Copy SimSecure to system commands
- Show success message
- Run a test

### Step 3: Test It!

Open a **new** terminal and type:
```cmd
simsecure -ls
```

**Boom! 🎉 It works from anywhere!**

---

## 🐧 Linux / 🍎 macOS (3 Steps)

### Step 1: Copy the Script
```bash
sudo cp ~/simsecure/simsecure /usr/local/bin/simsecure
```

### Step 2: Make it Executable
```bash
sudo chmod +x /usr/local/bin/simsecure
```

### Step 3: Edit the Path
```bash
sudo nano /usr/local/bin/simsecure
```

Find this line:
```bash
SIMSECURE_PATH="/path/to/simsecure"
```

Change it to your actual path. For example:
```bash
SIMSECURE_PATH="/home/user/simsecure"
# or
SIMSECURE_PATH="/opt/simsecure"
```

Save and exit (Ctrl+O, Enter, Ctrl+X)

### Step 4: Test It!
```bash
simsecure -ls
```

**Done! 🎉**

---

## ✅ Verification

### Windows
```cmd
$ simsecure --version
SimSecure v1.0

$ simsecure -ls
=== AVAILABLE SECURITY CHECKS ===
1. Website Security Scanner
2. Port Scanner
3. Password Strength Tester
```

### Linux/macOS
```bash
$ simsecure --version
SimSecure v1.0

$ simsecure -ls
=== AVAILABLE SECURITY CHECKS ===
1. Website Security Scanner
2. Port Scanner
3. Password Strength Tester
```

---

## 🎯 Now Use It From Anywhere!

```bash
# Test password from home directory
cd ~
simsecure password "MyPass#2026"

# Scan website from Desktop
cd Desktop
simsecure web https://example.com

# Scan ports from any folder
simsecure port example.com
```

---

## 📋 All Commands (Work Globally Now)

```bash
simsecure                              # Interactive menu
simsecure -ls                          # List all commands
simsecure -h                           # Show help
simsecure password "YourPass#123"      # Test password
simsecure web https://example.com      # Scan website
simsecure port example.com             # Scan ports
simsecure --report                     # Add --report flag to save
```

---

## 🔧 Troubleshooting

### Windows: Still Can't Find Command?

1. **Check if install worked:**
   ```cmd
   dir C:\Windows\System32 | findstr simsecure
   ```

2. **Manual PATH setup:**
   - Search for "Environment Variables" on Windows
   - Edit System PATH to include: `C:\Programming\RTRP\simsecure`
   - Restart terminal

### Linux/macOS: Command Not Found?

1. **Check if installed:**
   ```bash
   which simsecure
   ```

2. **Update the path in script:**
   ```bash
   sudo nano /usr/local/bin/simsecure
   # Update SIMSECURE_PATH to correct location
   ```

---

## 🚀 Success Indicators

✅ Can type `simsecure` from any folder
✅ Returns security checks list with `-ls` flag
✅ Works from Desktop, Documents, etc.
✅ No need to navigate to installation folder
✅ Works just like Nmap!

---

## 📝 Examples After Global Setup

### From Home Directory
```bash
$ cd ~
$ simsecure web https://github.com
[*] Scanning Website: https://github.com
Security Score: 8/10
```

### From Desktop
```bash
$ cd Desktop
$ simsecure password "AdminPass#2026" --report
[*] Analyzing Password Strength
Security Score: 10/10
[+] Report saved to: reports/scan_report_PASSWORD_*.txt
```

### From Project Directory
```bash
$ cd /my/project
$ simsecure port myserver.local
[*] Scanning Ports on: myserver.local
Security Score: 6/10
```

---

## ⚡ Now You Can:

✅ Use simsecure from ANY terminal
✅ Use simsecure from ANY directory  
✅ Use simsecure just like Nmap
✅ Add to scripts and automation
✅ Schedule regular security checks
✅ Run from cron jobs (Linux/macOS)

---

## 🎓 Next: Create Automation

### Windows Scheduled Task
```cmd
# Run security check weekly
schtasks /create /tn "SimSecure" /tr "simsecure port server --report" /sc WEEKLY
```

### Linux Cron Job
```bash
# Add to crontab (runs every Monday at 9 AM)
crontab -e

# Add this line:
0 9 * * 1 simsecure port server --report
```

---

**SimSecure is now global!** 🌍

Type `simsecure -ls` from anywhere and it works! 🎉
