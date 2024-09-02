#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>

class MoveArm : public rclcpp::Node
{
public:
  static std::shared_ptr<MoveArm> create()
  {
    auto node = std::shared_ptr<MoveArm>(new MoveArm());
    node->initializeMoveGroup();
    return node;
  }

  void initializeMoveGroup()
  {
    move_group_ = std::make_shared<moveit::planning_interface::MoveGroupInterface>(shared_from_this(), "arm");
    move_group_->setPoseReferenceFrame("base_link");

    geometry_msgs::msg::Pose target_pose;
    target_pose.orientation.w = 1.0;
    target_pose.position.x = 0.4;
    target_pose.position.y = 0.1;
    target_pose.position.z = 0.4;
    move_group_->setPoseTarget(target_pose);

    auto success = move_group_->move();
    if (success) {
      RCLCPP_INFO(this->get_logger(), "Motion plan executed successfully");
    } else {
      RCLCPP_ERROR(this->get_logger(), "Motion plan failed");
    }
  }

private:
  MoveArm() : Node("move_arm") {}
  std::shared_ptr<moveit::planning_interface::MoveGroupInterface> move_group_;
};

#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>

int main(int argc, char** argv)
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("move_arm");

  // Declare parameter and get its value
  std::string robot_description;
  node->declare_parameter("robot_description", "");
  node->get_parameter("robot_description", robot_description);

  if (robot_description.empty()) {
    RCLCPP_ERROR(node->get_logger(), "Robot description parameter not found!");
    return 1;
  }

  RCLCPP_INFO(node->get_logger(), "Robot description loaded successfully.");

  moveit::planning_interface::MoveGroupInterface move_group(node, "arm");

  // Your motion planning and execution code here...

  rclcpp::shutdown();
  return 0;
}

