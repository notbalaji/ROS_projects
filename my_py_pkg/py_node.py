#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Mynode(Node):
    def __init__(self):
        super().__init__('py_node')
        self.get_logger().info("hello")



def main(args=None):
    rclpy.init(args=args)
    node=Mynode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="main":
    main()
