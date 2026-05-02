#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move():
    rospy.init_node('move_turtlebot3_node')

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    twist = Twist()

    rospy.sleep(1)

    twist.linear.x = 0.0  
    twist.angular.z = 10 * 3.14159 / 180  

    for i in range(10):
        pub.publish(twist)
        rospy.sleep(1)

   
    twist.linear.x = 0.1  
    twist.angular.z = -15 * 3.14159 / 180 

    for i in range(15):
        pub.publish(twist)
        rospy.sleep(1)

   
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass

