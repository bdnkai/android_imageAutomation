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
    def __init__(self, image_file, device_id):

        #   properties

        adb_names = ["badbar0","badbar1","badbar2","badbar3"]
        device = None
        new_device_name = []
        new_wincap = []
        device_h = 0
        device_w = 0

        screenshot = []
        vision_image = None
        points = None
        print(device_id)
        if len(self.devices) >= 1:
            for i in range(len(self.devices)):
                print(f'Im seeing {len(self.devices)} devices, currently assigning device:{i}')
                if i == (len(self.devices) - 1):
                    print(i)
                    print(f'No more devices to assign')

                else:
                    new_device = self.devices[i]
                    self.device = new_device

                    new_device_name = adb_names[i]
                    print(f'ASSIGNING: {self.device} AS: {new_device_name} from the list of {adb_names}')
                    self.new_device_name = new_device_name
                    print(self.new_device_name)
                    wincap = WindowCapture(self.new_device_name)
                    new_wincap = wincap
                    print(new_wincap)


                    while True:

                        self.screenshot = new_wincap.get_screenshot()
                        image_file.find(self.screenshot, 0.8, 'points')

                        cv.imshow(f'{self.new_device_name}', self.screenshot)

                        if cv.waitKey(1) == ord('q'):
                            cv.destroyAllWindows()
                            quit()
                            print('Done.')
                            break

                            
        if len(self.devices) == 0:
            print('no device attached')
            quit()









