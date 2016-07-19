from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
	packages=['triton'],
	package_dir={'':'src'},
	requires=['roscpp', 'rospy', 'std_msgs', 'cv_bridge', 'mavros', 'usb_cam']
)

setup(**setup_args)
