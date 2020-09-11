#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

import tty
import sys
import termios
import signal

orig_settings = termios.tcgetattr(sys.stdin)

def keyboardInterruptHandler(signal, frame):
	print("Caught interrupt")
	resetTerminal()
	exit(0)

def resetTerminal():
	tty.tcsetattr(sys.stdin, tty.TCSAFLUSH, orig_settings)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

def controlls(letter,vel_msg,speed_l_f,speed_l_b,speed_a,vel_pub):
	if (letter == "w"):
		forwards(vel_msg,speed_l_f,vel_pub)
	elif (letter == "s"):
		backwards(vel_msg,speed_l_b,vel_pub)
	elif (letter == "a"):
		left(vel_msg,speed_a,vel_pub)
	elif (letter == "d"):
		right(vel_msg,speed_a,vel_pub)
	elif (letter == "b"):
		stop(vel_msg,vel_pub)
	else:
		return

def forwards(vel_msg,speed,vel_pub):
	vel_msg.linear.x = speed
	vel_msg.angular.z = 0
	vel_pub.publish(vel_msg)

def backwards(vel_msg,speed,vel_pub):
	vel_msg.linear.x = speed * -1
	vel_msg.angular.z = 0
	vel_pub.publish(vel_msg)

def left(vel_msg,speed,vel_pub):
	vel_msg.linear.x = 0
	vel_msg.angular.z = speed
	vel_pub.publish(vel_msg)

def right(vel_msg,speed,vel_pub):
	vel_msg.linear.x = 0
	vel_msg.angular.z = speed * -1
	vel_pub.publish(vel_msg)

def stop(vel_msg,vel_pub):
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	vel_pub.publish(vel_msg)

def main():
	rospy.init_node('move_forward',anonymous=True)
	velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	linear_velocity_forwards = 10 	# (m/s)
	linear_velocity_backwards = 5 	# (m/s)
	angular_velocity = 5		# (rad/s)

	# Initialising the data to send to rover
	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0


	tty.setcbreak(sys.stdin)
	x = 0

	print("Press Esc or Ctrl C to exit...")
	print("<--------------- Use the 'wasd' keys to control the rover, press 'b' to brake ---------------->")
	while x != '\x1b':	# Esc key
		x = sys.stdin.read(1)[0]
		controlls(x,vel_msg,linear_velocity_forwards,linear_velocity_backwards,angular_velocity,velocity_publisher)
	resetTerminal()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
