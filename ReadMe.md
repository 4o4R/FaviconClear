# Favicon Cache Cleaner  
_Clear browser favicon data to mitigate “supercookie” tracking techniques_

This tool provides a **single, cross-platform launcher** (macOS + Windows) that removes browser favicon databases used for persistent tracking, including the technique demonstrated in:

- **Inspired by:** https://news.ycombinator.com/item?id=45947770  
- **Countermeasure to:** https://github.com/jonasstrehle/supercookie

---

# Quick Start for Windows and macOS Users

## Windows: Step‑by‑Step Instructions

### 1. Install Python (if not already installed)
1. Press **Start** → type **python**.  
   If Python appears, skip to step 2.
2. If not:
   - Visit: https://www.python.org/downloads/windows/
   - Download **Python 3** (Python 2.7 also works if you already have it)
   - IMPORTANT: check the box **“Add Python to PATH”**
   - Finish install.

### 2. Put the Files in an Easy Folder
Create a folder:

```
C:\FaviconCleaner\
```

Move `clear_favicon_cache.py` **and** `run_cleaner.bat` into that folder.

### 3. Run It (Double‑Click)
Double‑click:

```
run_cleaner.bat
```

It tries available Python interpreters automatically (`python`, `python3`, then `py`), runs the cleaner, shows results, and waits for ENTER so you can read the output.

### Optional: Desktop Shortcut
Right‑click `run_cleaner.bat` → **Send to Desktop**.

---

## macOS: Step‑by‑Step Instructions

### 1. Check Python
Open **Terminal** and run:

```bash
python3 --version  # or: python --version
```

If Python appears, continue.  
If not: install via Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

Or download from python.org.

### 2. Create Folder for the Script

```bash
mkdir -p ~/FaviconCleaner
```

Move `clear_favicon_cache.py` **and** `run_cleaner.command` into it.

### 3. Run It (Double‑Click)
Double‑click `run_cleaner.command`. The first time, macOS may ask to confirm running a downloaded file.

If double‑clicking doesn’t start it, make it executable once:

```bash
chmod +x ~/FaviconCleaner/run_cleaner.command
```

### Optional: Run from Terminal
```bash
cd ~/FaviconCleaner
python clear_favicon_cache.py   # or: python3 clear_favicon_cache.py
```

---

# Automate It (Optional)

## Windows: Task Scheduler
Run at logon (good for “after reboot / after browser close”):
1. Open **Task Scheduler** → **Create Basic Task…**
2. Name: “Clear Favicon Cache”
3. Trigger: **When I log on**
4. Action: **Start a program**
   - Program/script: `C:\Windows\System32\cmd.exe`
   - Add arguments: `/c "C:\FaviconCleaner\run_cleaner.bat"`
5. Finish.

Weekly schedule instead:
1. Trigger: **Weekly**
2. Pick day/time → same Action as above.

Note: task runs hidden; check results by running `run_cleaner.bat` manually if needed.

## macOS: launchd (runs at login or weekly)
1. Create the plist:
   ```bash
   cat > ~/Library/LaunchAgents/com.user.faviconcleaner.plist <<'EOF'
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
     <key>Label</key><string>com.user.faviconcleaner</string>
     <key>ProgramArguments</key>
     <array>
       <string>/usr/bin/env</string>
       <string>python</string>
       <string>/Users/$USER/FaviconCleaner/clear_favicon_cache.py</string>
     </array>
     <key>StandardOutPath</key><string>/tmp/faviconcleaner.log</string>
     <key>StandardErrorPath</key><string>/tmp/faviconcleaner.log</string>
     <key>RunAtLoad</key><true/>
     <!-- Weekly: uncomment StartCalendarInterval and remove RunAtLoad if desired -->
     <!-- <key>StartCalendarInterval</key><dict><key>Weekday</key><integer>1</integer><key>Hour</key><integer>9</integer><key>Minute</key><integer>0</integer></dict> -->
   </dict>
   </plist>
   EOF
   ```
2. Load it:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.faviconcleaner.plist
   ```
3. To unload:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.user.faviconcleaner.plist
   ```

For a manual weekly run, use `StartCalendarInterval` (example above: Monday 09:00) and remove `RunAtLoad`.

---

# How It Works

The script removes favicon storage locations used by browsers:

### Chrome
- `Favicons`
- `Favicons-journal`
- All `Favicons*` in Chrome profile folders

### Firefox
- `favicons.sqlite`
- `favicons.sqlite-wal`
- `favicons.sqlite-shm`

### Safari (macOS)
- Entire `~/Library/Safari/Favicon Cache` directory

Browsers automatically recreate these files with clean data.

---

# Download the Script

From the releases. 


---

# Security Notes

- Does not modify cookies, bookmarks, or history
- Only deletes cache files that browsers safely rebuild
- Safeguards against “favicon supercookie” tracking vectors

---

# License

MIT License — free for personal and commercial use.
