from ppadb.client import Client as AdbClient
import time
import threading
import cv2
import numpy as np
from PIL import Image
import mss



class ADB_Connect:

  adb = AdbClient(host='127.0.0.1', port=5037)
  devices = adb.devices()
  print(f'')

  for i in devices:
    device = i
    device.shell(f'input tap 475 180')


  if len(devices) == 0:
      print('no device attached')
      quit()
