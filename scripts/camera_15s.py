#! /usr/bin/python
# Copyright (c) 2015, Rethink Robotics, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
# new cleaner format to name images in readable timestamps
from datetime import datetime
# os to make sure images directory is created if not avaialable
import os

os.chdir("/home")
if not os.path.exists("roboclyde_out"):
    os.makedirs("roboclyde_out")
os.chdir("roboclyde_out")

if not os.path.exists("Images"):
    os.makedirs("Images")
os.chdir("Images")

if not os.path.exists('Hazcam'):
    os.makedirs('Hazcam')
    print('Folders for Hazcam images created')

if not os.path.exists('Zed2_Right'):
    os.makedirs('Zed2_Right')
    print('Folders for Zed 2 Right camera images created')

if not os.path.exists('Zed2_Left'):
    os.makedirs('Zed2_Left')
    print('Folders for Zed 2 Left camera images created')

# Instantiate CvBridge
bridge = CvBridge()

print("Image time stamps are in 'dd-mm-yyyy hh-mm-ss' format")

def image_callback_Haz(msg):
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg
        time = msg.header.stamp
        #new timestamps
        timestamp = datetime.now()
        timestamp_string = timestamp.strftime("%d-%m-%Y_%H-%M-%S")
        cv2.imwrite('Hazcam/'+timestamp_string+'.jpeg', cv2_img)

def image_callback_Z2R(msg):
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg
        time = msg.header.stamp
        #new timestamps
        timestamp = datetime.now()
        timestamp_string = timestamp.strftime("%d-%m-%Y_%H-%M-%S")
        cv2.imwrite('Zed2_Right/'+timestamp_string+'.jpeg', cv2_img)

def image_callback_Z2L(msg):
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg
        time = msg.header.stamp
        #new timestamps
        timestamp = datetime.now()
        timestamp_string = timestamp.strftime("%d-%m-%Y_%H-%M-%S")
        cv2.imwrite('Zed2_Left/'+timestamp_string+'.jpeg', cv2_img)
        rospy.sleep(15.)

def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic_Haz = "/camera/image_raw"
    image_topic_Z2R = "/zed2/right/image_rect_color"
    image_topic_Z2L = "/zed2/left/image_rect_color"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic_Haz, Image, image_callback_Haz)
    rospy.Subscriber(image_topic_Z2R, Image, image_callback_Z2R)
    rospy.Subscriber(image_topic_Z2L, Image, image_callback_Z2L)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
