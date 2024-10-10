#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

class ObstacleIdentifier:
    def __init__(self):
        rospy.init_node("obstacle_identifier", anonymous=True)
        self.pub = rospy.Publisher("/obstacle", String, queue_size=10)
        rospy.Subscriber("/scan", LaserScan, self.laser_callback)

    def laser_callback(self, msg):
        
        obstacle_found = False
        
        
        for distance in msg.ranges:
            if distance > 0 and distance < 30.0:
                obstacle_found = True
                break 

        if obstacle_found:
            obstacle_message = "Obstacle Found"
            rospy.loginfo(obstacle_message)
            self.pub.publish(String(data=obstacle_message))

    def run(self):
        rospy.spin()  

if __name__ == "__main__":
    node = ObstacleIdentifier()
    node.run()

