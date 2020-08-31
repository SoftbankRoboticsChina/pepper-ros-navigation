#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
import socket
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class Socket2topic:
    def __init__(self):
        print "2222"
        self.HOST = "192.168.3.10"
        self.PORT = 5000
        print "2222"
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print "2222"
        self.mySocket.bind((self.HOST, self.PORT))
        print "2222"
        self.pepper2nav_pub = rospy.Publisher('/nav2pepper', String, queue_size=1)
    def sock_spin(self):
        while 1:
            packet, address = self.mySocket.recvfrom(1024)
            print packet
            self.pepper2nav_pub.publish(packet)


if __name__ == "__main__":
    rospy.init_node("Socket2topic")
    ss = Socket2topic()
    ss.sock_spin()
    rospy.spin()

