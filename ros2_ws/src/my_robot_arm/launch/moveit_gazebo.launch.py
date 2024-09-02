import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        # Launch Gazebo server
        launch.actions.ExecuteProcess(
            cmd=['/usr/bin/gzserver', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        # Launch Gazebo client
        launch.actions.ExecuteProcess(
            cmd=['/usr/bin/gzclient'],
            output='screen'
        ),

        # Launch robot_state_publisher
        launch_ros.actions.Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': open('/home/srushtei/ros2_ws/src/my_robot_arm/urdf/my_robot.urdf').read()
            }]
        ),

        # Launch MoveIt move_group node
        launch_ros.actions.Node(
            package='moveit_ros_move_group',
            executable='move_group',
            name='move_group',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                {'robot_description': open('/home/srushtei/ros2_ws/src/my_robot_arm/urdf/my_robot.urdf').read()},
                {'robot_description_semantic': open('/home/srushtei/ros2_ws/src/my_robot_arm/srdf/my_robot.srdf').read()}
            ]
        ),

        # Launch RViz2
        launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/home/srushtei/ros2_ws/src/my_robot_arm/config/moveit_config.rviz']
        ),
    ])

