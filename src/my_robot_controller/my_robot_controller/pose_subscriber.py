#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):

    def __init__(self):
        super().__init__("pose_subscriber")  # we pass in the node name as a string. Its because ros needs the name of the node. If the quotes are removed then it is simply a variable and not a node
        self.pose_subscriber = self.create_subscription(
             Pose, "/turtle1/pose", self.pose_callback, 10)     # format for creating a subscriber (datatype, topic_name, callback, que_size)
        
    def pose_callback(self, msg: Pose):
        self.get_logger().info("(" + str(msg.x) + "," + str(msg.y) + ")")

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()