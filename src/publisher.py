#!/usr/bin/env python2.7
import rospy
import cv2 

from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images

def publish_message():
 
    pub = rospy.Publisher('video_frames', Image, queue_size=10)
    rospy.init_node('video_pubisher')

    rate = rospy.Rate(10) # 10 frames in second
    
    cap = cv2.VideoCapture(0)
    
    # Used to convert between ROS and OpenCV images
    br = CvBridge()
 
    while not rospy.is_shutdown():
        ret, frame = cap.read()

        if ret == True:
            rospy.loginfo('Publishing video frame')
            
            # The 'cv2_to_imgmsg' method converts an OpenCV
            # image to a ROS image message
            pub.publish(br.cv2_to_imgmsg(frame))
            rate.sleep()
    

if __name__ == '__main__':
    publish_message()