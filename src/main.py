
import cv2 as cv
import numpy as np
import os
from time import time
from vision import Vision
from windowcapture import WindowCapture
from assigndevice import AssignDevice as aDevice


os.path.abspath(__file__)


# gnmenu_img = cv.imread('./img/gamenotice_img.png', cv.IMREAD_UNCHANGED)
# gntitlebar_img = cv.imread('./img/gntitlebar.png', cv.IMREAD_UNCHANGED)




# screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
# result = cv.matchTemplate(gntitlebar_img, screenshot, cv.TM_CCOEFF_NORMED)
# print(result)

# threshold = 1
# locations = np.where(result >= threshold)
# locations = list(zip(*locations[::-1]))
# print(locations)
#
# if locations:
#     # print('found a match')
#     gntitlebar_w = gntitlebar_img.shape[1]
#     gntitlebar_h = gntitlebar_img.shape[0]
#     line_color = (0,255,0)
#     line_type = cv.LINE_4
#
#     for loc in locations:
#         top_left = loc
#         bottom_right = (top_left[0] + gntitlebar_w, top_left[1] + gntitlebar_h)
#
#         cv.rectangle(screenshot, top_left, bottom_right, line_color, line_type)
# else:
#   print('match not found')


# wincap = WindowCapture("badbar0")
# namesArray = ['badbar0']
namesArray = ["badbar0","badbar1","badbar2","badbar3"]

def img_path(pic_name):
    img = f'src//img//{pic_name}.png'
    return img

icon_img = img_path("icon")



vision_gntitlebar = Vision(icon_img)

currentDevice = []
def android_device(vision_image):
    for device in range(len(aDevice.devices)):

        device_name = aDevice(namesArray[device],vision_image)
        currentDevice.append(device_name)
        println('current device has been pushed')
        println(currentDevice)
        # if statment for multiple device cvshow



# def adb_recognition(fetch_vision):
#         if AssignDevice.screenshot:
#             fetch_vision = vision_image.find(AssignDevice.screenshot, AssignDevice.device_name, 0.7, 'points')
#             return self.fetch_vision


while(True):

    if len(currentDevice) <= 0:
        adb_screenshot = android_device(vision_gntitlebar)




    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

cv.waitKey()
print('Done.')