import time
from rawmovement import *

def test_pitch(rm):
    #pitch up?
    power = RCIOPowerNormalized(pitch = 0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #pitch stop
    power.set(pitch = 0, throttle = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #pitch down
    power.set(pitch = -0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #pitch stop
    power.set(pitch = 0, throttle = 0)
    rm.set_motor_power(power)

def test_roll(rm):
    #roll right?
    power = RCIOPowerNormalized(roll = 0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #roll stop
    power.set(roll = 0, throttle = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #roll left?
    power.set(roll = -0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #roll stop
    power.set(roll = 0, throttle = 0)
    rm.set_motor_power(power)
    
def test_yaw(rm):
    #yaw right?
    power = RCIOPowerNormalized(yaw = 0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #yaw stop
    power.set(yaw = 0, throttle = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #yaw left?
    power.set(yaw = -0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #yaw stop
    power.set(yaw = 0, throttle = 0)
    rm.set_motor_power(power)
    

def test_forward(rm):
    #forward
    power = RCIOPowerNormalized(forward = 0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #forward stop
    power.set(forward = 0, throttle = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #backward
    power.set(forward = -0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #backward stop
    power.set(forward = 0, throttle = 0)
    rm.set_motor_power(power)
    

def test_lateral(rm):
    #strafe right?
    power = RCIOPowerNormalized(lateral = 0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #strafe stop
    power.set(lateral = 0, throttle = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #strafe left?
    power.set(lateral = -0.5, throttle = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #strafe stop
    power.set(lateral = 0, throttle = 0)
    rm.set_motor_power(power)

rospy.init_node('sdrcauv_main')
mavros.set_namespace()
rm = RawMovement()
    
