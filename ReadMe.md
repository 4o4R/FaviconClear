# Favicon Cache Cleaner  
_Clear browser favicon data to mitigate “supercookie” tracking techniques_

This tool provides a **single, cross-platform launcher** (macOS + Windows) that removes browser favicon databases used for persistent tracking, including the technique demonstrated in:

- **Inspired by:** https://news.ycombinator.com/item?id=45947770  
- **Countermeasure to:** https://github.com/jonasstrehle/supercookie

---

# Quick Start for Windows and macOS Users

## Windows: Step‑by‑Step Instructions

### 1. Install Python (if not already installed)
Python 3 is recommended, but the tool works on Python 2.7+.

1. Press **Start** → type **python**.  
   If Python appears, skip to step 2.
2. If not:
   - Visit: https://www.python.org/downloads/windows/
   - Download **Python (latest 3.x)**
   - IMPORTANT: check **“Add Python to PATH”**
   - Finish install.

### 2. Put the Files in an Easy Folder
Create a folder:

```
C:\FaviconCleaner\
```

Move `clear_favicon_cache.py` **and** `run_cleaner.bat` into that folder.
Be sure to **extract the entire zip first**—keep the .py and .bat in the same folder.

### 3. Run It (Double‑Click)
Double‑click:

```
run_cleaner.bat
```

It tries available Python interpreters automatically (`py -3`, `py -2`, `py`, `python3`, `python`), runs the cleaner, shows results, and waits for ENTER so you can read the output.

### Optional: Desktop Shortcut
Right‑click `run_cleaner.bat` → **Send to Desktop**.

---

## macOS: Step‑by‑Step Instructions

### 1. Check Python
Open **Terminal** and run:

```bash
python --version  # or: python3 --version
```

If a version prints (2.7+ or 3.x), continue.  
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
