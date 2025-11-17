# File: clear_favicon_cache.py
# Folder: Anywhere (e.g., Desktop, C:\Scripts, or ~/scripts)
#
# PURPOSE:
#   This script is a single cross-platform launcher that clears
#   favicon-related caches for:
#       - Google Chrome (all profiles it can find)
#       - Mozilla Firefox (all profiles it can find)
#       - Apple Safari (macOS only)
#
#   It is safe in the sense that it only deletes known cache/database
#   files used for favicons. Browsers will recreate these files.
#
# HOW TO USE:
#   1) Make sure Python 3 is installed.
#   2) Run:
#        macOS:   python3 clear_favicon_cache.py
#        Windows: python   clear_favicon_cache.py
#
#   If you double-click the file on Windows and it's associated with Python,
#   it should also run and show a console window.

import os
import glob
import shutil
import platform
from pathlib import Path


# ------------------------------------------------------------
# Small helper functions
# ------------------------------------------------------------

def log(msg: str) -> None:
    """Print a simple status line."""
    print(msg)


def remove_path(path: Path) -> None:
    """
    Delete either a file or a directory if it exists.

    We use this instead of calling os.remove / shutil.rmtree directly
    so we can:
      - check existence
      - avoid exceptions killing the script
      - reuse the same code for files and folders
    """
    try:
        if not path.exists():
            return

        if path.is_dir():
            # Recursively delete a directory tree.
            shutil.rmtree(path, ignore_errors=True)
            log(f"  removed directory: {path}")
        else:
            # Delete a single file.
            path.unlink(missing_ok=True)  # Python 3.8+: will ignore if missing
            log(f"  removed file     : {path}")
    except Exception as e:
        # We don't stop the script on errors, just report.
        log(f"  [WARN] could not remove {path} ({e})")


def ensure_expanded(path_str: str) -> Path:
    """
    Expand ~ and environment variables and return a Path object.

    This allows us to write paths in a portable way, e.g.:
      "~/Library/..." or "%LOCALAPPDATA%\\..."
    """
    expanded = os.path.expanduser(os.path.expandvars(path_str))
    return Path(expanded)


# ------------------------------------------------------------
# Chrome favicon cleanup
# ------------------------------------------------------------

def clear_chrome_favicons_mac() -> None:
    """
    Clear Chrome favicon databases on macOS.

    Chrome's user data lives under:
        ~/Library/Application Support/Google/Chrome

    Each profile (Default, Profile 1, etc.) is a subfolder.
    Each profile may contain:
        Favicons
        Favicons-journal

    Strategy:
      - Walk all subdirectories under Chrome user data.
      - For each file named 'Favicons' or starting with 'Favicons-',
        remove it.
    """
    base_dir = ensure_expanded("~/Library/Application Support/Google/Chrome")
    if not base_dir.exists():
        log("  Chrome base directory not found (macOS) – skipping.")
        return

    log(f"  scanning Chrome profiles under: {base_dir}")
    # Walk the tree and delete 'Favicons*' files.
    for path in base_dir.rglob("Favicons*"):
        # We only want regular files (not directories)
        if path.is_file():
            remove_path(path)


def clear_chrome_favicons_windows() -> None:
    """
    Clear Chrome favicon databases on Windows.

    Chrome's user data lives under:
        %LOCALAPPDATA%\Google\Chrome\User Data

    Strategy:
      - Walk all subdirectories under User Data.
      - Delete any files named 'Favicons' or starting with 'Favicons-'.
    """
    base_dir = ensure_expanded(r"%LOCALAPPDATA%\Google\Chrome\User Data")
    if not base_dir.exists():
        log("  Chrome base directory not found (Windows) – skipping.")
        return

    log(f"  scanning Chrome profiles under: {base_dir}")
    for path in base_dir.rglob("Favicons*"):
        if path.is_file():
            remove_path(path)


