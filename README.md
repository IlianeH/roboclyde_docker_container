# roboclyde_docker_container

Contains scripts for ERC 2020 RoboClyde team

clone into /catkin_ws/src directory
run catkin_make from /catkin_ws directory
run the following code:

source /catkin_ws/devel/setup.bash

echo "source /catkin_ws/devel/setup.bash" >> /etc/bash.bashrc
echo "ROS_IP=${ROS_IP}" >> /etc/environment
echo "ROS_MASTER_URI=${ROS_MASTER_URI}" >> /etc/environment

chmod +x /catkin_ws/src/roboclyde_docker_container/scripts/*

and finally to start the image and coordinate saver nodes run:

roslaunch roboclyde_docker_container startup.launch
