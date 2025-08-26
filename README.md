# AutonomousDroneLineFollower
This project uses a **Convolutional Neural Network (CNN)** to enable a drone to automatically detect and follow a line using its onboard camera.  

This project works in conjunction with the Tello drone from Ryze Robotics. Images are captured with the drone's on-board camera. These pictures are sent to the computer via WiFi where an inference is made using the CNN model. According to the inference made, a directional command is sent back to the drone.
