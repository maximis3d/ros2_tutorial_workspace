import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/max/University/Robotics and Automation/week2/workshop/ros2_tutorial_workspace/install/the_simplest_python_package'
