from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Launch Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': open('/home/srushtei/ros2_ws/src/my_robot_arm/urdf/my_robot.urdf', 'r').read()
            }]
        ),
        
        # Launch Joint State Publisher
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen'
        ),
        
        # Launch Gazebo server
        ExecuteProcess(
            cmd=['/usr/bin/gzserver', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        
        # Launch Gazebo client
        ExecuteProcess(
            cmd=['/usr/bin/gzclient'],
            output='screen'
        ),
        
        # Launch MoveIt move_group node
        Node(
            package='moveit_ros_move_group',
            executable='move_group',
            name='move_group',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                {'robot_description': open('/home/srushtei/ros2_ws/src/my_robot_arm/urdf/my_robot.urdf', 'r').read()},
                {'robot_description_semantic': open('/home/srushtei/ros2_ws/src/my_robot_arm/config/moveit_config.yaml', 'r').read()}
            ]
        ),
        
        # Launch RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/home/srushtei/ros2_ws/src/my_robot_arm/config/moveit.rviz']
        ),
    ])


