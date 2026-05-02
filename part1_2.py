#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

MAX_LINEAR_VELOCITY = 0.2  
MAX_ANGULAR_VELOCITY = 40 * (math.pi / 180)  

def calculate_angular_velocity(t):
    if t <= 1.55:
        return (min(1.35*t - 0.87*(t**2), MAX_ANGULAR_VELOCITY))
    elif 59.55 < t <= 62.88:
        return (min(0.6284*(t - 59.55) - 0.1887*((t - 59.55)**2), MAX_ANGULAR_VELOCITY))
    else:
        return 0

def calculate_linear_velocity(t):
    if 1.55 < t <= 59.55:
        return (min(0.009*(t - 1.55) - 0.00015*((t - 1.55)**2), MAX_LINEAR_VELOCITY))
    else:
        return 0

def move_robot():
    rospy.init_node('move_turtlebot3')
    
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    twist = Twist()

    start_time = rospy.Time.now().to_sec()

    counter = 0 

    while not rospy.is_shutdown():
        current_time = rospy.Time.now().to_sec() - start_time

        twist.linear.x = calculate_linear_velocity(current_time)
        twist.angular.z = calculate_angular_velocity(current_time)

        if twist.linear.x == 0 and twist.angular.z == 0 and counter != 0:
            break

        counter = 1

        pub.publish(twist)

        rospy.sleep(0.01)

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass

