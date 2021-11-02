# Universal Robot URDF Wrapper

Goal of this package is to create URDF files of the URx and URxe arms for using in simulations like PyBullet etc. For this the universal robot ROS package is used and all important files are wrapped to a new directory.



Tested under:

- Ubuntu 20.04
- ROS noetic installation



To create the new data model, proceed as follows:

```bash
# create a new dummy ROS workspace
mkdir -p ~/dummy_ws/src
cd ~/dummy_ws
catkin init

cd ~/dummy_ws/src/
# clone the universal robot package
git clone -b melodic-devel https://github.com/ros-industrial/universal_robot.git

# clone the wrapper package
git clone https://github.com/GeorgJohn/universal_robot_urdf_wrapper.git

# build your ROS workspace
cd ~/dummy_ws
catkin build

# wrap the arm models 
cd ~/dummy_ws/src/universal_robot_urdf_wrapper
. main.sh
```



The new model data can than be found under: ``` ~/dummy_ws/src/UniversalRobotModelDescription/```
