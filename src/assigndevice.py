from ppadb.client import Client as AdbClient
import time
import threading
import cv2 as cv
import numpy as np
from PIL import Image
import mss
from windowcapture import WindowCapture



class AssignDevice:
#   properties
    device = None
    device_name = None
    device_h = 0
    device_w = 0
    adb = AdbClient(host='127.0.0.1', port=5037)
    devices = adb.devices()
    screenshot = [...]

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
                    self.points = vision_image.find(self.screenshot, device_name, 0.7, 'points')


            if self.points:
                    print(f'{self.points[0]}')
                
            #     get window size then convert img to window size
            #     convert image size before calling vision function









            if len(self.devices) == 0:
                    print('no device attached')
                    quit()








