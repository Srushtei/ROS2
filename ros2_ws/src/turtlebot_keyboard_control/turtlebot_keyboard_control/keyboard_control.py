import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class KeyboardControl(Node):
    def __init__(self):
        super().__init__('keyboard_control')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.declare_parameter('linear_speed', 0.1)
        self.declare_parameter('angular_speed', 0.1)

    def timer_callback(self):
        twist = Twist()
        twist.linear.x = self.get_parameter('linear_speed').get_parameter_value().double_value
        twist.angular.z = self.get_parameter('angular_speed').get_parameter_value().double_value
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

