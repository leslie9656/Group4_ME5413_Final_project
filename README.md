# ME5413_Final_Project

NUS ME5413 autonomous mobile robotics final project
>Authors: Chen chunyu, Dong haoyu, Wang yongyuan, Su zhuoqun

![Ubuntu 20.04](https://img.shields.io/badge/OS-Ubuntu_20.04-informational?style=flat&logo=ubuntu&logoColor=white&color=2bbc8a)
![ROS Noetic](https://img.shields.io/badge/Tools-ROS_Noetic-informational?style=flat&logo=ROS&logoColor=white&color=2bbc8a)
![C++](https://img.shields.io/badge/Code-C++-informational?style=flat&logo=c%2B%2B&logoColor=white&color=2bbc8a)
![Python](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=Python&logoColor=white&color=2bbc8a)
![GitHub Repo stars](https://img.shields.io/github/stars/NUS-Advanced-Robotics-Centre/ME5413_Final_Project?color=FFE333)
![GitHub Repo forks](https://img.shields.io/github/forks/NUS-Advanced-Robotics-Centre/ME5413_Final_Project?color=FFE333)

## Dependencies

* System Requirements:
  * Ubuntu 20.04 (18.04 not yet tested)
  * ROS Noetic (Melodic not yet tested)
  * C++11 and above
  * CMake: 3.0.2 and above
* This repo depends on the following standard ROS pkgs:
  * `roscpp`
  * `rospy`
  * `rviz`
  * `std_msgs`
  * `nav_msgs`
  * `geometry_msgs`
  * `visualization_msgs`
  * `tf2`
  * `tf2_ros`
  * `tf2_geometry_msgs`
  * `pluginlib`
  * `map_server`
  * `gazebo_ros`
  * `jsk_rviz_plugins`
  * `jackal_gazebo`
  * `jackal_navigation`
  * `velodyne_simulator`
  * `teleop_twist_keyboard`
  * `point_cloud_to_laser_scan` 
  * `EVO`
* And this [gazebo_model](https://github.com/osrf/gazebo_models) repositiory


## Installation

Note: Before you start this work, please install ROS. Installation the ROS following the Installation/Upgrade in [ROS](http://wiki.ros.org/noetic/Installation/Ubuntu)


This repo is a ros workspace, containing three rospkgs:

* `interactive_tools` are customized tools to interact with gazebo and your robot
* `jackal_description` contains the modified jackal robot model descriptions
* `me5413_world` the main pkg containing the gazebo world, and the launch files

### Installation of the ME5413_Final_Project

After forking this repo to your own github:

```bash
cd
git clone https://github.com/<YOUR_GITHUB_USERNAME>/ME5413_Final_Project.git
cd ME5413_Final_Project

#update
sudo apt update

# Install all dependencies
rosdep install --from-paths src --ignore-src -r -y

# Build
catkin_make
# Source 
source devel/setup.bash
```

To properly load the gazebo world, you will need to have the necessary model files in the `~/.gazebo/models/` directory.

There are two sources of models needed:

* [Gazebo official models](https://github.com/osrf/gazebo_models)
  
  ```bash
  # Create the destination directory
  cd
  mkdir -p .gazebo/models

  # Clone the official gazebo models repo (assuming home here `~/`)
  git clone https://github.com/osrf/gazebo_models.git

  # Copy the models into the `~/.gazebo/models` directory
  cp -r ~/gazebo_models/* ~/.gazebo/models
  ```

* [Our customized models](https://github.com/NUS-Advanced-Robotics-Centre/ME5413_Final_Project/tree/main/src/me5413_world/models)

  ```bash
  # Copy the customized models into the `~/.gazebo/models` directory
  cp -r ~/ME5413_Final_Project/src/me5413_world/models/* ~/.gazebo/models
  ```
  
### Installation of EVO
  
  Installation the Evo tool following the Installation/Upgrade in [EVO](https://github.com/MichaelGrupp/evo)

  Note: If the evo command like evo_ape can not be used after installation, restarting your computer may deal with the problem.

## Usage

### Gazebo world

  Type followed code in terminal:

```bash
 roscore
 # open the gazebo world together with our robot
 cd
 cd ME5413_Final_Project
 source devel/setup.bash
 roslaunch me5413_world world.launch

```

### Mapping

Then open second terminal:

```bash
#start mapping-learning
cd
cd ME5413_Final_Project
source devel/setup.bash
roslaunch me5413_world mapping.launch
```

You can control the robot when you keep the second terminal open.
Or you can input code at another terminal:

```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

Then you can record the process of movement at new terminal:

* you may check the topics you open, you may not record all sensor'data

```bash
# sensor1 and sensor2 are sensors you want to record
cd
rosbag record -O my_data.bag /sensor1 /sensor2
```

After you finishing mapping, run the following command in the third terminal to save the map:

```bash
roscd me5413_world/maps/
rosrun map_server map_saver -f my_map map:=/map
```
Then you return the terminal of recording, click ctrl+c and save bag. The bag should save at you /home. 


You get the result of mapping. Then you can quit the mapping process.

Then you can open the EVO:
```bash
# <bag_file> is your bag name, and <topic_name> is the topic you use, like laser_scan. 
evo_traj bag <bag_file> <topic_name>
```

### Navigation

Open new terminal or keep second terminal:

```bash
# Start the navigation
roslaunch me5413_world navigation.launch
```

## Improvement of project

### 1. Improvement of Mapping
Like the second test, we obtain the new data by the 3D-lidar (project to 2D-lidar) and new imu sensor and record them into 3333.bag. In this test, the RMSE is 0.336, which is the smallest among three tests. The victual result show that the whole trajectory is most accurate. 


### 2. Improvement of navigation


## Contribution

We are following:

* [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html),
* [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#main),
* [ROS C++ Style Guide](http://wiki.ros.org/CppStyleGuide)

## License

The [ME5413_Final_Project](https://github.com/NUS-Advanced-Robotics-Centre/ME5413_Final_Project) is released under the [MIT License](https://github.com/NUS-Advanced-Robotics-Centre/ME5413_Final_Project/blob/main/LICENSE)
