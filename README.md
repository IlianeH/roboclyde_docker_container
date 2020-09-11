# roboclyde_docker_container

## Contains scripts for ERC 2020 RoboClyde team

#### Note: All data from rover is saved into the /home/roboclyde_out directory on the rover

##### 1: save the roboclyde_docker_container folder into /catkin_ws/src directory

##### 2: run catkin_make from /catkin_ws directory

##### 3: run the following code:


source /catkin_ws/devel/setup.bash

echo "source /catkin_ws/devel/setup.bash" >> /etc/bash.bashrc

echo "ROS_IP=${ROS_IP}" >> /etc/environment

echo "ROS_MASTER_URI=${ROS_MASTER_URI}" >> /etc/environment

chmod +x /catkin_ws/src/roboclyde_docker_container/scripts/*

##### 4: finally to start the image and coordinate saver nodes run:

roslaunch roboclyde_docker_container startup.launch


rover link:

curl -sSf "https://api.freedomrobotics.ai/accounts/AA7D5795801DBD3F956B6A9B1/devices/D9DD039A8E6B55369B0BCABA934/installscript?mc_token=T79f86da4031d82b3fd61d34f&mc_secret=Sa56b1d2703dbc1707ba799f8&install_elements=webrtc&auto_install_deps=true&ppa_is_allowed=true" | python


##### 5: To take pictures from rover manually, in pilot mode press 'c' then press '1'
