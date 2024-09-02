# File: ~/ros2_ws/src/my_robot_arm/launch/moveit_rviz.launch.py

import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        # Launch the MoveIt planning node using the correct package
        launch_ros.actions.Node(
            package='moveit_ros_move_group',
            executable='move_group',
            name='move_group',
            output='screen',
            parameters=[
                {'robot_description': '</home/srushtei/ros2_ws/src/my_robot_arm/urdf/my_robot.urdf>',
                 'robot_description_semantic': '</home/srushtei/ros2_ws/src/my_robot_arm/srdf/my_robot.srdf>',
                 'use_sim_time': True}
            ],
        ),
        
        # Launch RViz2
        launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/home/srushtei/ros2_ws/src/my_robot_arm/config/moveit_rviz_config.rviz']
        ),
    ])

