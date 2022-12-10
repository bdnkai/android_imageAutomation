
import cv2 as cv
import numpy as np
import os
from time import time
from vision import Vision
from windowcapture import WindowCapture
from assigndevice import Device


os.path.abspath(__file__)

#   constructor
class Recognize(Device):
    def __init__(self, vision_image_file, adb_number):
        super().__init__(vision_image_file, adb_number)
        print("Device")
def img_path(img_name):
    img = f'src//img//{img_name}.png'
    return img

icon_img = img_path("icon")
print(icon_img)







vision_gntitlebar = Vision(icon_img)

currentDevice = []

adb_names = ["badbar0","badbar1","badbar2","badbar3"]







# def adb_recognition(fetch_vision):
#         if AssignDevice.screenshot:
#             fetch_vision = vision_image.find(AssignDevice.screenshot, AssignDevice.device_name, 0.7, 'points')
#             return self.fetch_vi