def clear_chrome_favicons() -> None:
    """Dispatch Chrome cleanup based on OS."""
    system = platform.system()
    log("Chrome:")
    if system == "Darwin":
        clear_chrome_favicons_mac()
    elif system == "Windows":
        clear_chrome_favicons_windows()
    else:
        log("  non-macOS/non-Windows system – skipping Chrome.")
    log("")  # blank line for readability


# ------------------------------------------------------------
# Firefox favicon cleanup
# ------------------------------------------------------------

def clear_firefox_favicons_mac() -> None:
    """
    Clear Firefox favicon databases on macOS.

    Firefox profiles are under:
        ~/Library/Application Support/Firefox/Profiles/<profile-name>

    Favicons are stored in:
        favicons.sqlite
        favicons.sqlite-wal
        favicons.sqlite-shm
    """
    profiles_dir = ensure_expanded("~/Library/Application Support/Firefox/Profiles")
    if not profiles_dir.exists():
        log("  Firefox profiles directory not found (macOS) – skipping.")
        return

    log(f"  scanning Firefox profiles under: {profiles_dir}")
    for profile in profiles_dir.iterdir():
        if not profile.is_dir():
            continue
        # Pattern-match the favicon-related sqlite files.
        for pattern in ("favicons.sqlite", "favicons.sqlite-wal", "favicons.sqlite-shm"):
            candidate = profile / pattern
            remove_path(candidate)


def clear_firefox_favicons_windows() -> None:
    """
    Clear Firefox favicon databases on Windows.

    Firefox profiles are under:
        %APPDATA%\Mozilla\Firefox\Profiles\<profile-name>

    Same file names as on macOS.
    """
    profiles_dir = ensure_expanded(r"%APPDATA%\Mozilla\Firefox\Profiles")
    if not profiles_dir.exists():
        log("  Firefox profiles directory not found (Windows) – skipping.")
        return

    log(f"  scanning Firefox profiles under: {profiles_dir}")
    for profile in profiles_dir.iterdir():
        if not profile.is_dir():
            continue
        for pattern in ("favicons.sqlite", "favicons.sqlite-wal", "favicons.sqlite-shm"):
            candidate = profile / pattern
            remove_path(candidate)


def clear_firefox_favicons() -> None:
    """Dispatch Firefox cleanup based on OS."""
    system = platform.system()
    log("Firefox:")
    if system == "Darwin":
        clear_firefox_favicons_mac()
    elif system == "Windows":
        clear_firefox_favicons_windows()
    else:
        log("  non-macOS/non-Windows system – skipping Firefox.")
    log("")


# ------------------------------------------------------------
# Safari favicon cleanup (macOS only)
# ------------------------------------------------------------

def clear_safari_favicons_mac() -> None:
    """
    Clear Safari favicon cache on macOS.

    Safari keeps favicons in:
        ~/Library/Safari/Favicon Cache

    We remove the whole directory; Safari will recreate it.
    """
    cache_dir = ensure_expanded("~/Library/Safari/Favicon Cache")
    log("Safari:")
    if not cache_dir.exists():
        log("  Safari favicon cache directory not found – skipping.")
    else:
        remove_path(cache_dir)
    log("")


def clear_safari_favicons() -> None:
    """Dispatch Safari cleanup only on macOS."""
    system = platform.system()
    if system == "Darwin":
        clear_safari_favicons_mac()
    else:
        # No Safari on Windows; do nothing.
        pass


# ------------------------------------------------------------
# Main entry point
# ------------------------------------------------------------

def main() -> None:
    """Main launcher: detect OS and clear favicon caches."""
    system = platform.system()
    log("==============================================")
    log(f" Favicon cache cleaner  |  OS detected: {system}")
    log("==============================================")
    log("")

    # Order: Chrome, Firefox, Safari (Safari: macOS only)
    clear_chrome_favicons()
    clear_firefox_favicons()
    clear_safari_favicons()

    log("Done. Browsers may recreate favicon caches as you browse.")
    log("You may want to restart your browsers if they were running.")

    # On Windows, if run via double-click, keep the window open
    # so you can read the output.
    if os.name == "nt":
        input("\nPress ENTER to close this window... ")


if __name__ == "__main__":
    main()
