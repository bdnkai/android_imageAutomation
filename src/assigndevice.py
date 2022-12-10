from ppadb.client import Client as AdbClient
import time
import threading
import cv2 as cv
import numpy as np
from PIL import Image
from vision import Vision
from windowcapture import WindowCapture



class AssignDevice:
    adb = AdbClient(host='127.0.0.1', port=5037)
    devices = adb.devices()

#   properties
    namesArray = ["badbar0","badbar1","badbar2","badbar3"]
    device = None
    device_names = None
    device_h = 0
    device_w = 0

    screenshot = []
    vision_image = None



#   constructor
    def __init__(self, device_name, vision_image):
        if len(self.devices) >= 1:
            for i in range(devices):
                print(f'Im seeing {len(devices)} devices, currently assigning device:{i}')
                for device in self.devices:
                    if i == len(self.devices):
                        print(f'No more devices to assing')
                        break
                    elif i < len(self.devices):
                        new_device = device[i]
                        self.device = new_device
                        self.device_name = self.device
                        self.device_name = device_name
                        self.device_name = self.device_name
                        self.wincap = WindowCapture(device_name)
                    else:
                        print(i)

                # while True:
                #     self.screenshot = self.wincap.get_screenshot()
                #     # print('screenshot has been mutated to: ' f'{self.screenshot}')
                #     # print('vision image has been mutated to: ' f'{self.vision_image}')
                #     points = vision_image.find(self.screenshot,0.8, 'points')
                #     print(len(AssignDevice.devices))
                #     quiit()
                #     cv.imshow(f'{device_name}', self.screenshot)
                #
                #     if cv.waitKey(1) == ord('q'):
                #         cv.destroyAllWindows()
                #         quit()
                #         print('Done.')
                #         break







        # if __init__:


                    #     get window size then convert img to window size
                    #     convert image size before calling vision function









            if len(self.devices) == 0:
                    print('no device attached')
                    quit()








