
import cv2 as cv
import numpy as np
import os
from time import time
from vision import Vision
from windowcapture import WindowCapture
from assignment import Device, Recognize


os.path.abspath(__file__)


# LOCAL VAR

adb_names = ["badbar0","badbar1","badbar2","badbar3"]

listOfDevices = Device.devices
totalDevices = len(listOfDevices)




# ====== VISION ======
def img_path(img_name):
    img = f'src//img//{img_name}.png'
    return img

icon_img = img_path("icon")
print(icon_img)


vision_gntitlebar = Vision(icon_img)







# ===== ASSIGNMENT =====

while True:

    for i in range(totalDevices):

        if i in range(len(adb_names)):
            print('pushing assignment')
            Recognize(vision_gntitlebar, adb_names, i)
            cv.waitKey(1)




    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses



# while True:
    # if Recognize:
    #     print(ShowDevice)
      # cv.imshow(ShowDevice.device_name)







