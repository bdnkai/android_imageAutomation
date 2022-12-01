
import cv2 as cv
import numpy as np
import os
from time import time
# from windowcapture import WindowCapture
# from autopylon import ADB_Connect
# from detection import Image_Detector


os.chdir(os.path.dirname(os.path.abspath(__file__)))

gnmenu_img = cv.imread('./img/gnmenu.png', cv.IMREAD_UNCHANGED)
gntitlebar_img = cv.imread('./img/gntitlebar.png', cv.IMREAD_UNCHANGED)


result = cv.matchTemplate(gntitlebar_img, gnmenu_img, cv.TM_CCOEFF_NORMED)
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
        
        cv.rectangle(gnmenu_img, top_left, bottom_right, line_color, line_type)

    cv.imshow('matches', gnmenu_img)

else:
        print('match not found')


# emulator = "badbar0", "badbar1", "badbar2", "badbar3"

# for i in emulator:
    # wincap = WindowCapture(i)



while(True):
    
    # get an updated image of the game
    # for i in emulator:
    #     screenshot = wincap.get_screenshot()
    #     cv.imshow(f'{i}', screenshot)



    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


cv.waitKey()

print('Done.')