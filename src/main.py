import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from autopylon import ADB_Connect
from detection import Image_Detector

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.path.dirname(os.path.abspath(__file__))



# initialize the WindowCapture class
emulator = "badbar0", "badbar1", "badbar2", "badbar3"

for i in emulator:
    wincap = WindowCapture(i)



while(True):
    
    # get an updated image of the game
    for i in emulator:
        screenshot = wincap.get_screenshot()
        cv.imshow(f'{i}', screenshot)

    








    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')