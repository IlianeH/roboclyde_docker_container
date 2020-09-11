#!/usr/bin/env python
import rospy
import csv
from nav_msgs.msg import Odometry
from datetime import datetime
import os
import time
import signal
import sys
from geometry_msgs.msg import PoseWithCovarianceStamped,PoseStamped

def signal_handler(sig, frame):
    print('Saving and exiting...')
    write_to_file
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def write_to_file():
    global xArray
    global yArray
    global tArary
    global zArray

    f = open("Timed_Coordinates.csv","a+")
    try:
        writer = csv.writer(f)
        for i in range(len(xArray)):
            writer.writerow([tArray[i],xArray[i],yArray[i]],zArray[i])
    finally:
        f.close()

def callback(data):
    global xArray
    global yArray
    global tArray
    global zArray
    global second

    recorded_second = datetime.now().strftime("%S")
    if not recorded_second == second:
        second = recorded_second

        pose = PoseStamped()

        pose.pose.position.x = float(data.pose.pose.position.x)
        pose.pose.position.y = float(data.pose.pose.position.y)
        pose.pose.position.z = float(data.pose.pose.position.z)
        t = datetime.now().strftime("%H:%M:%S")

        xArray.append(pose.pose.position.x)
        yArray.append(pose.pose.position.y)
        tArray.append(t)
        zArray.append(pose.pose.position.z)

        if len(xArray) > 10:
            write_to_file()
            xArray = []
            yArray = []
            tArray = []
            zArray = []

def main():
    global xArray
    global yArray
    global tArray
    global zArray
    global second

    second = datetime.now().strftime("%S")

    xArray = []
    yArray = []
    tArray = []
    zArray = []
    os.chdir("/home")
    if not os.path.exists("roboclyde_out"):
        os.mkdir("roboclyde_out")
    os.chdir("roboclyde_out")
    create_datetime = "pos_data" + datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    if not os.path.exists(create_datetime):
        os.mkdir(create_datetime)
    os.chdir(create_datetime)
    f = open("Timed_Coordinates.csv","w+")
    try:
        writer = csv.writer(f)
        writer.writerow(("Date_Time","x (m)", "y (m)", "z (m)"))
    finally:
        f.close()

    msg = Odometry()
    rospy.init_node("coordinate_saver")
    msg = rospy.Subscriber("/zed2/odom", Odometry, callback)
    rospy.spin()
    rate = rospy.Rate(10)
    rate.sleep

if __name__ == "__main__":
    main()
