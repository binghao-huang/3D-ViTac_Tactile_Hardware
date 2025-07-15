
# 3D ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing

#### Project Website: https://binghao-huang.github.io/3D-ViTac/

This codebase contains python code and ros package for flexible tactile sensor in 3D-ViTac. To build the tactile sensors, follow the instructions below:
[[Hardware Assembly Tutorial]](https://docs.google.com/document/d/1XGyn-iV_wzRmcMIsyS3kwcrjxbnvblZAyigwbzDsX-E/edit?tab=t.0#heading=h.ny8zu0pq9mxy)
,[[Bills of Material]](https://docs.google.com/document/d/1auxwAbAnt88nG7HDqanr4JJreuAVkrhs1nK16VQaLpk/edit?tab=t.0#heading=h.ny8zu0pq9mxy)

## 1. Firmware

(1) Load the [arduino code](/arduino_code/MatrixArray.ino) to the arduino. 

## 2. PYTHON(option 1)
(1) Setup environment

        pip install pyserial
        pip install opencv-python==4.6.0.66
        pip install threading
        pip install scipy

(2)Start python visualization

        cd python
        python3 multi_thread_contact.py

## 3. ROS(option 2)
1. compile ros package(Assuming you have already installed ROS1)

        cd ros/tactile_ws
        catkin_make

3. rosrun tactile_sensor tactile_sensor.py

## 4. Multi Sensors name setup (optional)

1. setup multi thread tactile board name(Optional):
- One issue that arises is the port each robot binds to can change over time, e.g. a robot that
is initially ``ttyUSB0`` might suddenly become ``ttyUSB5``. 

- Take ``right_robot_left_finger``: right master robot as an example:
  1. Find the port that the right master robot is currently binding to, e.g. ``ttyUSB0``
  2. run ``udevadm info --name=/dev/ttyUSB0 --attribute-walk | grep serial`` to obtain the serial number. Use the first one that shows up, the format should look similar to ``FT6S4DSP``.
  3. ``sudo vim /etc/udev/rules.d/99-tactile.rules`` and add the following line: 

         SUBSYSTEM=="tty", ATTRS{serial}=="<serial number here>", ENV{ID_MM_DEVICE_IGNORE}="1", ATTR{device/latency_timer}="1", SYMLINK+="right_robot_left_finger"

  4. This will make sure the tactile in right_robot_left_finger is *always* binding to ``right_robot_left_finger``
  5. Repeat with the rest of 3 arms.
- To apply the changes, run ``sudo udevadm control --reload && sudo udevadm trigger``
- If successful, you should be able to find ``right_robot_left_finger`` in your ``/dev``


## 🏷️ License
FlexiTac © 2025 by Columbia University is licensed under CC BY-NC 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc/4.0/
