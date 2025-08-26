# AutonomousDroneLineFollower
This project uses a **Convolutional Neural Network (CNN)** to enable a drone to automatically detect and follow a line using its onboard camera.  

This project works in conjunction with the Tello drone from Ryze Robotics. Images are captured with the drone's on-board camera. These pictures are sent to the computer via WiFi where an inference is made using the CNN model. According to the inference made, a directional command is sent back to the drone.

Useful links:
CNN Model: https://huggingface.co/muizzkhan0/AutonomousDroneLineFollower
Training Dataset: https://huggingface.co/datasets/muizzkhan0/AutonomousDroneLineFollower

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


