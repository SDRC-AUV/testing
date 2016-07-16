#!/usr/bin/env python

import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv



def handle_norm_to_pwm(req):
	resp1 = false
	#converts numbers in range [-1,1] subset of R to range [1100,1900] subset of N
	rospy.wait_for_service('between')
	try:
		between = rospy.ServiceProxy('between', between)
		resp1 = between(1,1,req.a)
	except rospy.ServiceException, e:
		rospy.loginfo("Failed to call between service")
	if resp1 == true:
		req.a = req.a * 400 #[-1,1] => [-400,400]
		req.a = req.a + 1500 # -> [1100,1900]
		req.a = int(req.a)
		rospy.loginfo("Norm to pwm conversion successful.")
	else:
		req.a = 0
		rospy.loginfo("Norm to pwn conversion failed. Was it between -1 and 1?")
	return req.a
		

def norm_to_pwm_server():
	rospy.init_node('norm_to_pwm_server')
	s = rospy.Service('norm_to_pwm', norm_to_pwm, handle_norm_to_pwm)
	rospy.loginfo("Setup norm to pwm server")
	rospy.spin

if __name__ == "__main__":
	norm_to_pwm_server()
