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


# launch game
icon_img = img_path('icon')
notice_img = img_path('notice')
exit_img = img_path('exit')
enter_img = img_path('enter')

# makes character
mage_img = img_path('mage')
create_img = img_path('create')
confirm_img = img_path('confirm')
model_img = img_path('model')
confirm_app_img = img_path('confirm_app')
enter_game_img = img_path('enter')

# in-game
skip_img = img_path('skip')
confirm2_img = img_path('confirm2')
confirm3_img = img_path('confirm3')
ryall_img = img_path('model')
main_quest_img = img_path('main_quest')
dialogue_img = img_path('dialogue')
dialogue2_img = img_path('dialogue2')
skip2_img = img_path('skip2')

main_task = [
    icon_img,
    notice_img,
    exit_img,
    exit_img,
    enter_img,
    mage_img,
    create_img,
    confirm_img,
    model_img,
    confirm_app_img,
    enter_game_img,
    skip_img,
    confirm2_img,
    confirm3_img,
    main_quest_img,
    dialogue_img,
    dialogue2_img,
    skip2_img
]



adb_names = ["badbar4","badbar5","badbar6","badbar7"]
list_of_devices = Device.devices
devices_in_total = len(list_of_devices)

# def run_init(sequence):
#     Recognize(ball_img, adb_names, sequence)





BASEDIR = os.path.abspath(__file__)
def run_init(sequence):
    print(adb_names[sequence])
    process = ''
    for i in main_task:
        Assign(i, adb_names[sequence], sequence)


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


