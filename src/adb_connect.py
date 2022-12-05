from ppadb.client import Client as AdbClient
import time
import threading
import cv2
import numpy as np
from PIL import Image
import mss
from windowcapture import WindowCapture



class ADB_Connect:

  def __init__(self):
    adb = AdbClient(host='127.0.0.1', port=5037)
    devices = adb.devices()

  
    device = devices[0]
    print(device)
    device.shell(f'input tap 475 180')

    if len(devices) == 0:
        print('no device attached')
        quit()




  # for i in devices:
  #   device = i
  # while(True):
    
    




 
