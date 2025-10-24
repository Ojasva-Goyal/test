from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os
def generate_launch_description():
    rviz_cfg = os.path.join(os.path.dirname(__file__), '..', 'config', 'moveit.rviz')
    return LaunchDescription([ExecuteProcess(cmd=['rviz2','-d',rviz_cfg])])
