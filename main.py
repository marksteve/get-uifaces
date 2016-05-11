import json
import sys
import time

import requests
from tqdm import tqdm

uifaces = {}

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) == 2 else 12180
    print "Getting {} uifaces...".format(count)
    with tqdm(total=count, unit="uiface") as progress:
        while len(uifaces) < count:
            data = requests.get("http://uifaces.com/api/v1/random").json()
            if data.get("username") in uifaces:
                continue
            uifaces[data["username"]] = data["image_urls"]
            progress.update(len(uifaces))
            time.sleep(0.1)
    with open("uifaces.json", "wb") as f:
        f.write(json.dumps(uifaces))
    print "Written to uifaces.json"
