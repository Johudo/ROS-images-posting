#!/usr/bin/env python2.7
import rospy
import cv2

from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
 
def getting_image_callback(data):
 
    # Used to convert between ROS and OpenCV images
    br = CvBridge()

    rospy.loginfo("Receiving video frame")
    
    # Convert ROS Image message to OpenCV image
    current_frame = br.imgmsg_to_cv2(data)
    
    cv2.imshow("camera", current_frame)
    cv2.waitKey(1)

    
def receive_images():
    rospy.init_node('video_subscriber')
    rospy.Subscriber('video_frames', Image, getting_image_callback)
 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    receive_images()