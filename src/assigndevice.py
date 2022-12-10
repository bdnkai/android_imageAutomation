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
    adb_names = ["badbar0","badbar1","badbar2","badbar3"]
    device = None
    new_device_name = []
    new_wincap = []
    device_h = 0
    device_w = 0

    screenshot = []
    vision_image = None
    points = None



#   constructor
    def __init__(self, vision_image):
            if len(self.devices) >= 1:

                for i in range(len(self.devices)):
                    print(f'Im seeing {len(self.devices)} devices, currently assigning device:{i}')


                    if i == (len(self.devices)) - 1:
                        print(i)
                        print(f'No more devices to assign')
                        break

                    else:
                        new_device = self.devices[i]
                        self.device = new_device


                        new_device_name = self.adb_names[i]
                        print(f'ASSIGNING: {self.device} AS: {new_device_name} from the list of {self.adb_names}')
                        self.new_device_name = new_device_name

                        wincap = WindowCapture(self.new_device_name)
                        self.new_wincap.append(wincap)
                        print(self.new_wincap)
 






                    while True:

                        if self.new_device_name:

                            for win in self.new_wincap:
                                self.screenshot = win.get_screenshot()
                                cv.imshow(f'{self.new_device_name}', self.screenshot)


                        points = vision_image.find(self.screenshot, 0.8, 'points')

                        if cv.waitKey(1) == ord('q'):
                            cv.destroyAllWindows()
                            quit()
                            print('Done.')
                            break




            if len(self.devices) == 0:
                print('no device attached')
                quit()









        # if __init__:


                    #     get window size then convert img to window size
                    #     convert image size before calling vision function

















