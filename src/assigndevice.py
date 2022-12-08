from ppadb.client import Client as AdbClient
import time
import threading
import cv2 as cv
import numpy as np
from PIL import Image
from vision import Vision
from windowcapture import WindowCapture



class AssignDevice:
#   properties
    device = None
    device_name = None
    device_h = 0
    device_w = 0
    adb = AdbClient(host='127.0.0.1', port=5037)
    devices = adb.devices()
    screenshot = []
    vision_image = None

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
                    print('screenshot as been mutated to:' f'{self.screenshot}')

                    self.vision_image = vision_image
                    print('vision image as been mutated to:' f'{self.vision_image}')




        # if __init__:


                    #     get window size then convert img to window size
                    #     convert image size before calling vision function









            if len(self.devices) == 0:
                    print('no device attached')
                    quit()








