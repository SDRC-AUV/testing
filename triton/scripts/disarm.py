#!/usr/bin/env python

import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv

def disarm():
	mavros.set_namespace()
	rospy.ServiceProxy(mavros.get_topic('cmd', 'arming'), mavros_msgs.srv.CommandBool).call(False)

def disarm_server():
	rospy.init_node('disarm_server')
	s = rospy.Service('disarm', disarm, disarm)
	print "Disarming motors"
	rospy.spin

if __name__ == "__main__":
	disarm_server()
