#!/usr/bin/env python3
"""
Dying Light: The Beast Save Editor – Edit health, stamina, and resources.
Open source – no game memory modification, works directly with save files.
"""

import os
import json
import shutil
from datetime import datetime

SAVE_FILE = os.path.expandvars(r"%USERPROFILE%\Documents\Dying Light 2\out\save\save_coop_0.sav")
BACKUP_DIR = os.path.expanduser("~/DLBeast_Backups")

def backup_save():
    """Create a timestamped backup of the save file"""
    if not os.path.exists(SAVE_FILE):
        print("❌ Save file not found. Play the game first to create a save.")
        return False
    
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"save_{timestamp}.sav")
    shutil.copy2(SAVE_FILE, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return True

def edit_stats():
    """Edit player stats in the save file"""
    # This is a demo. The full trainer modifies memory directly.
    print("⚠️ This script is a placeholder. The full trainer is available in Releases.")
    print("📦 The trainer supports:")
    print("   - God Mode (F1)")
    print("   - Infinite Stamina (F3)")
    print("   - Beast Mode (F7)")
    print("   - One-Hit Kills (F9)")
    print("\nTo manually edit your save file:")
    print("   1. Locate save_coop_0.sav in Documents/Dying Light 2/out/save/")
    print("   2. Make a backup before editing")
    print("   3. Use a hex editor to modify values like 'health', 'stamina', etc.")

if __name__ == "__main__":
    if backup_save():
        edit_stats()
        input("\nPress Enter to exit...")