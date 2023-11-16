# -*- coding: utf-8 -*-

import requests
import undetected_chromedriver as uc
import time
from PIL import Image
import os
from win32com.client import Dispatch

# Get Chrome version
def get_version_via_com(filename):
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)  # This functon returns the Chrome version, required for the uc driver
    except Exception:
        return None
    return version
paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
         r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"] # Please indicate here your path to the Chrome browser .exe file
version = list(filter(None, [get_version_via_com(p) for p in paths]))[0] # Get the version of Chrome
chromeversion=int(version.split(".")[0])

# Scrap the image
os.chdir('C:\Users\tartempion\Pictures')
url="https://www.mindat.org"
try:
    options = uc.ChromeOptions()
    #options.add_argument('--headless') # With this line uncommented, Chrome browser should not pop up during the scrapping - however this fails recently
    try:
        driver = uc.Chrome(use_subprocess=True, options=options,version_main=chromeversion)
    except:
        driver = uc.Chrome(use_subprocess=True, options=options)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    txt=driver.page_source
    txt=txt.split("Click to view full screen")[0].split("src=")[-1].replace("\"", "").split("><")[0]
    img_url="https://www.mindat.org"+txt
    time.sleep(0.5)
    
    imgopen_state=1
    while imgopen_state>0:
        try:
            img = Image.open(requests.get(img_url, stream = True).raw) # Try to get the image
            imgopen_state=0
        except:
            imgopen_state+=1
        if imgopen_state>10:
            imgopen_state=0 # If too many attemps then give up
    time.sleep(1)
    
    img.save('photo.png') # Save the image file
except:
    print("Mindat scrapping failed")