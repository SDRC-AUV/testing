#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String


#MISSIONS:
# -1 Test
# 0 Prerun
# 1 Launch -> Gate
# 2 Starting gate
# 3 Gate -> Colored Buoys
# 4 Buoy Task
# 5 Scuttle Task
# 6 Buoys -> Nav Channel
# 7 Nav Channel 
# More to be defined, after nav channel we have to determine 
# how to reach the octagon



#TASK RETURNS:
#I think we could decide on a convention for returns when
#a task service is called. Such as, complete, failure but retry, and 
#failure and move on
# -1 Failure and move on
# 0 Failure but retry
# 1 Complete


def mainLoop():
	rospy.init_node("mainLoop")
	mission = 0
	var = 1
	while var == 1:		
		if mission == 0:
			#Call prerun service
			#rospy.wait_for_service('prerun')
			#try:
				#prerun = rospy.ServiceProxy('prerun',prerun)
				#prerun_result = prerun()
				#if prerun_result = -1
					#mission = 1
					#maybe have some more detailed resetup services in this case
				#elif prerun_result = 0
					#mission = 0
					#maybe have some more detailed resetup services in this case
				#elif prerun_result = 1
					#mission = 1
			#except rospy.ServiceException, e:
				#print "Call to prerun failed: %s"%e
			#for the sake of compliling
			mission = 1
		
		elif mission == 1:
			#Call finding first gate service
			#rospy.wait_for_service('navGate')
			#try:
				#navGate = rospy.ServiceProxy('navGate',navGate)
				#navGate_result = navGate()
				#if navGate_result = -1
					#mission = 2
					#maybe have some more detailed resetup services in this case
				#elif navGate_result = 0
					#mission = 1
					#maybe have some more detailed resetup services in this case
				#elif navGate_result = 1
					#mission = 2
			#except rospy.ServiceException, e:
				#print "Call to navGatefailed: %s"%e
			mission = 2

		elif mission == 2:
			#Call first gate service
			#rospy.wait_for_service('clearGate')
			#try:
				#clearGate = rospy.ServiceProxy('clearGate',clearGate)
				#clearGate_result = clearGate()
				#if clearGate_result = -1
					#mission = 3
					#maybe have some more detailed resetup services in this case
				#elif clearGate_result = 0
					#mission = 2
					#maybe have some more detailed resetup services in this case
				#elif clearGate_result = 1
					#mission = 3
			#except rospy.ServiceException, e:
				#print "Call to clearGate failed: %s"%e
			mission = 3
	
		elif mission == 3:
			#Call gate -> buoy service
			#rospy.wait_for_service('navBuoy')
			#try:
				#navBuoy = rospy.ServiceProxy('navBuoy',navBuoy)
				#navBuoy_result = navBuoy()
				#if navBuoy_result = -1
					#mission = 4
					#maybe have some more detailed resetup services in this case
				#elif navBuoy_result = 0
					#mission = 3
					#maybe have some more detailed resetup services in this case
				#elif navBuoy_result = 1
					#mission = 4
			#except rospy.ServiceException, e:
				#print "Call to navBuoy failed: %s"%e
			mission = 4

		elif mission == 4:
			#Call buoy ID service
			#rospy.wait_for_service('IDBuoys')
			#try:
				#IDBuoys = rospy.ServiceProxy('IDBuoys',IDBuoys)
				#IDBuoys_result = IDBuoys()
				#if IDBuoys_result = -1
					#mission = 5
					#maybe have some more detailed resetup services in this case
				#elif IDBuoys_result = 0
					#mission = 4
					#maybe have some more detailed resetup services in this case
				#elif IDBuoys_result = 1
					#mission = 5
			#except rospy.ServiceException, e:
				#print "Call to IDBuoys failed: %s"%e
			mission = 5
		
		elif mission == 5:
			#Call scuttle service
			#rospy.wait_for_service('scuttle')
			#try:
				#scuttle = rospy.ServiceProxy('scuttle',scuttle)
				#scuttle_result = scuttle()
				#if scuttle_result = -1
					#mission = 6
					#maybe have some more detailed resetup services in this case
				#elif scuttle_result = 0
					#mission = 5
					#maybe have some more detailed resetup services in this case
				#elif scuttle_result = 1
					#mission = 6
			#except rospy.ServiceException, e:
				#print "Call to scuttle failed: %s"%e
			mission = 6

	
		elif mission == 6:
			#Call buoys -> channel service
			#rospy.wait_for_service('navChannel')
			#try:
				#navChannel = rospy.ServiceProxy('navChannel',navChannel)
				#navChannel_result = navChannel()
				#if navChannel_result = -1
					#mission = 7
					#maybe have some more detailed resetup services in this case
				#elif navChannel_result = 0
					#mission = 6
					#maybe have some more detailed resetup services in this case
				#elif navChannel_result = 1
					#mission = 7
			#except rospy.ServiceException, e:
				#print "Call to navChannel failed: %s"%e
			mission = 7

		elif mission == 7:
			#Call channel service
			#rospy.wait_for_service('channel')
			#try:
				#channel = rospy.ServiceProxy('channel',channel)
				#channel_result = channel()
				#if channel_result = -1
					#mission = 8
					#maybe have some more detailed resetup services in this case
				#elif channel_result = 0
					#mission = 7
					#maybe have some more detailed resetup services in this case
				#elif channel_result = 1
					#mission = 8
			#except rospy.ServiceException, e:
				#print "Call to channel failed: %s"%e
			mission = 0


		elif mission == -1:
			#Call test service
			#rospy.wait_for_service('test')
			#try:
				#testing = rospy.ServiceProxy('test', test)
				#test_result = testing()
				#if test_result == -1
					#sys.exit(1)
				#mission = 0			
			#except rospy.ServiceException, e:
				#print "Call to test failed: %s"%e
			missions = -1


if __name__ == "__main__":
	mainLoop()

