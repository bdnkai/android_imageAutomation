from ppadb.client import Client as AdbClient
import time
import threading
import cv2
import numpy as np
from PIL import Image
import mss
from windowcapture import WindowCapture



class ADB_Connect:

  adb = AdbClient(host='127.0.0.1', port=5037)
  devices = adb.devices()

  device_names = ['badbar0', 'badbar1', 'badbar2', 'badbar3']

  device = devices

    # how to make this continuous
  for name in device_names:
    name = name
    print(name)
    wincap = WindowCapture(name)
    
    for device in devices:
      device = device
      screenshot = wincap.get_screenshot()
      print(device)
      cv2.imshow(name, screenshot)
      
    








  # for device in devices:
    


    # wincap = WindowCapture(device)
    
   

  while(True):

    # screenshot = wincap.get_screenshot()
    for i in device_names:
      device_name = i
      wincap = WindowCapture(device_name)
      screenshot = wincap.get_screenshot()

    cv2.imshow(device_name, screenshot)


    
    


    if cv2.waitKey(1) == ord('q'):
      cv2.destroyAllWindows()
      break


cv.waitKey()

print('Done.')
 

  # if len(devices) == 0:
  #     print('no device attached')
  #     quit()