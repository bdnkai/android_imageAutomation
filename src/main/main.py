import cv2 as cv
import numpy as np
import os
import time
import concurrent.futures

from action import dispatch

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
confirm_img = img_path('con')
model_img = img_path('model')
confirm_app_img = img_path('confirm_app')
eg_img = img_path('eg')

# in-game
skip_img = img_path('skip')
confirm2_img = img_path('confirm2')
confirm3_img = img_path('confirm3')
ryall_img = img_path('model')
main_quest_img = img_path('main_quest')
dialogue_img = img_path('dialogue')
dialogue2_img = img_path('dialogue2')
skip2_img = img_path('skip2')







if __name__ == '__main__':



# this_device  =   Assign(ball_img, adb_names, 1)
# print(this_device.this_device())

    while True:
        dispatch("assign", icon_img, 0.7)
        dispatch("assign", exit_img, 0.7)
        dispatch("assign", eg_img, 0.7)
        dispatch("assign", create_img, 0.6)
        dispatch("assign", mage_img, 0.7)
        dispatch("assign", confirm_app_img, 0.86)
        dispatch('assign', confirm_img, 0.65)
        dispatch('assign', model_img, 0.65)
        dispatch('assign', confirm2_img, 0.65)
        dispatch('assign', skip_img, 0.65)


        # test()
        # break




        if cv.waitKey(100) == ord('q'):
            quit()
            cv.destroyAllWindows()


