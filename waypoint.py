import rospy

import mavros
import mavros.utils
import mavros.setpoint

import tf

import smach
import smach_ros

import thread
import threading

class Waypoint:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.publisher  = mavros.setpoint.get_pub_position_local(queue_size = 10)
        self.subscriber = rospy.Subscriber(mavros.get_topic('local_position', 'pose'), mavros.setpoint.PoseStamped, self.reached)

    def navigate(self):
        rate = rospy.Rate(10)

        msg = mavros.setpoint.PoseStamped(header = mavros.setpoint.Header(frame_id = 'base_footprint',
                                                                          stamp = rospy.Time.now()))
        while not rospy.is_shutdown():
            msg.pose.position.x = self.x
            msg.pose.position.y = self.y
            msg.pose.position.z = self.z

            yaw_degrees = 0
            yaw = math.radians(yaw_degrees)
            quaternion = tf.transformations.quaternion_from_euler(0, 0, yaw)
            msg.pose.orentiation = mavros.setpoint.Quaternion(*quaternion)

            self.publisher.publish(msg)
            rate.sleep()

            thread.start_new_thread(self.navigate, ())
            self.done = False
            self.done_evt = threading.Event()
            
    def set(self, x, y, z, duration = 0, wait = True):
        self.done = False
        self.x = x
        self.y = y
        self.z = z

        if wait:
            rate = rospy.Rate(5)
            while not self.done and not rospy.is_shutdown():
                rate.sleep()
        time.sleep(duration)

    def reached(self, topic):
        def is_near(msg, x, y):
            rospy.logdebug("Position %s: local: %d, target: %d, abs diff: %d", msg, x, y, abs(x - y))
            return abs(x-y) < 0.5
        if is_near('X', topic.pose.position.x, self.x) and \
           is_near('Y', topic.pose.position.y, self.y) and \
           is_near('Z', topic.pose.position.z, self.z):
            self.done = True
            self.done_evt.set()
