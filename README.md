# AutonomousDroneLineFollower
This project uses a **Convolutional Neural Network (CNN)** to enable a drone to automatically detect and follow a line using its onboard camera.  

This project works in conjunction with the Tello drone from Ryze Robotics. Images are captured with the drone's on-board camera. These pictures are sent to the computer via WiFi where an inference is made using the CNN model. According to the inference made, a directional command is sent back to the drone.

Useful links:
CNN Model: https://huggingface.co/muizzkhan0/AutonomousDroneLineFollower
Training Dataset: https://huggingface.co/datasets/muizzkhan0/AutonomousDroneLineFollower

## Dataset
A custom dataset was collecting using the drone's onboard camera itself. The data was then organized into six classes: No Line, Straight, Move Left, Turn Left, Move Right, Turn Right. The dataset collected can be found at ![Link](https://huggingface.co/datasets/muizzkhan0/AutonomousDroneLineFollower) https://huggingface.co/datasets/muizzkhan0/AutonomousDroneLineFollower.
