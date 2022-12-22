
import cv2 as cv
import numpy as np
import os
import threading
import time
import concurrent.futures
from assignment import Device, Recognize
# from action import *



BASE_DIR = os.path.abspath(__file__)


# LOCAL VAR
if __name__ == "__main__":



    adb_names = ["badbar0","badbar1","badbar2","badbar3"]

    list_of_devices = Device.devices

    devices_in_total = len(list_of_devices)




    # ====== VISION ======
    def img_path(img_name):
        img = f'src//img//{img_name}.png'
        return img

    icon_img = img_path('icon')

    ball_img = img_path('ball2')

    head, tail = os.path.split(BASE_DIR)
    print(head)
    print(tail)

    # quit()
    #
    #     # ===== ASSIGNMENT =====
    def run_init():
        for adb in range(devices_in_total):
            if adb in range(len(adb_names)):
                Recognize(ball_img, adb_names, adb)

    # # TESTING =============================================


    # start = time.perf_counter()
    #
    # def run_init(seconds):
    #     print(f'Sleeping {seconds} second(s)...')
    #     time.sleep(seconds)
    #     # print("this one is finished")
    #     return (f'done {seconds}')



    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     secs = [5, 4, 3, 2, 1]
    #     # map method
    #     # results = executor.map(run_init, secs)
    #     #
    #     #
    #     # for result in results:
    #     #     print(result)
    #
    #     # list iterator
    #     results = [executor.submit(run_init, sec) for sec in secs]
    #
    #     f1 = executer.submit(run_init,1)
    #     f2 = executer.submit(run_init,1)
    #     print(f1.result())
    #     print(f1.result())
    #
    #     for f in concurrent.futures.as_completed(results):
    #         print(f.result())


    # finish = time.perf_counter()

    # print(f'Finished in {round(finish-start, 2)}')

    while True:

        run_init()




        if cv.waitKey(1) == ord('q'):
            quit()
            cv.destroyAllWindows()
            break
    #







