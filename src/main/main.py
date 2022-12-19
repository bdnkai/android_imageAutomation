
import cv2 as cv
import numpy as np
import os
from assignment import Device, Recognize
from action import *





BASE_DIR = os.path.abspath(__file__)
IMG_DIR = os.path.abspath(__file__)
print(BASE_DIR)



# LOCAL VAR
if __name__ == "__main__":



    adb_names = ["badbar0","badbar1","badbar2","badbar3"]

    list_of_devices = Device.devices

    devices_in_total = len(list_of_devices)




    # ====== VISION ======
    def img_path(img_name):
        img = f'src//img//{img_name}.png'
        return img
    icon_img = img_path('icon')

    ball_img = img_path('ball2')

    head, tail = os.path.split(IMG_DIR)
    print(head)
    print(tail)

    # quit()

        # ===== ASSIGNMENT =====

    while True:

        for adb in range(devices_in_total):
            if adb in range(len(adb_names)):
                Recognize(ball_img, adb_names, adb)


        if cv.waitKey(1) == ord('q'):
            quit()
            cv.destroyAllWindows()
            break








