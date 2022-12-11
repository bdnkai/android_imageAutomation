
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




for names in adb_names:
    Recognize(vision_gntitlebar, names, [names])









# def adb_recognition(fetch_vision):
#         if AssignDevice.screenshot:
#             fetch_vision = vision_image.find(AssignDevice.screenshot, AssignDevice.device_name, 0.7, 'points')
#             return self.fetch_vi