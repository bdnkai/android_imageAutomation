from ppadb.client import Client as AdbClient
import time
import threading
import cv2
import numpy as np
from PIL import Image
import mss



adb = AdbClient(host='127.0.0.1', port=5037)
print(adb.version())

devices = adb.devices()


if len(devices) == 0:
    print('no device attached')
    quit()


sct = mss.mss()
while True:


    scr = sct.grab({
        'left':8,
        'top':50,
        'width':882,
        'height':498
    })

    

    img = np.array(scr)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('output', gray)

    # def click_event(event, x, y, flags, params):
 
    # # checking for left mouse clicks
    #     if event == cv2.EVENT_LBUTTONDOWN:
        
    #         # displaying the coordinates
    #         # on the Shell
    #         print(x, ' ', y)
    
    #         # displaying the coordinates
    #         # on the image window
    #         font = cv2.FONT_HERSHEY_SIMPLEX
    #         cv2.putText(img, str(x) + ',' +
    #                     str(y), (x,y), font,
    #                     1, (255, 0, 0), 2)
    #         cv2.imshow('output', gray)
    
    #     # checking for right mouse clicks    
    #     if event==cv2.EVENT_RBUTTONDOWN:
        
    #         # displaying the coordinates
    #         # on the Shell
    #         print(x, ' ', y)
    
    #         # displaying the coordinates
    #         # on the image window
    #         font = cv2.FONT_HERSHEY_SIMPLEX
    #         b = img[y, x, 0]
    #         g = img[y, x, 1]
    #         r = img[y, x, 2]
    #         cv2.putText(img, str(b) + ',' +
    #                     str(g) + ',' + str(r),
    #                     (x,y), font, 1,
    #                     (255, 255, 0), 2)
    #         cv2.imshow('output', gray)

    #     img = cv2.imread("image", 1)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        running = False
        break




quit()