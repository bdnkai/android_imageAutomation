
import cv2 as cv
import numpy as np
import os
from time import time
from vision import Vision
from windowcapture import WindowCapture
from assignment import Recognize
from assignment import Device


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

# print(icon_img)




# vision_gntitlebar = Vision(icon_img)



looplist = []

    # ===== ASSIGNMENT =====

while True:

    for adb in range(totalDevices):
        if adb in range(len(adb_names)):
            Recognize(icon_img, adb_names, adb)

    if cv.waitKey(1) == ord('q'):
        quit()
        cv.destroyAllWindows()
        break








