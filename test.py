import time
import signal
import sys
from rawmovement import *

def test_pitch(rm, p = 0.5):
    #pitch up?
    power = RCIOPowerNormalized(pitch = p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #pitch stop
    power.set(pitch = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #pitch down
    power.set(pitch = -1*p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #pitch stop
    power.set(pitch = 0)
    rm.set_motor_power(power)

def test_roll(rm, p = 0.5):
    #roll right?
    power = RCIOPowerNormalized(roll = p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #roll stop
    power.set(roll = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #roll left?
    power.set(roll = -1*p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #roll stop
    power.set(roll = 0)
    rm.set_motor_power(power)
    
def test_yaw(rm, p = 0.5):
    #yaw right?
    power = RCIOPowerNormalized(yaw = p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #yaw stop
    power.set(yaw = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #yaw left?
    power.set(yaw = -1*p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #yaw stop
    power.set(yaw = 0)
    rm.set_motor_power(power)
    

def test_forward(rm, p = 0.5):
    #forward
    power = RCIOPowerNormalized(forward = p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #forward stop
    power.set(forward = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #backward
    power.set(forward = -1*p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #backward stop
    power.set(forward = 0)
    rm.set_motor_power(power)
    

def test_lateral(rm, p = 0.5):
    #strafe right?
    power = RCIOPowerNormalized(lateral = p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #strafe stop
    power.set(lateral = 0)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #strafe left?
    power.set(lateral = -1*p)
    rm.set_motor_power(power)
    time.sleep(0.5)

    #strafe stop
    power.set(lateral = 0)
    rm.set_motor_power(power)

def signal_handler(signal, frame):
    disarm()
    sys.exit(0)


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


signal.signal(signal.SIGINT, signal_handler)

rospy.init_node('sdrcauv_main')
mavros.set_namespace()

rm = RawMovement()


zero_power = RCIOPowerNormalized()

arm()

for i in range(5):
    ch = getch()
    channels = [0, 0, 0, 0, 0, 0]
    channels[int(ch)-1] = 0.1

    power = RCIOPowerNormalized(*channels)
    rm.set_motor_power(power)
    rospy.sleep(3)
    rm.set_motor_power(zero_power)
disarm()
