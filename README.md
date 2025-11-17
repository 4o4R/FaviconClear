# Favicon Cache Cleaner  
_Clear browser favicon data to mitigate “supercookie” tracking techniques_

This tool provides a **single, cross-platform launcher** (macOS + Windows) that removes browser favicon databases used for persistent tracking, including the technique demonstrated in:

- **Inspired by:** https://news.ycombinator.com/item?id=45947770  
- **Countermeasure to:** https://github.com/jonasstrehle/supercookie

The favicon-based “supercookie” exploit stores a unique ID inside your browser's cached favicon database. Because browsers rarely delete these files—and often recreate them automatically—sites can identify users across sessions, private-mode windows, and even after typical cache clears.

This script reliably removes those underlying database files for **Chrome**, **Firefox**, and **Safari (macOS)**, across all profiles it can discover, forcing browsers to regenerate clean caches.

---

## Features

- **Cross-platform**: Works on macOS and Windows.
- **Multi-browser**: Chrome, Firefox, Safari (macOS only).
- **Profile-aware**: Detects and cleans all available profiles.
- **Safe**: Only removes favicon database files or Safari's favicon cache directory; browsers rebuild them automatically.
- **Portable**: Single `python` file, no external dependencies.
- **Transparent**: Detailed logging of each deleted file/path.

---

## Why This Exists

Websites can store a persistent identifier inside your browser’s **favicon cache**. This “supercookie” technique works because:

- Browsers store icons in SQLite databases (Chrome/Firefox) or directories (Safari).
- These favicon caches often survive:
  - Normal cache clears  
  - Private browsing sessions  
  - Incognito tabs  
  - Even some full history deletions  
- The data is not isolated by site and is rarely purged.

By periodically deleting these favicon databases, you eliminate the data required for this persistence layer, reducing the ability of a site to re-identify you.

---

## Supported Browsers

### macOS
- Google Chrome (all profiles)
- Mozilla Firefox (all profiles)
- Safari (removes entire `Favicon Cache` directory)

### Windows
- Google Chrome (all profiles)
- Mozilla Firefox (all profiles)

---

## Usage

### Requirements
- Python 3.8+  
- Permissions to read/write your browser profile directories

### Running
```bash
python clear_favicon_cache.py
```

### Double-click / one-click operation
- **Windows**: Create a `.bat` file or shortcut pointing to Python.
- **macOS**: Wrap with an Automator “Application” to integrate with Launchpad.

---

## How It Works

The script looks for known favicon storage locations and deletes only:

### Chrome
- `Favicons`
- `Favicons-journal`
- Any `Favicons*` files under profile directories

### Firefox
- `favicons.sqlite`
- `favicons.sqlite-shm`
- `favicons.sqlite-wal`

### Safari (macOS)
- Entire `~/Library/Safari/Favicon Cache` directory

All browsers re-create these structures automatically upon next launch.

---

## Code

See [`clear_favicon_cache.py`](./clear_favicon_cache.py) for the full script.  
It includes extensive inline documentation explaining every line and decision.

---

## Security Notes

- This script does **not** interfere with bookmarks, history, or cookies.  
- It only removes favicon cache files that can regenerate without data loss.  
- It does **not** attempt to modify browser configurations or privacy settings.

For maximum protection, consider running this script:

- At system startup  
- Daily or weekly via cron / Task Scheduler  
- Before and after sensitive browsing  

---

## Roadmap

- Optional “dry run” mode  
- Linux support  
- Auto-packaging into:
  - macOS app bundle  
  - Windows executable  
- Optional system service for periodic cleanup  
- Browser-specific hardening recommendations  

---

## License

MIT License.  
Contributions are welcome.
