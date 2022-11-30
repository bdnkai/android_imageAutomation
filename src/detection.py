import cv2 as cv, cv2
import numpy as np
import os
from windowcapture import WindowCapture
from threading import Thread, Lock


class Image_Detector:
    def __init__(self):
        path = os.path.dirname(os.path.dirname(__file__))
        img_path = os.path.join(path, 'img')

        gamenotice_img = cv2.imread(os.path.join(self.img_path, 'gamenotice.png'), cv2.IMREAD_UNCHANGED)
        result_try = cv2.matchTemplate(img, gamenotice_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result_try)
        if max_val > .9:
            print("Found it!!")
            gamenotice_img.get_screen_position()
            print(f'{gamenotice_img.get_screen_position()}')

        