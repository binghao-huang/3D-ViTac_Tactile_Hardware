# PYTHON
cd python
python3 multi_thread_contact.py

# ROS

1. setup multi thread tactile board name:
- One issue that arises is the port each robot binds to can change over time, e.g. a robot that
is initially ``ttyUSB0`` might suddenly become ``ttyUSB5``. 

- Take ``right_robot_left_finger``: right master robot as an example:
  1. Find the port that the right master robot is currently binding to, e.g. ``ttyUSB0``
  2. run ``udevadm info --name=/dev/ttyUSB0 --attribute-walk | grep serial`` to obtain the serial number. Use the first one that shows up, the format should look similar to ``FT6S4DSP``.
  3. ``sudo vim /etc/udev/rules.d/99-fixed-interbotix-udev.rules`` and add the following line: 

         SUBSYSTEM=="tty", ATTRS{serial}=="<serial number here>", ENV{ID_MM_DEVICE_IGNORE}="1", ATTR{device/latency_timer}="1", SYMLINK+="right_robot_left_finger"

  4. This will make sure the right master robot is *always* binding to ``ttyDXL_master_right``
  5. Repeat with the rest of 3 arms.
- To apply the changes, run ``sudo udevadm control --reload && sudo udevadm trigger``
- If successful, you should be able to find ``right_robot_left_finger`` in your ``/dev``

2. compile ros package
   cd ros/tactile_ws
   catkin_make

3. rosrun tactile_sensor tactile_node_left