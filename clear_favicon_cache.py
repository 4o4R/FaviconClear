# File: clear_favicon_cache.py
# Works with: Python 2.7+ and Python 3.x
#
# PURPOSE:
#   Cross-platform launcher that clears favicon-related caches for:
#       - Google Chrome (all profiles it can find)
#       - Mozilla Firefox (all profiles it can find)
#       - Apple Safari (macOS only)
#   Browsers will recreate the files safely.
#
# HOW TO USE:
#   macOS:   python clear_favicon_cache.py   (or python3)
#   Windows: python clear_favicon_cache.py   (or double-click run_cleaner.bat)

from __future__ import print_function

import os
import shutil
import platform
import sys

MIN_VERSION = (2, 7)


# ------------------------------------------------------------
# Small helper functions
# ------------------------------------------------------------

def log(msg):
    """Print a simple status line."""
    print(msg)


def remove_path(path):
    """
    Delete a file or directory if it exists.

    Using os.path and shutil for compatibility with Python 2.7.
    """
    try:
        if not os.path.exists(path):
            return

        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
            log("  removed directory: {0}".format(path))
        else:
            try:
                os.remove(path)
                log("  removed file     : {0}".format(path))
            except OSError as e:
                log("  [WARN] could not remove {0} ({1})".format(path, e))
    except Exception as e:
        log("  [WARN] could not remove {0} ({1})".format(path, e))


def ensure_expanded(path_str):
    """Expand ~ and environment variables and return a string path."""
    return os.path.expanduser(os.path.expandvars(path_str))


def remove_files_with_prefix(base_dir, prefix):
    """
    Walk a directory tree and remove files whose names start with prefix.
    """
    for root, dirs, files in os.walk(base_dir):
        for name in files:
            if name.startswith(prefix):
                remove_path(os.path.join(root, name))


# ------------------------------------------------------------
# Chrome favicon cleanup
# ------------------------------------------------------------

def clear_chrome_favicons_mac():
    """
    Clear Chrome favicon databases on macOS.
    """
    base_dir = ensure_expanded("~/Library/Application Support/Google/Chrome")
    if not os.path.exists(base_dir):
        log("  Chrome base directory not found (macOS) - skipping.")
        return

    log("  scanning Chrome profiles under: {0}".format(base_dir))
    remove_files_with_prefix(base_dir, "Favicons")


def clear_chrome_favicons_windows():
    """
    Clear Chrome favicon databases on Windows.
    """
    base_dir = ensure_expanded(r"%LOCALAPPDATA%\Google\Chrome\User Data")
    if not os.path.exists(base_dir):
        log("  Chrome base directory not found (Windows) - skipping.")
        return

    log("  scanning Chrome profiles under: {0}".format(base_dir))
    remove_files_with_prefix(base_dir, "Favicons")


def clear_chrome_favicons():
    """Dispatch Chrome cleanup based on OS."""
    system = platform.system()
    log("Chrome:")
    if system == "Darwin":
        clear_chrome_favicons_mac()
    elif system == "Windows":
        clear_chrome_favicons_windows()
    else:
        log("  non-macOS/non-Windows system - skipping Chrome.")
    log("")


# ------------------------------------------------------------
# Firefox favicon cleanup
# ------------------------------------------------------------

def clear_firefox_favicons_mac():
    """
    Clear Firefox favicon databases on macOS.
    """
    profiles_dir = ensure_expanded("~/Library/Application Support/Firefox/Profiles")
    if not os.path.exists(profiles_dir):
        log("  Firefox profiles directory not found (macOS) - skipping.")
        return

    log("  scanning Firefox profiles under: {0}".format(profiles_dir))
    patterns = ("favicons.sqlite", "favicons.sqlite-wal", "favicons.sqlite-shm")
    for profile in os.listdir(profiles_dir):
        subdir = os.path.join(profiles_dir, profile)
        if not os.path.isdir(subdir):
            continue
        for pattern in patterns:
            candidate = os.path.join(subdir, pattern)
            remove_path(candidate)


def clear_firefox_favicons_windows():
    """
    Clear Firefox favicon databases on Windows.
    """
    profiles_dir = ensure_expanded(r"%APPDATA%\Mozilla\Firefox\Profiles")
    if not os.path.exists(profiles_dir):
        log("  Firefox profiles directory not found (Windows) - skipping.")
        return

    log("  scanning Firefox profiles under: {0}".format(profiles_dir))
    patterns = ("favicons.sqlite", "favicons.sqlite-wal", "favicons.sqlite-shm")
    for profile in os.listdir(profiles_dir):
        subdir = os.path.join(profiles_dir, profile)
        if not os.path.isdir(subdir):
            continue
        for pattern in patterns:
            candidate = os.path.join(subdir, pattern)
            remove_path(candidate)


def clear_firefox_favicons():
    """Dispatch Firefox cleanup based on OS."""
    system = platform.system()
    log("Firefox:")
    if system == "Darwin":
        clear_firefox_favicons_mac()
    elif system == "Windows":
        clear_firefox_favicons_windows()
    else:
        log("  non-macOS/non-Windows system - skipping Firefox.")
    log("")


# ------------------------------------------------------------
# Safari favicon cleanup (macOS only)
# ------------------------------------------------------------

def clear_safari_favicons_mac():
    """
    Clear Safari favicon cache on macOS.
    """
    cache_dir = ensure_expanded("~/Library/Safari/Favicon Cache")
    log("Safari:")
    if not os.path.exists(cache_dir):
        log("  Safari favicon cache directory not found - skipping.")
    else:
        remove_path(cache_dir)
    log("")


def clear_safari_favicons():
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

def wait_for_enter():
    """Wait for ENTER on Windows double-click; safe on other OSes too."""
    try:
        prompt = "\nPress ENTER to close this window... "
        if sys.version_info[0] < 3:
            raw_input(prompt)  # noqa: F821  # type: ignore
        else:
            input(prompt)
    except Exception:
        pass


def ensure_min_python():
    """Require Python 2.7+."""
    if sys.version_info < MIN_VERSION:
        log("This script requires Python {0}.{1} or newer.".format(MIN_VERSION[0], MIN_VERSION[1]))
        wait_for_enter()
        sys.exit(1)


def main():
    """Main launcher: detect OS and clear favicon caches."""
    ensure_min_python()

    system = platform.system()
    log("==============================================")
    log(" Favicon cache cleaner  |  OS detected: {0}".format(system))
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
        wait_for_enter()


if __name__ == "__main__":
    main()
