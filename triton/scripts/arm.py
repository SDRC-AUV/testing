#!/usr/bin/env python

import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv

def arm():
	mavros.set_namespace()
	rospy.ServiceProxy(mavros.get_topic('cmd', 'arming'), mavros_msgs.srv.CommandBool).call(True)

def arm_server():
	rospy.init_node('arm_server')
	s = rospy.Service('arm', arm, arm)
	print "Arming motors"
	rospy.spin

if __name__ == "__main__":
	arm_server()
