#!/usr/bin/env python

import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv

def handle_between(req):
	if req.c < min(req.a,req.b) or req.c > max(req.a,req.b):
		rospy.loginfo("Value: %s was not between %s and %s"%(req.c,req.a,req.b))
		return false
	rospy.loginfo("Value: %s was between %s and %s"%(req.c,req.a,req.b))
	return true

def between_server():
	rospy.init_node('between_server')
	s = rospy.Service('between', between, handle_between)
	rospy.loginfo("Setup between server")
	rospy.spin()

if __name__ == "__main__":
	between_server()
