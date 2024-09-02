import rclpy
from rclpy.node import Node
from moveit_commander import RobotCommander, PlanningSceneInterface, MoveGroupCommander

class MoveitControlNode(Node):
    def __init__(self):
        super().__init__('moveit_control_node')
        rclpy.init()

        self.robot = RobotCommander()
        self.scene = PlanningSceneInterface()
        self.group = MoveGroupCommander("arm")

        self.move_arm_to_point([0.5, 0.5, 0.5])

    def move_arm_to_point(self, target_position):
        self.group.set_target(target_position)
        plan = self.group.go(wait=True)
        self.group.stop()
        self.group.clear_pose_targets()

def main(args=None):
    rclpy.init(args=args)
    node = MoveitControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
