# !python3 -m venv env

# !source env/bin/activate

# !which python

# !pip3 install -r requirements.txt

# !apt remove python3-opencv --yes

# this is from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2 as cv
#import paho.mqtt.client as mqtt
import sys



# LOCAL_MQTT_HOST=sys.argv[1]
# LOCAL_MQTT_PORT=int(sys.argv[2])
# LOCAL_MQTT_TOPIC=sys.argv[3]

# def on_connect_local(client, userdata, flags, rc):
#        print("connected to local broker with rc: " + str(rc))

# local_mqttclient = mqtt.Client()
# local_mqttclient.on_connect = on_connect_local
# local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

# local_mqttclient.publish(LOCAL_MQTT_TOPIC,"test message")

vegmaster = cv.dnn.readNetFromONNX('best.onnx')

cv.imread('redcross.jpg')

classes = ["apple","banana","beef","blueberries","bread","butter","carrot","cheese","chicken","chicken_breast","chocolate","corn","eggs","flour","goat_cheese","green_beans","ground_beef","ham","heavy_cream","lime","milk","mushrooms","onion","potato","shrimp","spinach","strawberries","sugar","sweet_potato","tomato"]

colors = np.random.uniform(0, 255, size=(len(classes), 3))

# the index depends on your camera setup and which one is your USB camera.
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret_val, img = cap.read()
    rows = img.shape[0]
    cols = img.shape[1]
    vegmaster.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
    # Our operations on the frame come here
    cvOut = vegmaster.forward()

    # Go through each object detected and label it
    for detection in cvOut[0,0,:,:]:
        score = float(detection[2])
        if score > 0.3:

            idx = int(detection[1])
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

        # draw the prediction on the frame
            label = "{}: {:.2f}%".format(classes[idx],score * 100)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(img, label, (int(left), int(y)),cv.FONT_HERSHEY_SIMPLEX, 0.5, colors[idx], 2)

  # Display the frame
    cv2.imshow('my webcam', img)
    if cv2.waitKey(1) == 27:
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

