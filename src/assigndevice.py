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


class ShowDevice(Device):
    def __init__(self, test1, test2, test3):
        super().__init__(test1, test2, test3)

        while True:

            print(test1, test3)
            break
            # cv.imshow(f'{self.new_device_name}', self.screenshot)



class Recognize(Device):
    def __init__(self, vision_image_file, adb_names, device_number):
        super().__init__(vision_image_file, adb_names, device_number)


        if len(self.devices) >= 1:
            [device_number] = device_number
            device_number = device_number
            print(f'Im seeing {len(self.devices)} devices, there are {len(self.devices) - device_number } left to assign, currently assigning device: {adb_names[device_number]}')

            print(f'Device Number = {device_number}')
            print(f'Devices Length = {len(self.devices)}')

            devices_length = len(self.devices)

            if devices_length := device_number:
                print(f'No more devices to assign')


            else:
                new_device = self.devices[device_number]
                device = new_device
                print(device)
                new_device_name = adb_names[device_number]
                print(f'ASSIGNING: {new_device} AS: {new_device_name} from the list of {adb_names}')

                # new_device_name = new_device_name
                print(new_device_name)

                wincap = WindowCapture(new_device_name)
                new_wincap = wincap
                print(new_wincap)

                screenshot = new_wincap.get_screenshot()
                image_data = vision_image_file
                image_data.find(screenshot, 0.8, 'points')

                # cv.imshow(f'{self.new_device_name}', self.screenshot)
                print(' pushing data to showDevice')
                print(device_number + 1)
                adjusted_device_number = device_number + 1

                print(adjusted_device_number)
                Recognize(vision_image_file, adb_names, [adjusted_device_number])
                ShowDevice(f'{new_device_name}', screenshot, device_number)



            if len(self.devices) == 0:
                print('no device attached')
                quit()










