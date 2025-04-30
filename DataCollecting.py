from djitellopy import Tello
import KeyboardControlModule as kp
import time
import cv2


# Connecting to the drone
drone = Tello()
drone.connect()
drone.streamon();
print(drone.get_battery())

kp.init()

# Video stream constants
width = 360
height = 240

# Used to periodically save images
count = 0

while True:

    # Displaying video stream
    myFrame = drone.get_frame_read().frame
    img = cv2.cvtColor(myFrame, cv2.COLOR_BGR2RGB)
    img = cv2.flip(img, 0)
    resized_img = cv2.resize(img, (width, height))
    #resized_img = cv2.flip(resized_img, 0) # Image should be flipped if using mirror clip
    cv2.imshow("Camera Feed", resized_img)
    
    # Capturing frames from the video stream
    if(count == 25):
    #if(kp.getKey("x")):
        cv2.imwrite(f'Resources/New_Data/{time.time()}.jpg', img)
        count = 0
    else:
        count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
drone.end()
