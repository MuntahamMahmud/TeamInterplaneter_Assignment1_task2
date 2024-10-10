#!/usr/bin/env python3


import rospy
from std_msgs.msg import String


class SaveDirection():
    def __init__(self):
        rospy.init_node("command_history",anonymous=True)
        rospy.Subscriber("commandtopic",String,self.callback)
        self.Command=[]
    
    def callback(self,data):
        rospy.loginfo(f"Received Command is {data.data}")
        self.Command.append(data.data)
    def run(self):
        rospy.spin()

if __name__=="__main__":
    node=SaveDirection()
    node.run()


