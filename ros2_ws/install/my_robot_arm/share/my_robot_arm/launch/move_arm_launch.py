from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Load the URDF file
    urdf_file_path = '/home/srushtei/ros2_ws/src/my_robot_arm/urdf/my_robot.urdf'
    
    with open(urdf_file_path, 'r') as file:
        robot_description = file.read()
    
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
            package='my_robot_arm',
            executable='move_arm_node',
            output='screen',
            parameters=[{'robot_description': robot_description, 'robot_description_semantic': '</home/srushtei/ros2_ws/src/my_robot_arm/srdf/my_robot.srdf >'}],
        ),
    ])

