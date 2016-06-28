#!/usr/bin/env python
#smach only, navigation wasn't usable

import rospy

import mavros
import mavros.utils
import mavros.setpoint

import tf

import smach
import smach_ros


from navigation import Navigation

def Circle():
  

	mavros.set_namespace()
	rate = rospy.Rate(10)
	n = Navigation()
	offset_z = -2
		


        rospy.loginfo("Flying in a circle")

 
        n.set_position(1.5, 0, offset_z, 5)

        #fly in a circle
        offset_x = 1.5
        offset_y = -1.5

        sides = 360
        radius = 1.5

        n.set_position(0, 0, 10, 3)
        i = 0
        while not rospy.is_shutdown():
            j = -i + 90
            x = radius * math.cos(j * 2 * math.py / sides) + offset_x
            y = radius * math.sin(j * 2 * math.py / sides) + offset_y
            z = offset_z

            wait = False
            duration = 0
            if i == 0 or i == sides:
                wait = true
                delay = 5

            n.set_position(x, y, z, duration, wait)

            i += 1
            rate.sleep()

            if i > sides:
                break



def circle_move_server():

	rospy.init_node('circle_move_server')
	s = rospy.Service('circle_move', circleMove, Circle)
	rospy.spin()


if __name__ == '__main__':
    circle_move_server()
