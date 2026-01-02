#!/usr/bin/env python3
import os
import time

directory = "/var/www/html"
now = time.time()
day_seconds = 24 * 60 * 60  # 24 hours

for root, dirs, files in os.walk(directory):
    for name in files:
        filepath = os.path.join(root, name)
        try:
            # Only files modified in last 24 hours
            if now - os.path.getmtime(filepath) <= day_seconds:
                # Only files owned by root
                if os.stat(filepath).st_uid == 0:
                    # Check if file contains the string
                    with open(filepath, "r", errors="ignore") as f:
                        if "eval(base64_decode)" in f.read():
                            print(filepath)
        except:
            pass
