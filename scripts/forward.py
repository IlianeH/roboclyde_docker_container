#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def forward():
	rospy.init_node('move_forward',anonymous=True)
	velocity_publisher = rospy.Publisher('/controllers/diff_drive/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	
	# Rover speed (m/s)
	speed = input("Desired rover speed: ")
	# Distance for rover to move forward (m)
	distance = input("Desired rover distance: ")
	
	# Only linear X and angular Z are important
	vel_msg.linear.x = speed
	vel_msg.angular.z = 0
	
	# Remaining linear and angular velocities are ignored
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	
	# Keep running until it is stopped
	while not rospy.is_shutdown():
		# Get simulation time
		t0 = rospy.Time.now().to_sec()
		
		# Moving from when run
		current_distance = 0
		
		while(current_distance < distance):
			# Send desired velocity
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			# Assuming no loss
			current_distance = speed*(t1-t0)
		
		# After loop has ended, stop rover
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		velocity_publisher.publish(vel_msg)
		
if __name__ == '__main__':
	try:
  		#Testing our function
  		forward()
  	except rospy.ROSInterruptException: pass


