#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

class turtlebot:
    def __init__(self):
        rospy.init_node("position_turtle",anonymous=True)
        self.pub=rospy.Publisher("/turtle_pos_xy",String,queue_size=10)
        rospy.Subscriber("/odom",Odometry,self.clbk)
        self.x=0.0
        self.y=0.0
       
        

    def clbk (self,msg):
       
        coordinates=Odometry()
        self.x=msg.pose.pose.position.x
        self.y=msg.pose.pose.position.y
        rospy.loginfo(f"received coordinates {self.x} & {self.y}")

    def publish_position(self):
        position_message=f"Current Position: x={self.x} , y={self.y}"
        self.pub.publish(String(data=position_message))
        

    def run(self):
        rate=rospy.Rate(0.2)
        while not rospy.is_shutdown():
            position_message=f"Current Position: x={self.x} , y={self.y}"
            self.pub.publish(String(data=position_message))
            rate.sleep()

        

if __name__=="__main__":
    node=turtlebot()
    node.run()
