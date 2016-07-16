#!/usr/bin/env python

import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv

def handle_arm():
	mavros.set_namespace()
	try:
		arm = rospy.ServiceProxy(mavros.get_topic('cmd'), arming)
		ret = arm(true)
	except rospy.ServiceException, e:
		rospy.loginfo("Arming failed")

def arm_server():
	rospy.init_node('arm_server')
	s = rospy.Service('arm', arm, handle_arm)
	rospy.loginfo("Setup Arm server")
	rospy.spin

if __name__ == "__main__":
	arm_server()
