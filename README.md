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
   - Download **Python 3**
   - IMPORTANT: check the box **“Add Python to PATH”**
   - Finish install.

### 2. Put the Script in an Easy Folder
Create a folder:

```
C:\FaviconCleaner\
```

Move `clear_favicon_cache.py` into that folder.

### 3. Create a One‑Click Launcher
1. Open **Notepad**
2. Paste:

```bat
@echo off
python "%~dp0clear_favicon_cache.py"
pause
```

3. Save as:

```
C:\FaviconCleaner\run_cleaner.bat
```
(Make sure “Save as type” is **All Files**, not .txt.)

### 4. Run It
Double‑click:

```
run_cleaner.bat
```

A window will open, run the cleaner, display results, and wait for ENTER.

### Optional: Create Desktop Shortcut
Right‑click `run_cleaner.bat` → **Send to Desktop**.

---

## macOS: Step‑by‑Step Instructions

### 1. Check Python
Open **Terminal** and run:

```bash
python3 --version
```

If Python 3 appears, continue.  
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

Move `clear_favicon_cache.py` into it.

### 3. Run the Script
```bash
cd ~/FaviconCleaner
python3 clear_favicon_cache.py
```

### Optional: Create a Clickable macOS App
1. Open **Automator**
2. Choose **Application**
3. Add **Run Shell Script**
4. Paste:

```bash
/usr/bin/env python3 "$HOME/FaviconCleaner/clear_favicon_cache.py"
```

5. Save as:

```
Favicon Cleaner.app
```

Place it in Applications or Desktop.

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

You can download the full script here:

**[Download clear_favicon_cache.py](sandbox:/mnt/data/clear_favicon_cache.py)**

(If you need it zipped, I can generate that too.)

---

# Security Notes

- Does not modify cookies, bookmarks, or history
- Only deletes cache files that browsers safely rebuild
- Safeguards against “favicon supercookie” tracking vectors

---

# License

MIT License — free for personal and commercial use.
