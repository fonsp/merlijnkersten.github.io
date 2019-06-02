# AUTOMATED RE-NAMING OF PHOTOS
# SUNDAY, 2 JUNE

# =============================

# Goal: Need a systematic way to access photos in the /assets repository so
# they can be used on the soloespresso (and eventually nerdonanisland)
# pages. With a few exceptions, there is one photo per day and I therefore
# want to automatically change the name of the pictures to 
# soloespressoYYYY-MM-DD.jpg or something similar. I'll then mannually
# correct the exceptions.

# Input: an 800px-wide image file named 'XXXXX.jpg'
# Output: an 800px-wide image file named 'soloespressoYYYY-MM-DD.jpg'

# Potential issues: 1) some dates have multiple images, will one of them
# be ignored? 

# From https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
# and https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python/39501288#39501288
# os.path.getctime() gets creation time (need date) on Windows only.
# needs os and platform

# From https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
# os.rename(old_file, new_file) renames a file. Can use: 
# os.path.join("directory", "name.extensions")

# Alternative (same source):
# from pathlib import Path
# p = Path(some_path)
# p.rename(Path(p.parent, "{}_{}".format(p.stem, 1) + p.suffix))

# https://stackoverflow.com/questions/19501711/how-can-i-convert-os-path-getctime
# For correct date+time

import os
from datetime import datetime
from shutil import copyfile
import random
from PIL import Image

root_directory = r"C:\\Users\\Merlijn Kersten\\Pictures\\Backgrounds"
os.chdir(root_directory) #Sets directory

for subdir, dirs, files in os.walk(root_directory):
    for file in files:
        old_path = file
        a = os.path.getctime(old_path) #creation date (computer)
        b = datetime.fromtimestamp(a).strftime('%Y-%m-%d') #creation date (human-readable)
        c = "Background800px" + b +".jpg" #correct filename
        new_path = os.path.join("C:\\", "Users", "Merlijn Kersten", "Pictures", "Backgrounds Renamed", c)
        if os.path.isfile(new_path) != True:
            image = Image.open(old_path)
            image.thumbnail((800,100000))
            image.save(new_path)
            print("Image #" + file + " is now: " + c)  
        else:
            new_c = "attention_needed_" + str(random.randint(1,100000)) + "_" + c #random integer to avoid double-naming (most of the time)
            new_path = os.path.join("C:\\", "Users", "Merlijn Kersten", "Pictures", "Backgrounds Renamed", new_c)
            image = Image.open(old_path)
            image.thumbnail((800, 100000))
            image.save(new_path)
            print("Attention need for file" + c)

