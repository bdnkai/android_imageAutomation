import cv2 as cv
import numpy as np
import os
import time
import concurrent.futures
from assignment import Device, Assign
# from action import *





def img_path(img_name):
    img = f'src//img//{img_name}.png'
    return img

icon_img = img_path('icon')

ball_img = img_path('ball2')



adb_names = ["badbar0","badbar1","badbar2","badbar3"]
list_of_devices = Device.devices
devices_in_total = len(list_of_devices)
# def run_init(sequence):
#     Recognize(ball_img, adb_names, sequence)





# if __name__ == '__main__':
BASEDIR = os.path.abspath(__file__)
# ======  PRE CONCURRENCY MULTI PROCESSING  =========
def run_init(sequence):

    Recognize(ball_img, adb_names, sequence)


    # ======include multiprocessing here: ======
if __name__ == '__main__':
    def test():
        with concurrent.futures.ProcessPoolExecutor() as executor:

            future = [executor.submit(run_init, sequence= adb)for adb in range(devices_in_total)]
            results = executor.map(future)


            for f in concurrent.futures.as_completed(future):
                print(f.result())







this_device  =   Assign(ball_img, adb_names, 1)
print(this_device.tap_location)

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     while True:
    #         # test()
    #
    #         print(my_device)
    #         break
        # for result in results:
        # print(results)
        # assignment()

        #
        # f.result(future)
        #
        #     if cv.waitKey(1) == ord('q'):
        #         quit()
        #         cv.destroyAllWindows()
        #         break








