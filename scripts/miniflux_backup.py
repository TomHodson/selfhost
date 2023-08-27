import miniflux
import yaml
from pathlib import Path
import logging 
logging.captureWarnings(True)

root = Path(__file__).parents[1]

with open(root / "data/secrets.yaml", 'r') as file:
    credentials = yaml.safe_load(file)["miniflux"]

import requests
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth(credentials["username"], credentials["password"]) 

r = requests.get("https://selfhost.local/miniflux/v1/export", auth=basic, verify=False)

assert "opml" in r.text
with open(root / "backups/feeds.opml", 'w') as f:
    f.write(r.text)