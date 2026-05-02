# ROS Robot Trajectory Control

ROS 1 robotics project for controlling and analyzing the motion of TurtleBot3 and RRBot.

The project includes ROS nodes for velocity control, trajectory generation, joint control, and motion analysis using Octave and ROS plotting tools.

## Overview

This project was developed for a Robotics course assignment. It focuses on trajectory planning and control for two robotic systems:

- **TurtleBot3**, a differential-drive mobile robot
- **RRBot**, a two-joint robotic arm

The implementation uses ROS 1 nodes to send velocity and joint commands, while the motion behavior is analyzed through theoretical plots and ROS runtime data.

## Features

### TurtleBot3 Motion Control

- Publish linear and angular velocity commands
- Control robot motion through ROS topics
- Generate point-to-point trajectories
- Execute motion in three stages:
  - rotation toward the target
  - linear movement toward the target
  - final rotation to the desired orientation
- Use cubic polynomial trajectories for smooth motion
- Compare theoretical trajectories with actual ROS odometry data

### RRBot Joint Control

- Control two robotic arm joints
- Send desired joint positions
- Generate joint trajectories
- Use linear segments with parabolic blends
- Analyze joint angles and angular velocities
- Compare theoretical motion with ROS `rqt_plot` results

## Technologies

- ROS 1
- Python
- TurtleBot3
- RRBot
- Gazebo
- Octave
- rqt_plot
- Linux / Ubuntu
