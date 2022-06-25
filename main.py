from cv2 import VideoCapture,QRCodeDetector
from pyqrcode import *

cam = VideoCapture(0)
detector = QRCodeDetector()
cash = []

def save(data):
    my_QR = create(str(data))
    x = 0
    my_QR.png(f'qr({x}).png')
    x += 1

def live_capture():
    while True:
        _,img = cam.read()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)

        if bbox is not None and data != "" and data not in cash:
            cash.append(str(data))
            print(f"data : {data}")

live_capture()