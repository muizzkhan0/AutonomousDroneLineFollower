import tensorflow as tf
from tensorflow.keras.models import load_model
from djitellopy import Tello

import KeyboardControlModule as kp
import time
import cv2
import numpy as np

new_model = load_model("FlightModel.h5")
class_labels = ["Move Left","Move Right","No Line","Straight","Turn Left","Turn Right"]

drone = Tello()
drone.connect()
drone.streamon();
print(drone.get_battery())

kp.init()


a_speed = 20
turn_speed = 50
command_delay = 0.500
no_command_delay = 0.500

manual = True

def getKeyInput():
    l_r, f_b, u_d, yaw = 0, 0, 0, 0
    speed = 40

    if kp.getKey("LEFT"):
        l_r = -speed
    elif kp.getKey("RIGHT"):
        l_r = speed

    if kp.getKey("UP"):
        f_b = speed
    elif kp.getKey("DOWN"):
        f_b = -speed

    if kp.getKey("w"):
        u_d = speed
    elif kp.getKey("s"):
        u_d = -speed

    if kp.getKey("a"):
        yaw = -speed
    elif kp.getKey("d"):
        yaw = speed

    if kp.getKey("o"):
        drone.takeoff()

    if kp.getKey("p"):
        drone.land()

    return [l_r, f_b, u_d, yaw]

while True:
    # Capturing frame from drone video stream
    myFrame = drone.get_frame_read().frame

    # Displaying frame to computer
    img = cv2.cvtColor(myFrame, cv2.COLOR_BGR2RGB)
    img = cv2.flip(img, 0)
    if manual == True:
        imgDisplay = cv2.resize(img, (360, 240))
        cv2.imshow("Camera Feed", imgDisplay)

    # Resizing frame then predicting using model
    resized_img = tf.image.resize(img, (256,256))
    prediction = new_model.predict(np.expand_dims(resized_img/255,0))
    index = np.argmax(prediction)
    print(f"Predicted Class: {class_labels[index]}")

    keyInput = getKeyInput()
    # Starts in manual control
    if manual == True:
        if(kp.getKey("RETURN")):
            manual = False
        drone.send_rc_control(keyInput[0], keyInput[1], keyInput[2], keyInput[3]) 
    # Pressing ENTER begins autonomous mode
    else:
        if(kp.getKey("RETURN")): # Pressing ENTER again reverts to manual mode
            manual = True
        elif(class_labels[index] == "No Line"):
            drone.send_rc_control(0, 0, 0, 0)
        elif(class_labels[index] == "Move Left"):
            drone.send_rc_control(-a_speed, 0, 0, 0)
            time.sleep(command_delay)
            drone.send_rc_control(0, 0, 0, 0)
            time.sleep(no_command_delay)
        elif(class_labels[index] == "Move Right"):
            drone.send_rc_control(a_speed, 0, 0, 0)
            time.sleep(command_delay)
            drone.send_rc_control(0, 0, 0, 0)
            time.sleep(no_command_delay)
        elif(class_labels[index] == "Straight"):
            drone.send_rc_control(0, a_speed, 0, 0)
            time.sleep(command_delay)
            drone.send_rc_control(0, 0, 0, 0)
            time.sleep(no_command_delay)
        elif(class_labels[index] == "Turn Left"):
            drone.send_rc_control(0, 0, 0, -turn_speed)
            time.sleep(command_delay)
            drone.send_rc_control(0, 0, 0, 0)
            time.sleep(no_command_delay)
        elif(class_labels[index] == "Turn Right"):
            drone.send_rc_control(0, 0, 0, turn_speed)
            time.sleep(command_delay)
            drone.send_rc_control(0, 0, 0, 0)
            time.sleep(no_command_delay)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
drone.end()