# **_BLUESEA PACKAGE_**

---
### **Code Information**
**Integration:** _[Eng. Davidson Daniel Rojas Cediel](https://www.linkedin.com/in/dadaroce/)_ \
**Mail:** _davidson@kiwibot.com_ \
**Kiwi Campus / AI & Robotics Team**

**Based on: ROS2 [Bluesea2 Package](https://github.com/BlueSeaLidar/bluesea-ros2) by Lanhai** 

---

<p align="center">
    <img src="https://user-images.githubusercontent.com/39452483/108378469-04f2ef00-71d3-11eb-8a37-e848525e6f34.png">
</p>

<p align="center">
    bluesea
</p>

<video width="560" height="315" src="https://user-images.githubusercontent.com/39452483/129423561-7d5f272e-782d-4bcc-9811-37b1513c4dcd.mp4" frameborder="0" allowfullscreen></video>

---

```
File Tree
📦bluesea2
 ┣ 📂include
 ┃ ┣ 📜parser.h
 ┃ ┗ 📜reader.h
 ┣ 📂launch
 ┃ ┣ 📜LDS-50C-2.launch.py
 ┃ ┣ 📜LDS-50C-C30E.py
 ┃ ┗ 📜bluesea.launch.py
 ┣ 📂params
 ┃ ┣ 📜LDS-50C-2.yaml
 ┃ ┗ 📜LDS-50C-C30E.yaml
 ┣ 📂src
 ┃ ┣ 📜LHLiDAR.rules
 ┃ ┣ 📜bluesea_node.cpp
 ┃ ┣ 📜parser.cpp
 ┃ ┣ 📜tcp_reader.cpp
 ┃ ┣ 📜uart.c
 ┃ ┣ 📜uart_reader.cpp
 ┃ ┗ 📜udp_reader.cpp
 ┣ 📜.git
 ┣ 📜CMakeLists.txt
 ┣ 📜README.md
 ┗ 📜package.xml
```
---

# Bluesea2
ROS2 driver for Lanhai USB/Network 2D LiDAR 

How to build Lanhai ros driver
=====================================================================
    1) Clone this project to your workspace src folder
    2) Running `colcon build` to build 

How to run Lanhai ros node (Serial Port Version)
=====================================================================
1) Copy UDEV rule file : sudo cp src/LHLiDAR.rules /etc/udev/rules.d/
2) or Run : sudo chmod 666 /dev/ttyUSB0 # make usb serial port readable


## if your lidar model is LDS-50C-2 :
* ros2 launch bluesea2 LDS-50C-2.py 

## if your lidar model is LDS-50C-C30E :
* ros2 launch bluesea2 LDS-50C-C30E.py 
    

3) optional : ros2 topic hz /scan
4) optional : rviz2 # 




