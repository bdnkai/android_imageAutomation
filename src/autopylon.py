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

  


  device_name = ['badbar0', 'badbar1', 'badbar2', 'badbar3']



  for device in devices:
    device = device

  for i in device_name:
    wincap = [WindowCapture(i)]
   

  while(True):

    for win in wincap:
       screenshot = win.get_screenshot()
     
    for i in device_name:
        cv2.imshow(i, screenshot)
    
    


    if cv2.waitKey(1) == ord('q'):
      cv2.destroyAllWindows()
      break


cv.waitKey()

print('Done.')
 

  # if len(devices) == 0:
  #     print('no device attached')
  #     quit()