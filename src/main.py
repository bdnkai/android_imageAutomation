
import cv2 as cv
import numpy as np
import os
from time import time
from vision import Vision
from windowcapture import WindowCapture
from assigndevice import Device, Recognize


os.path.abspath(__file__)

#   constructor

def img_path(img_name):
    img = f'src//img//{img_name}.png'
    return img

icon_img = img_path("icon")
print(icon_img)







vision_gntitlebar = Vision(icon_img)

currentDevice = []

adb_names = ["badbar0","badbar1","badbar2","badbar3"]

listOfDevices = Device.devices
totalDevices = len(listOfDevices)

print(range(len(listOfDevices)))
print(range(totalDevices))
print(totalDevices)

for i in adb_names :
    if i < totalDevices:
        print('nothing else to assign, bye')
    else:
        Recognize(vision_gntitlebar, [adb_names][i], [i])






