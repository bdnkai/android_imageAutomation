from ppadb.client import Client as AdbClient
import time
import threading
import cv2 as cv
import numpy as np
from windowcapture import WindowCapture



class AssignDevice:
#   properties
    device = None
    device_name = None
    device_h = 0
    device_w = 0
    adb = AdbClient(host='127.0.0.1', port=5037)
    devices = adb.devices()
    screenshot = None

#   constructor
    def __init__(self, device_name, vision_image):
        if len(self.devices) >= 1:
            for device in self.devices:
                self.device = device
                self.device_name = self.device
                self.device_name = device_name
                self.device_name = self.device_name
                wincap = WindowCapture(device_name)
                self.screenshot = wincap.get_screenshot()

        # if self.screenshot > 0:
        while(True):
            self.points = vision_image.find(self.screenshot, 0.7, 'points')
            if self.points:
                print(f'{self.points[0]}')
                
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break




            # print(device)

    # device.shell(f'input tap 318 31')

        if len(self.devices) == 0:
                print('no device attached')
                quit()

  # for i in devices:
  #   device = i
  # while(True):
    
    




 