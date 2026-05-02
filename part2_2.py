#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import math

def rotate():
    rospy.init_node('rotate')

    pub_q1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub_q2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(100) 

    q1 = 0.0
    q2 = 0.0
    
    q1_dot_max = 10.0 * math.pi / 180.0 
    q2_dot_max = 8.0 * math.pi / 180.0  

    for i in range(1001):  
        t = i / 100.0  

        #  q1
        if t <= 1:
            q1_f = min(q1 + q1_dot_max * t, 0.04945 * t ** 2)
        elif 1 < t <= 9:
            q1_f = min(q1 + q1_dot_max * t, 0.04945 + 0.00989 * (t - 1))
        else:  
            q1_f = min(q1 + q1_dot_max * t, 0.89 - 0.04945 * ((10 - t) ** 2))

        #  q2
        if t <= 1:
            q2_f = min(q2 + q2_dot_max * t, - 0.04945 * t ** 2)
        elif 1 < t <= 9:
            q2_f = min(q2 + q2_dot_max * t, - 0.04945 - 0.00989 * (t - 1))
        else:  
            q2_f = min(q2 + q2_dot_max * t, - 0.89 + 0.04945 * ((10 - t) ** 2))

        pub_q1.publish(q1_f)
        pub_q2.publish(q2_f)

        rate.sleep()

if __name__ == '__main__':
    try:
        rotate()
    except rospy.ROSInterruptException:
        pass


