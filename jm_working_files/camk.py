# this is from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2
#import paho.mqtt.client as mqtt
import sys

#LOCAL_MQTT_HOST=sys.argv[1]
#LOCAL_MQTT_PORT=int(sys.argv[2])
#LOCAL_MQTT_TOPIC=sys.argv[3]

#def on_connect_local(client, userdata, flags, rc):
#        print("connected to local broker with rc: " + str(rc))

#local_mqttclient = mqtt.Client()
#local_mqttclient.on_connect = on_connect_local
#local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

#local_mqttclient.publish(LOCAL_MQTT_TOPIC,"test message")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# the index depends on your camera setup and which one is your USB camera.
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    try:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#            face = gray[y:y+h, x:x+w]
#            rc,png = cv2.imencode('.png', face)
#            msg = png.tobytes()
            #local_mqttclient.publish(LOCAL_MQTT_TOPIC,"Face Detected!")
#            local_mqttclient.publish(LOCAL_MQTT_TOPIC,msg)
    except:
        continue
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
