
import cv2 as cv
import numpy as np
import os
from time import time
from vision import Vision
from windowcapture import WindowCapture
from assigndevice import AssignDevice as aDevice


os.path.abspath(__file__)


def img_path(pic_name):
    img = f'src//img//{pic_name}.png'
    return img

icon_img = img_path("icon")



vision_gntitlebar = Vision(icon_img)

currentDevice = []
def android_device(vision_image):


    device_name = aDevice(namesArray[device],vision_image)
    currentDevice.append(device_name)
    println('current device has been pushed')
    println(currentDevice)
        # if statment for multiple device cvshow



# def adb_recognition(fetch_vision):
#         if AssignDevice.screenshot:
#             fetch_vision = vision_image.find(AssignDevice.screenshot, AssignDevice.device_name, 0.7, 'points')
#             return self.fetch_vision


while(True):

    if len(currentDevice) <= 0:
        adb_screenshot = android_device(vision_gntitlebar)




    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

cv.waitKey()
print('Done.')