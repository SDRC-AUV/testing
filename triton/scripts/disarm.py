#!/usr/bin/env python

import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv

def handle_disarm():
	mavros.set_namespace()
	try:
		disarm = rospy.ServiceProxy(mavros.get_topic('cmd'), arming)
		ret = disarm(false)
	except rospy.ServiceException, e:
		rospy.loginfo("Disarming failed")
	

def disarm_server():
	rospy.init_node('disarm_server')
	s = rospy.Service('disarm', disarm, handle_disarm)
	rospy.loginfo("Setup disarm server")
	rospy.spin

if __name__ == "__main__":
	disarm_server()
