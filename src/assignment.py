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



class Recognize(Device):
    # def __init__(self, vision_image_file, adb_names, device_number):

    screenshot = []

    def __new__(cls, vision_image_file, adb_names, device_number):

        if len(cls.devices) >= 1:
            device_number = device_number

            devices_length = len(cls.devices)

            if devices_length == device_number:
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
                screenshot = wincap.get_screenshot()
                # new_wincap = wincap
                # print(new_wincap)

                # get scale from official h *  w
                official_h = wincap.size_h
                official_w = wincap.size_w

                # check official capture before scaling

                float_scale_h = float(official_h / 720)
                float_scale_w = float(official_w / 1280)
                scale = (float_scale_h + float_scale_w) / 2

                print(f'--FLOAT H:{float_scale_h} FLOAT W: {float_scale_w}')
                print(int(scale*100))
                print(f'capturedW: {official_w}  CAPTURED_H: {official_h}  ')

                image_path = vision_image_file

                # convert img size
                img = cv.imread(image_path)
                scale_width = int(img.shape[1] / float_scale_w )
                scale_height = int(img.shape[0] / float_scale_h )
                scale = (scale_width + scale_height) / 2

                if scale_width <= int(img.shape[1]):

                    dim = (scale_height, scale_width)
                    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
                    print('Resized Dimensions : ', resized.shape)
                    vision_image = Vision(resized)
                    cv.imshow("Resized image", resized)
                    image_data = vision_image
                    image_data.find(scale, screenshot, 0.65, 'points')

                else:
                    dim = print(int(img.shape[1]), int(img.shape[0]))

                    vision_image = Vision(img)
                    image_data = vision_image
                    tap_location = image_data.find(scale, screenshot, 0.65, 'rectangles')

                    x = tap_location
                    y = tap_location


                    print(f'POOOOOIINTS:: {x} {y}')
                    device.shell(f'input tap {x} {y}')

            if cv.waitKey(1) == ord('q'):
                quit()
                cv.destroyAllWindows()



        else:
            adjusted_device_number = device_number + 1
            Recognize(vision_image_file, adb_names, adjusted_device_number)

        if len(cls.devices) == 0:
            print('no device attached')
            quit()
