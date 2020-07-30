#!/usr/bin/env python3

import os
from PIL import Image


working_dir = "supplier-data/images"

for infile in os.listdir(working_dir):
    f, e = os.path.splitext(infile)
    outfile = f + ".jpeg"
    try:
        with Image.open(os.path.join(working_dir, infile)) as im:
            new_im = im.resize((600, 400)).convert("RGB")
            new_im.save(os.path.join(working_dir, outfile), "JPEG")
    except OSError:
        pass
