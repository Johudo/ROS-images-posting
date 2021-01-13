# ROS images posting from webcam

Start:

```bash
cd ~/catkin_ws
catkin_create_pkg <folder> image_transport cv_bridge sensor_msgs rospy roscpp std_msgs
mv <this_project> <folder>
catkin_make
roscd <folder>
roslaunch <folder> images_posting.launch
```
