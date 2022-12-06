
import cv2 as cv
import numpy as np
import os
from time import time
from vision import Vision
from windowcapture import WindowCapture
from assigndevice import AssignDevice


os.path.abspath(__file__)


# gnmenu_img = cv.imread('./img/gamenotice_img.png', cv.IMREAD_UNCHANGED)
# gntitlebar_img = cv.imread('./img/gntitlebar.png', cv.IMREAD_UNCHANGED)




# screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
# result = cv.matchTemplate(gntitlebar_img, screenshot, cv.TM_CCOEFF_NORMED)
# print(result)

# threshold = 1
# locations = np.where(result >= threshold)
# locations = list(zip(*locations[::-1]))
# print(locations)
#
# if locations:
#     # print('found a match')
#     gntitlebar_w = gntitlebar_img.shape[1]
#     gntitlebar_h = gntitlebar_img.shape[0]
#     line_color = (0,255,0)
#     line_type = cv.LINE_4
#
#     for loc in locations:
#         top_left = loc
#         bottom_right = (top_left[0] + gntitlebar_w, top_left[1] + gntitlebar_h)
#
#         cv.rectangle(screenshot, top_left, bottom_right, line_color, line_type)
# else:
#   print('match not found')


# wincap = WindowCapture("badbar0")
namesArray = ['badbar0']
# namesArray = ["badbar0","badbar1","badbar2","badbar3"]

for device in AssignDevice.devices:
    for name in namesArray:
        AssignDevice(name)

vision_gntitlebar = Vision('src\\img\\x.png')

while(True):


    points = vision_gntitlebar.find(screenshot, 0.7, 'points')


    if points:
        print(f'{points[0]}')
        break
    # print(points)

    # cv.imshow('matches', screenshot)






    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
        
cv.waitKey()
print('Done.')