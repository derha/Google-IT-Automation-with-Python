#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
working_dir = "supplier-data/images"
for file in os.listdir(working_dir):
    f, e = os.path.splitext(file)
    if e == ".jpeg":
        with open(os.path.join(working_dir, file), "rb") as opened:
            r = requests.post(url, files={"file": opened})
