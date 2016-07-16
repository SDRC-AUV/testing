import rospy
import mavros
import mavros_msgs.msg
import mavros_msgs.srv


def set_mode(mode):
    modes = ["ACRO", "STABILIZE", "ALT_HOLD", "AUTO",
             "CIRCLE", "LOITER", "GUIDED", "LAND", "RTL",
             "DRIFT", "SPORT", "FLIP", "AUTOTUNE", "POSHOLD",
             "BRAKE", "THROW"]

    if mode not in modes:
        return False

    mavros.set_namespace()
    ret = rospy.ServiceProxy(mavros.get_topic('set_mode'), mavros_msgs.srv.SetMode).call(0, mode)
    return ret.success

def set_rcio_mode(idx):
    return False
    mavros.set_namespace()
    publisher = rospy.Publisher('/mavros/rc/override', mavros_msgs.msg.OverrideRCIn)
    mode_msg = mavros_msgs.msg.OverrideRCIn()

    #fix this
    modes = {1:1000, 2:1100, 3:1200,
             4:1300, 5:1400, 6:1500}

    mode = modes[idx] 

    mode_msg.channels = [0, 0, 0, 0, mode, 0, 0, 0]

    ret = publisher.publish(mode_msg)
    return ret.success