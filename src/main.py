
import cv2 as cv
import numpy as np
import os
from time import time
from vision import Vision
from windowcapture import WindowCapture
from assigndevice import Device


os.path.abspath(__file__)

def img_path(img_name):
    img = f'src//img//{img_name}.png'
    return img

icon_img = img_path("icon")
print(icon_img)

def android_device(vision_image):
    Android()






vision_gntitlebar = Vision(icon_img)

currentDevice = []


android_device(vision_gntitlebar)



# def adb_recognition(fetch_vision):
#         if AssignDevice.screenshot:
#             fetch_vision = vision_image.find(AssignDevice.screenshot, AssignDevice.device_name, 0.7, 'points')
#             return self.fetch_vi