
import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from adb_connect import ADB_Connect


os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture("badbar0")
screenshot = wincap.get_screenshot()
gnmenu_img = cv.imread('./img/gnmenu.png', cv.IMREAD_UNCHANGED)
gntitlebar_img = cv.imread('./img/gntitlebar.png', cv.IMREAD_UNCHANGED)
test

result = cv.matchTemplate(gntitlebar_img, screenshot, cv.TM_CCOEFF_NORMED)
print(result)

threshold = 1
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))
print(locations)

if locations:
    # print('found a match')
    gntitlebar_w = gntitlebar_img.shape[1]
    gntitlebar_h = gntitlebar_img.shape[0]
    line_color = (0,255,0)
    line_type = cv.LINE_4

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + gntitlebar_w, top_left[1] + gntitlebar_h)
        
        cv.rectangle(screenshot, top_left, bottom_right, line_color, line_type)

    cv.imshow('matches', screenshot)

else:
        print('match not found')








while(True):
    

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        

cv.waitKey()

print('Done.')