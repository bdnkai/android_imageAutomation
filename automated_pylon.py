from cv2 import cv2 
from PIL import Image
import mss
from ppadb.client import Client


adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

running = True
