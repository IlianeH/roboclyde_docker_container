#!/usr/bin/env python
import rospy
import tf
import math
from nav_msgs.msg import Odometry


def callback(msg):
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    angX = msg.pose.pose.orientation.x
    angY = msg.pose.pose.orientation.y
    angZ = msg.pose.pose.orientation.z
    odom_quat = tf.transformations.quaternion_from_euler(0.0, 0.0, angZ)
    br.sendTransform((x, y, z),
                    odom_quat,
                    rospy.Time.now(),
                    "base_link",
                    "odom")
    rate.sleep()



if __name__ == '__main__':
    rospy.init_node('tf_world_to_rover')
    rospy.Subscriber("/zed2/odom",Odometry,callback)
    rospy.spin()
