from imageai.Detection.Custom import CustomObjectDetection
import os


import numpy as np
import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
        cv2.imwrite('capApfel.png',frame)
        cv2.destroyAllWindows()
        break

cap.release()

execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(detection_model_path="detection_model-ex-028--loss-8.723.h5")
detector.setJsonPath(configuration_json=r"C:\Users\hp\Desktop\apple_detection_dataset\apple_dataset\json\detection_config.json")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="capApfel.png", minimum_percentage_probability=60, output_image_path="badApfelnew.png")

for detection in detections:
    # print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

    if detection["name"]=="damaged_apple":
        print("damaged")
    elif detection["name"]=="apple":
        print("good")
