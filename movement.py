
#usage: move_[axis](distance)
#       move_[rotation axis](degrees)
# x: forward
# y: strafe
# z: 
from rawmovement import *
import math

mass = 50 #kg
drag_x = ?
drag_y = ?
drag_z = ?
thruster_force = 21.4 #N
velocity = 0.5 #m/s
angular_velocity = 60 #degrees/s

zero_power = RCIOPowerNormalized()

def angle_time_required(delta):
    return delta / angular_velocity + 0.1

def distance_time_required(distance, force, drag):
    return (mass * math.acosh(math.exp(drag * distance / mass))) / (math.sqrt(drag * force))

def distance_time_required_linear(distance, force=0, drag=0):
    return disatance / velocity + 0.5

def move_x(distance):
    sign = 1

    if distance < 0:
        sign = -1

    distance = distance * sign

    power = RCIOPowerNormalized(forward = sign * 0.5)
    rm = RawMovement()

    time = distance_time_required(distance, thruster_force, drag_x)

    rm.set_motor_power(power)
    rospy.sleep(time)
    rm.set_motor_power(zero_power)
    
    return time_required

def move_y(distance):
    sign = 1

    if distance < 0:
        sign = -1

    distance = distance * sign

    power = RCIOPowerNormalized(strafe = sign * 0.5)
    rm = RawMovement()

    time = distance_time_required(distance, thruster_force, drag_y)

    rm.set_motor_power(power)
    rospy.sleep(time)
    rm.set_motor_power(zero_power)
    
    return time_required

def move_z(distance):

    sign = 1

    if distance < 0:
        sign = -1

    distance = distance * sign

    power = RCIOPowerNormalized(throttle = sign * 0.5)
    rm = RawMovement()

    time = distance_time_required(distance, thruster_force, drag_z)

    rm.set_motor_power(power)
    rospy.sleep(time)
    rm.set_motor_power(zero_power)
    
    return time_required

def yaw(degrees):
    sign = 1

    if degrees < 0:
        sign = -1

    degrees = degrees * sign

    power = RCIOPowerNormalized(yaw = sign * 0.2)
    rm = RawMovement()

    time = angle_time_required(degrees)

    rm.set_motor_power(power)
    rospy.sleep(time)
    rm.set_motor_power(zero_power)
    
    return time_required
