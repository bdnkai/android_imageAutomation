import cv2 as cv
import numpy as np
import os
import time
import concurrent.futures
from assignment import Device, Assign

adb_names = "MIRMG(2)"
list_of_devices = Device.devices
devices_in_total = len(list_of_devices)


def dispatch(action, img, threshold):

        match action:
            case "assign":
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    results = [executor.submit(Assign, vision_image_file=img, adb_name=adb_names[adb], device_sequence=adb, threshold= threshold)for adb in range(devices_in_total)]

                for f in concurrent.futures.as_completed(results):
                    this = f.result()
                    print(f'{f.result()}')
                    # this.tap(this.device, f'{950} {162}')
                    cv.imshow("test", this.screenshot)
                    cv.waitKey(1)


            case "main":
                return "one"
            case "dailies":
                return "two"
            case default:
                return "something"



