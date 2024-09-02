import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/srushtei/ros2_ws/src/turtlebot_sine_trajectory/install/turtlebot_sine_trajectory'
