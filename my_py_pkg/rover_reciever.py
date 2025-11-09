#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Reciver(Node):
    def __init__(self):
        super().__init__('rover_reciever')
        self.subsriber=self.create_subscription(String,"topic_900MHZ",self.callback_GHSmessage,10)
        
    
    def callback_GHSmessage(self,msg:String):
        self.get_logger().info(msg.data)

    



def main(args=None):
    rclpy.init(args=args)
    node=Reciver()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="main":
    main()
