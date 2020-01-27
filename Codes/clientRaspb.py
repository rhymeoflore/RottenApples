import cv2
import io
import socket
import struct
import time
import pickle
import zlib
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50
servo0 = servo.Servo(pca.channels[0])
servo1 = servo.Servo(pca.channels[1])
servo2 = servo.Servo(pca.channels[2])
servo3 = servo.Servo(pca.channels[3])
servo4 = servo.Servo(pca.channels[4])
servo5 = servo.Servo(pca.channels[5])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.43.105', 8487))
connection = client_socket.makefile('wb')

cam = cv2.VideoCapture(0)

cam.set(3, 320);
cam.set(4, 240);

img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
#   data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)


    print("{}: {}".format(img_counter, size))
    client_socket.sendall(struct.pack(">L", size) + data)
    img_counter += 1
    break

cam.release()

data = client_socket.recv(10)
print("\n\n", data)
data=data.decode('utf-8')

if data == "damaged":
    print("arm start")
    servo1.angle = 100
    servo2.angle = 10
    servo4.angle = 155
    time.sleep(2)
    servo3.angle =130
    servo0.angle = 45
    time.sleep(2)
    servo3.angle =81
    time.sleep(2)
    servo0.angle = 95
    time.sleep(2)
    servo3.angle = 87
    time.sleep(2)
    servo1.angle = 180
    time.sleep(2)
    servo0.angle =45
    time.sleep(2)
    servo3.angle =130
    time.sleep(2)
    servo1.angle =90
    pca.deinit()



elif data == "good":
    print ("arm will not move")
# els
#     #Invalid stuff
