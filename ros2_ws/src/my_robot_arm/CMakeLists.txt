cmake_minimum_required(VERSION 3.8)
project(my_robot_arm)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(moveit_ros_move_group REQUIRED)
find_package(moveit_ros_visualization REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rviz2 REQUIRED)

include_directories(include
  ${rclcpp_INCLUDE_DIRS}
  ${moveit_ros_planning_interface_INCLUDE_DIRS}
  ${gazebo_ros_INCLUDE_DIRS}
)

# Add executables and dependencies here
add_executable(move_arm_node src/move_arm_node.cpp)

install(
  PROGRAMS
  scripts/moveit_control.py
    DESTINATION lib/my_robot_arm
)

install(
  DIRECTORY urdf/
  DESTINATION share/my_robot_arm/urdf
)


# Install launch files
install(DIRECTORY
  launch/
  DESTINATION share/my_robot_arm/launch
)

install(TARGETS
  move_arm_node
  DESTINATION lib/${PROJECT_NAME})


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()
ament_target_dependencies(move_arm_node rclcpp moveit_core moveit_ros_planning moveit_ros_planning_interface)

ament_package()
