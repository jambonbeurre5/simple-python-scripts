import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file) as f:
        data = json.load(f)
    
    # Assume JSON has a list of objects with 'ip' field
    ips = [item['ip'] for item in data if 'ip' in item]

    # Write CSV
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP"])
        for ip in ips:
            writer.writerow([ip])

# Example usage
json_to_csv("threat.json", "firewall_blocklist.csv")
