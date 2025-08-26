# AutonomousDroneLineFollower
This project uses a **Convolutional Neural Network (CNN)** to enable a drone to automatically detect and follow a line using its onboard camera.  

This project works in conjunction with the Tello drone from Ryze Robotics. Images are captured with the drone's on-board camera. These pictures are sent to the computer via WiFi where an inference is made using the CNN model. According to the inference made, a directional command is sent back to the drone.

Demo: https://www.youtube.com/watch?v=ismJeOGh_W8  
<p align="center">
  <a href="https://www.youtube.com/watch?v=ismJeOGh_W8">
    <img src="https://img.youtube.com/vi/K-_hVV_IY0s/0.jpg" alt="Watch the video" />
  </a>
</p>

Useful links:
CNN Model: https://huggingface.co/muizzkhan0/AutonomousDroneLineFollower  
Training Dataset: https://huggingface.co/datasets/muizzkhan0/AutonomousDroneLineFollower  
Tello Drone: https://www.ryzerobotics.com/tello  
Tello Drone User Manual: https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20User%20Manual%20v1.4.pdf  
Official Tello App: https://www.dji.com/ca/downloads/djiapp/tello  

## Setup
1. Prerequisites
- Python 3.8+
- pip

2. Clone repo
3. Create a virtual environment (recommended)
4. Install dependencies via requirement.txt
5. Download CNN model

## Running the Demo
1. Turn on drone and connect via WiFi
2. Run AutonomousFlight.py
3. Program starts in manual control
O: Takeoff
P: Land
Arrow Up: Move forwards
Arrow Down: Move backwards
Arrow Left: Move left
Arrow right: Move Right
W: Move up
A: Turn Left (Adjust yaw left)
S: Move down
D: Turn right (Adjust yaw right)
Enter: Switch between manual and autonomous control
4. Takeoff and use manual controls to center the drone above the track
5. Enter autonomous mode
6. Land at any time


## Dataset
A custom dataset was collecting using the drone's onboard camera itself. The data was then organized into six classes: Straight, Turn Left, Move Left, Turn Right, Move Right, Straight. The dataset collected can be found at https://huggingface.co/datasets/muizzkhan0/AutonomousDroneLineFollower.
The data was randomly split 70-20-10 for training/validation/test.
Before training the data set was normalized and converted to grayscale.
<table align="center">
  <tr>
    <th>Straight</th>
    <th>Turn Left</th>
    <th>Move Left</th>
    <th>Turn Right</th>
    <th>Move Right</th>
    <th>No Line</th>
  </tr>
  <tr>
    <td><img src="https://github.com/muizzkhan0/AutonomousDroneLineFollower/blob/main/Images/image18.jpg" width="120"/></td>
    <td><img src="https://github.com/muizzkhan0/AutonomousDroneLineFollower/blob/main/Images/image14.jpg" width="120"/></td>
    <td><img src="https://github.com/muizzkhan0/AutonomousDroneLineFollower/blob/main/Images/image9.jpg" width="120"/></td>
    <td><img src="https://github.com/muizzkhan0/AutonomousDroneLineFollower/blob/main/Images/image11.jpg" width="120"/></td>
    <td><img src="https://github.com/muizzkhan0/AutonomousDroneLineFollower/blob/main/Images/image15.jpg" width="120"/></td>
    <td><img src="https://github.com/muizzkhan0/AutonomousDroneLineFollower/blob/main/Images/image8.png" width="120"/></td>
  </tr>
</table>


## Model Architecture

<p align="center">
  <img src="https://github.com/muizzkhan0/AutonomousDroneLineFollower/blob/main/Images/image17.png?raw=true" width="600"/>
</p>

## Results

<p align="center">
  <img src="https://github.com/muizzkhan0/AutonomousDroneLineFollower/blob/main/Images/image10.png" width="600"/>
</p>
