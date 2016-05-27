#borrowed liberally from https://github.com/mavlink/mavros/blob/master/test_mavros/scripts/setpoint_position_demo

import rospy

import mavros
import mavros.utils
import mavros.setpoint

import tf

import smach
import smach_ros

import thread
import threading

from waypoint import Waypoint


def main():
    rospy.init_node('sdrcauv_main')
    mavros.set_namespace()
    rate = rospy.Rate(10)

    waypoint = Waypoint()

    offset_z = -2

    #sink
    waypoint.set(0, 0, offset_z)

    
    #fly in a square
    waypoint.set(3, 0, offset_z, 5)
    waypoint.set(3, -3, offset_z, 5)
    waypoint.set(0, -3, offset_z, 5)
    waypoint.set(0, 0, offset_z, 5)

    
    waypoint.set(1.5, 0, offset_z, 5)

    #fly in a circle
    offset_x = 1.5
    offset_y = -1.5

    sides = 360
    radius = 1.5

    waypoint.set(0, 0, 10, 3)
    i = 0
    while not rospy.is_shutdown():
        j = -i + 90
        x = radius * math.cos(j * 2 * math.py / sides) + offset_x
        y = radius * math.sin(j * 2 * math.py / sides) + offset_y
        z = offset_z

        wait = False
        duration = 0
        if i == 0 or i == sides:
            wait = true
            delay = 5

        waypoint.set(x, y, z, duration, wait)

        i += 1
        rate.sleep()

        if i > sides:
            break

        #land
        waypoint.set(0, 0, 0, -2, 5)
        waypoint.set(0, 0, 0, -1.5, 5)
        waypoint.set(0, 0, 0, -1, 5)
        waypoint.set(0, 0, 0, -.5, 2)
        waypoint.set(0, 0, 0, 0, 2)
        waypoint.set(0, 0, 0, 0.2, 2)
        
if __name__ == '__main__':
    main()
#after debugging uncomment
#    try:
#        main()
#    except:
#        print("something happened")
#        pass
