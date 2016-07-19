cmake_minimum_required(VERSION 2.8.3)

project(triton)

find_package(catkin REQUIRED
roscpp 
rospy 
std_msgs 
cv_bridge 
mavros 
usb_cam)

catkin_python_setup()

catkin_package()

include_directories(
	${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
	scripts/between.py
	scripts/norm_to_pwm.py
	scripts/pwm_to_norm.py
	scripts/set_RCIOPower.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

