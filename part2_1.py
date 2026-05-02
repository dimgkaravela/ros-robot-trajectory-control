#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def rotate():
    rospy.init_node('rotate')

    pub_q1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub_q2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(30) 

    q1_initial = 0
    q1_final = -0.610865238198 
    q2_initial = 0
    q2_final = 0.872664625 

    
    for i in range(101):
        t = i / 100.0

        print(t)

        q1 = (1 - t) * q1_initial + t * q1_final
        q2 = (1 - t) * q2_initial + t * q2_final

        pub_q1.publish(q1)
        pub_q2.publish(q2)

        rate.sleep()

if __name__ == '__main__':
    try:
        rotate()
    except rospy.ROSInterruptException:
        pass

