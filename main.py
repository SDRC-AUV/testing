
#smach only, navigation wasn't usable

import rospy

import mavros
import mavros.utils
import mavros.setpoint

import tf

import smach
import smach_ros

import thread
import threading

from navigation import Navigation

class Square(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['success'],
                                   input_keys = ['navigation', 'offset_z'])    
    def execute(self, userdata):
        rospy.loginfo("Flying in a square")

        n = userdata.navigation
        offset_z = userdata.offset_z

        #sink
        n.set_position(0, 0, offset_z)

        n.set_position(3, 0, offset_z, 5)
        n.set_position(3, -3, offset_z, 5)
        n.set_position(0, -3, offset_z, 5)
        n.set_position(0, 0, offset_z, 5)

        return 'circle'


class Circle(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['success'],
                                   input_keys = ['navigation', 'offset_z'])

    def execute(self, userdata):
        rospy.loginfo("Flying in a circle")

        n = userdata.navigation
        offset_z = userdata.offset_z

        n.set_position(1.5, 0, offset_z, 5)

        #fly in a circle
        offset_x = 1.5
        offset_y = -1.5

        sides = 360
        radius = 1.5

        n.set_position(0, 0, 10, 3)
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

            n.set_position(x, y, z, duration, wait)

            i += 1
            rate.sleep()

            if i > sides:
                break
        return 'land'

class End(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['success'],
                                   input_keys = ['navigation'])

    def execute(self, userdata):
        rospy.loginfo("Finishing up")
        
        n = userdata.navigation

        #land
        n.set_position(0, 0, 0, -2, 10)
        n.set_position(0, 0, 0, -1.5, 5)
        n.set_position(0, 0, 0, -1, 5)
        n.set_position(0, 0, 0, -.5, 2)
        n.set_position(0, 0, 0, 0, 2)
        n.set_position(0, 0, 0, 0.2, 2)

        return 'end'

def main():
    rospy.init_node('sdrcauv_main')
    mavros.set_namespace()
    rate = rospy.Rate(10)

    n = Navigation()
    offset_z = -2

    sm = smach.StateMachine(outcomes = ['end'])
    sm.userdata.navigation = n
    sm.userdata.offset_z = offset_z

    with sm:
        smach.Statemachine.add('CIRCLE', Circle(),
                               transitions={'success':'END'},
                               remapping={'navigation':'navigation', #not sure if needed
                                          'offset_z':'offset_z'})
        smach.Statemachine.add('END', End(),
                               transitions={'success':'end'},
                               remapping={'navigation':'navigation'})
        smach.Statemachine.add('SQUARE', Square(),
                               transitions={'success':'CIRCLE'},
                               remapping={'navigation':'navigation',
                                          'offset_z':'offset_z'})

    outcome = sm.execute()

    
    #todo: test orientations


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
