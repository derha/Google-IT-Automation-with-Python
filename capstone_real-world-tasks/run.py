#!/usr/bin/env python3

import os
import requests

keys = ["title", "name", "date", "feedback"]

for file in os.listdir("/data/feedback/"):
    with open("/data/feedback/" + file) as f:
        review_dict = dict()
        for key in keys:
            review_dict[key] = f.readline().strip()

    # Replace <corpweb-external-IP> with corpweb's external IP address.
    response = requests.post("http://<corpweb-external-IP>/feedback/", json=review_dict)
    response.raise_for_status()
