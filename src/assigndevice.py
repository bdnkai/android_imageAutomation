from ppadb.client import Client as AdbClient
import time
import threading
import cv2 as cv
import numpy as np
from PIL import Image
from vision import Vision
from windowcapture import WindowCapture



class Device(object):

    adb = AdbClient(host='127.0.0.1', port=5037)
    devices = adb.devices()
    def __init__(self, image_file, device_names, device_nums):

        #   properties
        self.device = None
        self.adb_name = []
        self.new_wincap = []
        self.device_h = 0
        self.device_w = 0

        self.screenshot = []
        self.vision_image = None
        self.points = None









class Recognize(Device):
    def __init__(self, vision_image_file, adb_names, device_number):
        super().__init__(vision_image_file, adb_names, device_number)
        print("Device")


        if len(self.devices) >= 1:

            print(f'Im seeing {len(self.devices)} devices, currently assigning device:{adb_names}')
            if device_number == (len(self.devices) - 1):
                print(device_number)
                print(f'No more devices to assign')

            else:
                new_device = self.devices
                self.device = new_device

                new_device_name = adb_names
                print(f'ASSIGNING: {self.device} AS: {new_device_name} from the list of {adb_names}')
                self.new_device_name = new_device_name
                print(self.new_device_name)
                wincap = WindowCapture(self.new_device_name)
                new_wincap = wincap
                print(new_wincap)

                self.screenshot = new_wincap.get_screenshot()
                image_data = vision_image_file
                image_data.find(self.screenshot, 0.8, 'points')

                cv.imshow(f'{self.new_device_name}', self.screenshot)
                return


            cv.waitkey(0)
            if len(self.devices) == 0:
                print('no device attached')
                quit()










