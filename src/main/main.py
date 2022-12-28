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



notice_img = img_path('notice')
exit_img = img_path('exit')
icon_img = img_path('icon')
enter_img = img_path('enter')

main_task = icon_img, exit_img, notice_img

print(main_task)


adb_names = ["badbar0","badbar1","badbar2","badbar3"]
list_of_devices = Device.devices
devices_in_total = len(list_of_devices)

# def run_init(sequence):
#     Recognize(ball_img, adb_names, sequence)





BASEDIR = os.path.abspath(__file__)
def run_init(sequence):
    print(adb_names[sequence])
    for task in main_task:
        Assign(task, adb_names[sequence], sequence)


if __name__ == '__main__':
    def test():
        with concurrent.futures.ProcessPoolExecutor() as executor:

            future = [executor.submit(run_init, sequence= adb)for adb in range(devices_in_total)]


            for f in concurrent.futures.as_completed(future):
                print(f.result())







# this_device  =   Assign(ball_img, adb_names, 1)
# print(this_device.this_device())

    while True:
        test()

        # break




        if cv.waitKey(1) == ord('q'):
            quit()
            cv.destroyAllWindows()


