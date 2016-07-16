#!/usr/bin/env python

#This is the service that will be holding our motor values. 
#It should be able to to act as a sort of psuedo class
#I'm making it a service so that it can act as a publisher as well


import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv


pitchPub = 0
rollPub = 0
throttlePub = 0
yawPub = 0
forwardPub = 0
lateralPub = 0

pitch = 1500
roll = 1500
throttle = 1500
yaw = 1500
forward = 1500
lateral = 1500


def handle_set_RCIOPower(req):
	
	rospy.loginfo("Seting RCIOPower")
	global roll = req.a
	global rollPub.publish(roll)
	global pitch = req.b
	global pitchPub.publish(pitch)	
	global throttle = req.c
	global throttlePub.publish(throttle)
	global yaw = req.d
	global yawPub.publish(yaw)
	global forward = req.e
	global forwardPub.publish(forward)
	global lateral = req.f
	global lateralPub.publish(lateral)
	try:
		set_rc = rospy.ServiceProxy(mavros.get_topic('rc'),override)
		ret = set_rc(roll,pitch,throttle,yaw,0,forward,lateral,0)
	except rospy.ServiceException, e:
		rospy.loginfo("Failed to set rc override")





def set_RCIOPower_server():
	rospy.init_node('set_CIOPower_server')
	s = rospy.Service('set_RCIOPower', set_RCIOPower, handle_set_RCIOPower)
	rospy.loginfo("Setup set_RCIOPower server and publisher")
	global pitchPub = rospy.Publisher('RCIOPitch',int, queue_size=10) 
	global rollPub = rospy.Publisher('RCIORoll',int, queue_size=10)
	global throttlePub = rospy.Publisher('RCIOthrottle',int, queue_size=10)
	global yawePub = rospy.Publisher('RCIOyaw',int, queue_size=10)
	global forwardPub = rospy.Publisher('RCIOforward',int, queue_size=10)
	global lateralPub = rospy.Publisher('RCIOlateral',int, queue_size=10)
	rospy.spin

if __name__ == "__main__":
	set_RCIOPower_server()
