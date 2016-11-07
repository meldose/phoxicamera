# phoxi_camera

This package enables interfacing Photoneo PhoXi 3D Scanner/Camera from ROS.  

<img src="http://www.photoneo.com/wp-content/uploads/2016/04/0003_5.png" width="640">

#Install
Clone phoxi_camera package to your catkin_ws and build as usual
```
cd catkin_ws/src
git clone https://github.com/photoneo/phoxi_camera.git
cd ..
catkin_make
```
#Test PhoXi ROS interface without real 3D scanner
It is possible to test PhoXi ROS interface without real hardware. 
- Start PhoXiControl application 
- Launch ```roslaunch phoxi_camera phoxi_camera_test.launch```
- Now, application should connect to the camera and start to aquire example pointclouds
- Notice that pointcloud data are also being published on ROS topics
- Notice available ROS services that enables direct camera control

#Test PhoXi ROS interface with real device
- Start PhoXiControl application 
- Connect to your device
- Run Interface node ```rosrun phoxi_camera phoxi_camera ```
- Use available ROS services to control your 3D scanner




