import time
import signal
import sys
from rawmovement import *

def test_pitch(rm, power = 0.5):
    #pitch up?
    power = RCIOPowerNormalized(pitch = power)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #pitch stop
    power.set(pitch = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #pitch down
    power.set(pitch = -1*power)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #pitch stop
    power.set(pitch = 0)
    rm.set_motor_power(power)

def test_roll(rm, power = 0.5):
    #roll right?
    power = RCIOPowerNormalized(roll = power)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #roll stop
    power.set(roll = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #roll left?
    power.set(roll = -1*power)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #roll stop
    power.set(roll = 0)
    rm.set_motor_power(power)
    
def test_yaw(rm, power = 0.5):
    #yaw right?
    power = RCIOPowerNormalized(yaw = power)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #yaw stop
    power.set(yaw = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #yaw left?
    power.set(yaw = -1*power)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #yaw stop
    power.set(yaw = 0)
    rm.set_motor_power(power)
    

def test_forward(rm, power = 0.5):
    #forward
    power = RCIOPowerNormalized(forward = power)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #forward stop
    power.set(forward = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #backward
    power.set(forward = -1*power)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #backward stop
    power.set(forward = 0)
    rm.set_motor_power(power)
    

def test_lateral(rm, power = 0.5):
    #strafe right?
    power = RCIOPowerNormalized(lateral = 0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #strafe stop
    power.set(lateral = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #strafe left?
    power.set(lateral = -0.5)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #strafe stop
    power.set(lateral = 0)
    rm.set_motor_power(power)

def signal_handler(signal, frame):
    disarm()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

rospy.init_node('sdrcauv_main')
mavros.set_namespace()

rm = RawMovement()

arm()
test_forward(rm, 0.1)
disarm()
