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

def Square():
  

	mavros.set_namespace()
	rate = rospy.Rate(10)
	n = Navigation()
	offset_z = -2
		


	rospy.loginfo("Flying in a square")

        n = userdata.navigation
        offset_z = userdata.offset_z

        #sink
        n.set_position(0, 0, offset_z)

        n.set_position(3, 0, offset_z, 5)
        n.set_position(3, -3, offset_z, 5)
        n.set_position(0, -3, offset_z, 5)
        n.set_position(0, 0, offset_z, 5)

        return 'circle'



def square_move_server():

	rospy.init_node('square_move_server')
	s = rospy.Service('square_move', squareMove, Square)
	rospy.spin()


if __name__ == '__main__':
    square_move_server()
