#borrowed liberally from mavros' setpoint_position_demo


import rospy

import mavros
import mavros.utils
import mavros.setpoint

import tf

import thread
import threading

class Navigation:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.roll_degrees  = 0.0
        self.pitch_degrees = 0.0
        self.yaw_degrees   = 0.0

        self.publisher  = mavros.setpoint.get_pub_position_local(queue_size = 10)
        self.subscriber = rospy.Subscriber(mavros.get_topic('local_position', 'pose'), mavros.setpoint.PoseStamped, self.reached)


        try:
            thread.start_new_thread(self.navigate, ())
        except:
            fault("Unable to start thread")

        self.done = False
        self.done_evt = threading.Event()

    def navigate(self):
        rate = rospy.Rate(10)

        msg = mavros.setpoint.PoseStamped(header = mavros.setpoint.Header(frame_id = 'base_footprint',
                                                                          stamp = rospy.Time.now()))
        while not rospy.is_shutdown():
            msg.pose.position.x = self.x
            msg.pose.position.y = self.y
            msg.pose.position.z = self.z

            roll  = math.radians(self.roll_degrees)
            pitch = math.radians(self.pitch_degrees)
            yaw   = math.radians(self.yaw_degrees)

            quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
            msg.pose.orentiation = mavros.setpoint.Quaternion(*quaternion)

            self.publisher.publish(msg)
            rate.sleep()

            
    def set_position(self, x, y, z, duration = 0, wait = True):
        self.done = False
        self.x = x
        self.y = y
        self.z = z

        if wait:
            rate = rospy.Rate(5)
            while not self.done and not rospy.is_shutdown():
                rate.sleep()
        time.sleep(duration)

    def set_orientation(self, roll, pitch, yaw, duration = 0, wait = True):
        self.done = False
        self.roll_degrees  = roll
        self.pitch_degrees = pitch
        self.yaw_degrees   = yaw

        if wait:
            rate = rospy.Rate(5)
            while not self.done and not rospy.is_shutdown():
                rate.sleep()
        time.sleep(duration)

    def reached(self, topic):
        def is_near(msg, x, y, tolerance = 0.5):
            rospy.logdebug("Position %s: local: %d, target: %d, abs diff: %d", msg, x, y, abs(x - y))
            return abs(x-y) < tolerance
        
        roll, pitch, yaw = euler_from_quaternion(msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w)
        if is_near('X', topic.pose.position.x, self.x) and \
           is_near('Y', topic.pose.position.y, self.y) and \
           is_near('Z', topic.pose.position.z, self.z) and \
           is_near('roll',  math.degrees(roll),  self.roll_degrees)  and \
           is_near('pitch', math.degrees(pitch), self.pitch_degrees) and \
           is_near('yaw',   math.degrees(yaw),   self.yaw_degrees):
            self.done = True
            self.done_evt.set()
