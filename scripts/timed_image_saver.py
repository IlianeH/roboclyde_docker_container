#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import os

bridge = CvBridge()

def image_callback(msg):
    global imageNo
    print("Received an image!")
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        time = msg.header.stamp
        cv2.imwrite('Timed_Image_'+str(imageNo)+'.jpeg', cv2_img)
        # Waits for specified seconds
        rospy.sleep(10.)
        imageNo = imageNo + 1

def main():
    global imageNo
    # Make folder if it doesnt exist
    os.chdir("/home")
    if not os.path.exists("roboclyde_out"):
        os.mkdir("roboclyde_out")
    os.chdir("roboclyde_out")
    if not os.path.exists("Timed_Images"):
        os.mkdir("Timed_Images")
    os.chdir("Timed_Images")
    rospy.init_node('image_listener')
    image_topic = "/zed2/left/image_rect_color"
    imageNo = 1
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
