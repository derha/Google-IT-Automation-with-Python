#!/usr/bin/env python3

import requests
import os
import re


working_dir = "supplier-data/descriptions/"

for file in os.listdir(working_dir):
    with open(os.path.join(working_dir, file), 'r+', encoding="utf-8") as f:
        content = dict()
        content["name"] = f.readline().strip()
        pattern = re.search(r"^([\d]+)", f.readline().strip())
        content["weight"] = int(pattern.group(1))
        content["description"] = f.readline().strip()
        f, e = os.path.splitext(file)
        content["image_name"] = f + ".jpeg"

        # replace [linux-instance-external-IP]
        response = requests.post("http://[linux-instance-external-IP]/fruits", json=content)
        response.raise_for_status()
