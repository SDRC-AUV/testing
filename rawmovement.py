import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv

from pymavlink import mavutil

DEBUG = True

MAVROS = True


def arm():
    mavros.set_namespace()
    service = mavros.get_topic('cmd', 'arming')
    rospy.wait_for_service(service)
    rospy.ServiceProxy(service, mavros_msgs.srv.CommandBool).call(True)
    
def disarm():
    mavros.set_namespace()
    service = mavros.get_topic('cmd', 'arming')
    rospy.wait_for_service(service, timeout=5)
    rospy.ServiceProxy(service, mavros_msgs.srv.CommandBool).call(False)

def between(a, b, value):
    if value < min(a, b) or value > max(a, b):
        return False
    return True

def check(a, b, value):
    if DEBUG:
        if not between(a, b, value):
            raise ValueError
    else:
        pass

def norm_to_pwm(value):
    "converts numbers in range [-1,1] subset of R to range [1100,1900] subset of N"
    check(-1, 1, value)

    value = value * 400  # [-1, 1] -> [-400, 400]
    value = value + 1500 # [-400, 400] -> [1100, 1900]
    value = int(value)   # truncate
    return value

def pwm_to_norm(value):
    "converts numbers in range [1100,1900] subset of N to range [-1,1] subset of R"
    check(1100, 1900, value)

    value = value - 1500
    value = float(value)
    value = value / 400.0
    return value


class RCIOPower:
    def __init__(self, pitch=1500, roll=1500, throttle=1500, yaw=1500, forward=1500, lateral=1500):
        self.roll     = 1500
        self.pitch    = 1500
        self.throttle = 1500
        self.yaw      = 1500
        self.forward  = 1500
        self.lateral  = 1500

        self.set(pitch, roll, throttle, yaw, forward, lateral)

    def set(self, pitch=None, roll=None, throttle=None, yaw=None, forward=None, lateral=None):
        if roll is not None:
            check(1100, 1900, roll)
            self.roll = roll
        if pitch is not None:
            check(1100, 1900, pitch)
            self.pitch = pitch
        if throttle is not None:
            check(1100, 1900, throttle)
            self.throttle = throttle
        if yaw is not None:
            check(1100, 1900, yaw)
            self.yaw = yaw
        if forward is not None:
            check(1100, 1900, forward)
            self.forward = forward
        if lateral is not None:
            check(1100, 1900, lateral)
            self.lateral = lateral

    def __call__(self):
        return [self.pitch, \
                self.roll, \
                self.throttle, \
                self.yaw, \
                0xffff, \
                self.forward, \
                self.lateral, \
                0xffff]
    
    def get_message(self):
        msg = mavros_msgs.msg.OverrideRCIn()
        msg.channels = self.__call__()

class RCIOPowerNormalized(RCIOPower):
    def __init__(self, pitch=0, roll=0, throttle=0, yaw=0, forward=0, lateral=0):
        self.roll     = 0
        self.pitch    = 0
        self.throttle = 0
        self.yaw      = 0
        self.forward  = 0
        self.lateral  = 0

        self.set(pitch, roll, throttle, yaw, forward, lateral)

    def set(self, pitch=None, roll=None, throttle=None, yaw=None, forward=None, lateral=None):
        if roll is not None:
            check(-1, 1, roll)
            self.roll = roll
        if pitch is not None:
            check(-1, 1, pitch)
            self.pitch = pitch
        if throttle is not None:
            check(-1, 1, throttle)
            self.throttle = throttle
        if yaw is not None:
            check(-1, 1, yaw)
            self.yaw = yaw
        if forward is not None:
            check(-1, 1, forward)
            self.forward = forward
        if lateral is not None:
            check(-1, 1, lateral)
            self.lateral = lateral

    def __call__(self):
        return [norm_to_pwm(self.pitch), \
                norm_to_pwm(self.roll),\
                norm_to_pwm(self.throttle),\
                norm_to_pwm(self.yaw),\
                0xffff, \
                norm_to_pwm(self.forward),\
                norm_to_pwm(self.lateral),\
                0xffff]

    def get_message(self):
        msg = mavros_msgs.msg.OverrideRCIn()
        msg.channels = self.__call__()


def log(data):
    print(str(data.data))

class RawMovement:
    def __init__(self):

        if not MAVROS:        
            mavros.set_namespace()
            self.last_rcio_power = RCIOPower()

            self.publisher = rospy.Publisher('/mavros/rc/override',  mavros_msgs.msg.OverrideRCIn)
            self.in_subscriber  = rospy.Subscriber('/mavros/rc/in',  mavros_msgs.msg.RCIn, callback=log)
            self.out_subscriber = rospy.Subscriber('/mavros/rc/out', mavros_msgs.msg.RCOut, callback=log)
            
            self.arm_function = rospy.ServiceProxy(mavros.get_topic('cmd', 'arming'), mavros_msgs.srv.CommandBool).call

            alt_hold_msg = mavros_msgs.msg.OverrideRCIn()
            alt_hold_msg.channels = [0xffff, 0xffff, 0xffff, 0xffff, 1500, 0xffff, 0xffff, 0xffff]

            self.publisher.publish(alt_hold_msg)
        else:
            self.master = mavutil.mavlink_connection(None, baud = 115200)
            print("waiting for heartbeat...")
            master.wait_heartbeat()
            print("Connected")
            master.mav.requrest_data_stream_send(master.target_system, master.target_component, mavutil.mavlink.MAV_DATA_STREAM_ALL, 4, 1)
    
    def set_motor_power(self, power):
        if not MAVROS:
            self.publisher.publish(power.get_message())
        else:
            master.mav.rc_channels_override_send(master.target_system, master.target_component, power())


    def arm(self):
        self.arm_function(True)
    
    def disarm(self):
        self.arm_function(False)

    def close(self):
        if MAVROS:
            self.master.mav.rc_channels_override_send(master.target_system, master.target_component, [0]*8)

