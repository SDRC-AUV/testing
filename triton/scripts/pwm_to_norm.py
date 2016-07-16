#!/usr/bin/env python

import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv



def handle_pwm_to_norm(req):
	resp1 = false
	#converts numbers in range [1100,1900] subset of N to range [-1,1 subset of R
	rospy.wait_for_service('between')
	try:
		between = rospy.ServiceProxy('between', between)
		resp1 = between(1100,1900,req.a)
	except rospy.ServiceException, e:
		rospy.loginfo("Failed to call between service")
	if resp1 == true:
		req.a = req.a - 1500
		req.a = float(req.a)
		req.a = req.a/400.0
		rospy.loginfo("pwm to norm conversion successful.")
	else:
		req.a = 0
		rospy.loginfo("pwm to norm conversion failed. Was it between 1100 and 1900?")
	return req.a
		

def pwm_to_norm_server():
	rospy.init_node('pwm_to_norm_server')
	s = rospy.Service('pwm_to_norm', pwm_to_norm, handle_pwm_to_norm)
	rospy.loginfo("Setup pwm to norm server")
	rospy.spin

if __name__ == "__main__":
	pwm_to_norm_server()
