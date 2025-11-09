#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Yaggi_GroundStationnode(Node):
    def __init__(self):
        super().__init__('GroundStation_publisher')
        self.publisher_=self.create_publisher(String,"topic_900MHZ",10)
        self.timer_=self.create_timer(0.5,self.publish_news)
        self.get_logger().info("CONNECTION SECURED BETWEEN ROVER AND GS")
    def publish_news(self):
        msg=String()
        msg.data="SENDING SENSOR DATA TO ROVER"
        self.publisher_.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node=Yaggi_GroundStationnode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="main":
    main()
