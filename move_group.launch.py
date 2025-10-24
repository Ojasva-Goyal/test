from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os
def generate_launch_description():
    this_dir = os.path.dirname(__file__)
    config_dir = os.path.join(this_dir, '..', 'config')
    urdf = os.path.join(config_dir, 'robot_description.urdf')
    # This launch file is a placeholder. Use move_group from MoveIt2 with your workspace.
    return LaunchDescription([])
