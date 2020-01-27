import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib
import os

HOST=''
PORT=8487

# following are the codes for receiving the image captured by
# raspberry pie cam, and then saving it as a file

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    while len(data) < payload_size:
        print("Recv: {}".format(len(data)))
        data += conn.recv(4096)

    print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    print("msg_size: {}".format(msg_size))
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    # cv2.imshow('ImageWindow',frame)
    cv2.imwrite('capApfel.png',frame)
    break

    cv2.waitKey(1)



# our trained model tests whether the image received is rotten or not,
# and sends the reply message accordingly

from imageai.Detection.Custom import CustomObjectDetection
execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(detection_model_path="finalModel.h5")
detector.setJsonPath(configuration_json=r"detection_config.json")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="capApfel.png", minimum_percentage_probability=60, output_image_path="badApfelnew.png")

for detection in detections:
    # print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

    if detection["name"]=="damaged_apple":
        data="damaged"
    elif detection["name"]=="apple":
        data="good"

# sending the result back to the raspberry pie camera
conn.sendall(data.encode('utf-8'))
