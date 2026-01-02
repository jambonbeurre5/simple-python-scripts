import re
from collections import Counter

# Track IPs
error_ips = set()
successful_post = []

# Open log file (assume "access.log")
with open("access.log") as f:
    for line in f:
        parts = line.split()
        ip = parts[0]
        # Check if 9th field (index 8) is 404
        if parts[8] == "404":
            error_ips.add(ip)
        # Check if POST /admin was successful (200)
        if len(parts) > 8 and parts[5] == '"POST' and parts[6] == "/admin" and parts[8] == "200":
            if ip in error_ips:
                successful_post.append(ip)

# Count top 10 IPs
top_ips = Counter(successful_post).most_common(10)
print(top_ips)
