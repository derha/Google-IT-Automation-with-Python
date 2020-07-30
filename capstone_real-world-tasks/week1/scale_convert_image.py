#!/usr/bin/env python3

import os
from PIL import Image


source_dir = input("Source directory: ")
destination_dir = input("Destination directory: ")

if not os.path.isdir(destination_dir):
    os.makedirs(destination_dir)

for image in os.listdir(source_dir):
    try:
        with Image.open(os.path.join(source_dir, image)) as im:
            new_im = im.rotate(270).resize((128, 128)).convert("RGB")
            new_im.save(os.path.join(destination_dir, image), "JPEG")
    except OSError:
        pass
