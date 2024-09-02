import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from pynput import keyboard

class KeyboardControl(Node):
    def __init__(self):
        super().__init__('keyboard_control')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.twist = Twist()
        self.speed = 0.5
        self.deceleration = 0.1
        self.create_timer(0.1, self.timer_callback)
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def timer_callback(self):
        self.publisher_.publish(self.twist)

    def on_press(self, key):
        try:
            if key.char == 'w':
                self.twist.linear.x = self.speed
            elif key.char == 's':
                self.twist.linear.x = -self.speed
            elif key.char == 'a':
                self.twist.angular.z = self.speed
            elif key.char == 'd':
                self.twist.angular.z = -self.speed
        except AttributeError:
            pass

    def on_release(self, key):
        if key.char in ['w', 's']:
            self.twist.linear.x = 0
        elif key.char in ['a', 'd']:
            self.twist.angular.z = 0

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
