# 🔒 Global Installation Guide (Like Nmap)

## Make SimSecure Work From Anywhere

Just like Nmap, you can install SimSecure so it works from any terminal directory.

---

## Windows Installation

### Method 1: Add to System PATH (Recommended)

**Step 1: Copy the batch file**
```cmd
# Copy simsecure.bat to a system folder
copy C:\Programming\RTRP\simsecure\simsecure.bat C:\Windows\System32\simsecure.bat
```

**Step 2: Verify it works**
```cmd
# From ANY directory, try:
simsecure -ls
```

Output:
```
=== AVAILABLE SECURITY CHECKS ===

1. Website Security Scanner
2. Port Scanner
3. Password Strength Tester
```

---

### Method 2: Add to Custom PATH Location

**Step 1: Create a custom folder** (optional but cleaner)
```cmd
mkdir C:\Tools
cd C:\Tools
```

**Step 2: Copy the batch file**
```cmd
copy C:\Programming\RTRP\simsecure\simsecure.bat C:\Tools\simsecure.bat
```

**Step 3: Add to Windows PATH**

1. Open Settings → Search for "Environment Variables"
2. Click "Edit the system environment variables"
3. Click "Environment Variables..." button
4. Under "System variables", find "Path" and click "Edit"
5. Click "New" and add: `C:\Tools`
6. Click OK on all dialogs
7. **Restart your terminal/PowerShell**

**Step 4: Test**
```cmd
simsecure -ls
```

---

### Method 3: Quick Alias (PowerShell Only)

```powershell
# Add to your PowerShell profile
Add-Content $PROFILE "Set-Alias simsecure 'C:\Programming\RTRP\simsecure\simsecure.bat'"

# Reload profile
. $PROFILE

# Now use it
simsecure -ls
```

---

## Linux/macOS Installation

### Method 1: System-Wide (Recommended)

**Step 1: Copy to /usr/local/bin**
```bash
sudo cp /path/to/simsecure/simsecure /usr/local/bin/simsecure
```

**Step 2: Make it executable**
```bash
sudo chmod +x /usr/local/bin/simsecure
```

**Step 3: Update the script with correct path**
```bash
# Edit the script
sudo nano /usr/local/bin/simsecure

# Change SIMSECURE_PATH to your actual path
# For example: SIMSECURE_PATH="/path/to/simsecure"
```

**Step 4: Test from anywhere**
```bash
simsecure -ls
```

---

### Method 2: User-Only Installation

```bash
# Create personal bin folder
mkdir -p ~/bin

# Copy and make executable
cp /path/to/simsecure/simsecure ~/bin/simsecure
chmod +x ~/bin/simsecure

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc

# Reload shell
source ~/.bashrc

# Test
simsecure -ls
```

---

## Usage After Global Installation

Once installed globally, use from **ANY directory**:

```bash
# From home directory
cd ~
simsecure -ls

# From Desktop
cd Desktop
simsecure password "test123"

# From any project
cd /my/project
simsecure web https://example.com
```

---

## Verification

### Windows
```cmd
# Check if simsecure is in PATH
where simsecure

# Should show:
# C:\Windows\System32\simsecure.bat

# Or test directly
simsecure --version
```

### Linux/macOS
```bash
# Check if simsecure is in PATH
which simsecure

# Should show:
# /usr/local/bin/simsecure

# Or test directly
simsecure --version
```

---

## Global Usage Examples

Now you can use it like Nmap from anywhere:

### List All Commands
```bash
$ simsecure -ls

=== AVAILABLE SECURITY CHECKS ===

1. Website Security Scanner
2. Port Scanner
3. Password Strength Tester
```

### Test Password (From Anywhere)
```bash
$ cd Desktop
$ simsecure password "MyPass#2026"

[*] Analyzing Password Strength
Security Score: 10/10
```

### Scan Website (From Anywhere)
```bash
$ cd Documents
$ simsecure web https://example.com

[*] Scanning Website: https://example.com
Security Score: 7/10
```

### Scan Ports (From Anywhere)
```bash
$ cd /home/user
$ simsecure port example.com

[*] Scanning Ports on: example.com
Security Score: 6/10
```

---

## Troubleshooting

### Windows: "simsecure not found"

**Solution 1: Verify PATH**
```cmd
# Check if in PATH
echo %PATH%

# If C:\Windows\System32 is there, copy the .bat file
copy C:\Programming\RTRP\simsecure\simsecure.bat C:\Windows\System32\
```

**Solution 2: Use full path temporarily**
```cmd
C:\Programming\RTRP\simsecure\simsecure.bat -ls
```

**Solution 3: Restart terminal**
```cmd
# Close and reopen Command Prompt or PowerShell
```

---

### Linux/macOS: "simsecure not found"

**Solution:** Make sure it's in PATH
```bash
# Check PATH
echo $PATH

# Add to PATH if needed
export PATH="/usr/local/bin:$PATH"

# Make permanent by adding to ~/.bashrc
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

### "Python not found" Error

**Solution:** Update the script path
```bash
# Edit the script
sudo nano /usr/local/bin/simsecure

# Make sure SIMSECURE_PATH points to correct location
# Example: SIMSECURE_PATH="/home/user/simsecure"
```

---

## Comparison: Before vs After

### Before Installation (Navigate Required)
```bash
cd C:\Programming\RTRP\simsecure
python simsecure.py password "test"
```

### After Global Installation (Works Anywhere!)
```bash
# From any directory
simsecure password "test"
simsecure web https://example.com
simsecure port example.com
```

---

## Professional Workflow

Once installed globally, create professional security workflows:

```bash
# Security audit script
#!/bin/bash
echo "Starting security audit..."
simsecure password "AdminPass#2026" --report
simsecure web https://company.com --report
simsecure port company-server --report
echo "Done! Reports in simsecure/reports/"
```

---

## Add to Cron/Scheduled Tasks

### Linux/macOS: Cron Job
```bash
# Edit crontab
crontab -e

# Add this line (weekly security check)
0 9 * * 1 simsecure port company-server --report
```

### Windows: Task Scheduler
```batch
# Create scheduled task
schtasks /create /tn "SimSecure Weekly" /tr "simsecure port server --report" /sc WEEKLY
```

---

## Summary

| Platform | Command | Location |
|----------|---------|----------|
| **Windows** | `simsecure -ls` | `C:\Windows\System32\simsecure.bat` |
| **Linux** | `simsecure -ls` | `/usr/local/bin/simsecure` |
| **macOS** | `simsecure -ls` | `/usr/local/bin/simsecure` |

---

## Next Steps

1. Choose your installation method above
2. Copy/install the script to the appropriate location
3. Restart your terminal
4. Test: `simsecure -ls`
5. Use from anywhere!

---

**Now SimSecure works globally like Nmap!** 🚀

Just type `simsecure` from any terminal and it works! 🔒
