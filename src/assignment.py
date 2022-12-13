from ppadb.client import Client as AdbClient
import time
import threading
import cv2 as cv
import numpy as np
from vision import Vision
from windowcapture import WindowCapture



class Device(object):
    adb = AdbClient(host='127.0.0.1', port=5037)
    devices = adb.devices()
    # devices[0].shell('input tap 281 119')

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






imageList = []







class Recognize(Device):
    # def __init__(self, vision_image_file, adb_names, device_number):

        screenshot = []
        def __new__(cls, vision_image_file, adb_names, device_number):

            if len(cls.devices) >= 1:
                device_number = device_number

                devices_length = len(cls.devices)

                if devices_length is device_number:
                    # print(f' No more devices to assign')
                    quit()



                if devices_length > device_number:
                    # print(f' Im seeing {len(cls.devices)} devices, there are {len(cls.devices) - device_number } left to assign, currently assigning device: {adb_names[device_number]}')
                    new_device = cls.devices[device_number]
                    device = new_device
                    # print(device)
                    new_device_name = adb_names[device_number]
                    # print(f' ASSIGNING: {new_device} AS: {new_device_name} from the list of {adb_names}')

                    new_device_name = f'{new_device_name}'
                    # print(new_device_name)

                    wincap = WindowCapture(new_device_name)
                    new_wincap = wincap
                    # print(new_wincap)

                    screenshot = new_wincap.get_screenshot()

                    image_data = vision_image_file
                    image_data.find(new_device_name, screenshot, new_device, 0.8, 'rectangles')

                if cv.waitKey(1) == ord('q'):
                    quit()
                    cv.destroyAllWindows()



            else:
                adjusted_device_number = device_number + 1
                Recognize(vision_image_file, adb_names, adjusted_device_number)







            if len(cls.devices) == 0:
                print('no device attached')
                quit()










