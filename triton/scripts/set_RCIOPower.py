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

RCOverRidePub = 0

def handle_set_RCIOPower(req):	
	global pitchPub
	global rollPub
	global throttlePub
	global yawPub
	global forwardPub
	global lateralPub
	global pitch
	global roll
	global throttle
	global yaw
	global forward
	global lateral
	global RCOverRidePub

	rospy.loginfo("Seting RCIOPower")
	roll = req.a
	rollPub.publish(roll)
	pitch = req.b
	pitchPub.publish(pitch)	
	throttle = req.c
	throttlePub.publish(throttle)
	yaw = req.d
	yawPub.publish(yaw)
	forward = req.e
	forwardPub.publish(forward)
	lateral = req.f
	lateralPub.publish(lateral)
	alt_hold_msg = mavros_msg.OverrideRCin()
	alt_hold_msg.channels = [roll,pitch,throttle,yaw,0,forward,lateral,0]
	RCOverRidePub.publish(alt_hold_msg)





def set_RCIOPower_server():
	global pitchPub
	global rollPub
	global throttlePub
	global yawPub
	global forwardPub
	global lateralPub
	global RCOverRidePub

	rospy.init_node('set_CIOPower_server')
	s = rospy.Service('set_RCIOPower', set_RCIOPower, handle_set_RCIOPower)
	rospy.loginfo("Setup set_RCIOPower server and publisher")
	pitchPub = rospy.Publisher('RCIOPitch',int, queue_size=10) 
	rollPub = rospy.Publisher('RCIORoll',int, queue_size=10)
	throttlePub = rospy.Publisher('RCIOThrottle',int, queue_size=10)
	yawPub = rospy.Publisher('RCIOYaw',int, queue_size=10)
	forwardPub = rospy.Publisher('RCIOForward',int, queue_size=10)
	lateralPub = rospy.Publisher('RCIOLateral',int, queue_size=10)
	RCOverRidePub =  rospy.Publisher('/mavros/rc/override',mavros_msgs.msg.OverrideRCIn)
	rospy.spin()

if __name__ == "__main__":
	set_RCIOPower_server()
