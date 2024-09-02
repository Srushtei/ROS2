#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class SineTrajectoryNode(Node):
    def __init__(self):
        super().__init__('sine_trajectory_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_velocity)
        self.time_elapsed = 0.0
        self.amplitude = 0.5  # Amplitude of the sine wave
        self.frequency = 0.1  # Frequency of the sine wave

    def publish_velocity(self):
        velocity_msg = Twist()

        # Calculate linear and angular velocity
        linear_velocity = 0.2  # Constant forward velocity
        angular_velocity = self.amplitude * math.sin(2 * math.pi * self.frequency * self.time_elapsed)

        velocity_msg.linear.x = linear_velocity
        velocity_msg.angular.z = angular_velocity

        self.publisher_.publish(velocity_msg)

        self.time_elapsed += 0.1
        if self.time_elapsed > 1000:
            self.time_elapsed = 0.0

def main(args=None):
    rclpy.init(args=args)
    node = SineTrajectoryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
