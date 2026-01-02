
---

## Scripts Overview

### 1. `log_parser.py`
- Parses web server logs to:
  - Find IPs that received a `404` error.
  - Check if they later made a successful `POST /admin`.
- Outputs the **top 10 IPs** with counts.

### 2. `file_analysis.py`
- Finds all files in a directory (`/var/www/html` by default) that:
  - Were modified in the last 24 hours.
  - Are owned by `root`.
  - Contain the string `eval(base64_decode)`.
- Prints matching filenames.

### 3. `api_ingestion.py`
- Reads a Threat Intel JSON feed.
- Extracts all IP addresses.
- Writes them into a **CSV firewall blocklist**.

---

## Requirements

- Python 3.x
- Standard libraries only: `json`, `csv`, `re`, `collections`  

---

## Usage

1. **Clone the repository**

```bash
git clone https://github.com/jambonbeurre5/simple-python-scripts.git
cd simple-python-scripts

# Log parsing
python scripts/log_parser.py

# File analysis (can adjust folder path inside script)
python scripts/file_analysis.py

# Threat Intel JSON to CSV
python scripts/api_ingestion.py

