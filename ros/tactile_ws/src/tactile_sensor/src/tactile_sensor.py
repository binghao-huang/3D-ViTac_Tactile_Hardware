# #!/usr/bin/env python

# import rospy
# from std_msgs.msg import Float64MultiArray
# import numpy as np
# import threading
# import time

# class TactileSensor:
#     def __init__(self, tactile_names):
#         self.tactile_name = tactile_names
#         rospy.init_node('tactile_listener', anonymous=True)
#         self.tactile_data = None  # Placeholder for the latest data received
#         # Initialize subscriber
#         for tactile_name in tactile_names:
#             self.subscriber = rospy.Subscriber(f'{tactile_name}', Float64MultiArray, self.callback)
    
#     def callback(self, data):
#         # Callback function that will be called when new data is published on the topic
#         self.tactile_data = np.array(data.data).reshape((16, 16))  # Assuming data is a 16x16 matrix
#         # You can add processing code here
#         # print(f"Received data on {self.tactile_name}: {self.tactile_data}")
    
#     def get_latest_data(self):
#         # Method to fetch the latest data received; returns None if no data has been received yet.
#         return self.tactile_data


# if __name__ == '__main__':
#     tactile_names = ['right_robot_left_finger', 'right_robot_right_finger']
#     tactile = TactileSensor(['right_robot_right_finger'])
#     while not rospy.is_shutdown():
#         print('right',tactile.tactile_right)
#         time.sleep(0.1)
#         # rospy.spin()

import rospy
import numpy as np
from std_msgs.msg import Float64MultiArray
import time

class TactileSensor:
    def __init__(self, tactile_names):
        self.tactile_names = tactile_names
        rospy.init_node('tactile_listener', anonymous=True)
        self.tactile_data = {}  # Use a dictionary to store data from each sensor
        # Initialize subscribers for each tactile sensor
        for tactile_name in tactile_names:
            self.tactile_data[tactile_name] = None  # Initialize with None
            rospy.Subscriber(tactile_name, Float64MultiArray, self.callback, callback_args=tactile_name)

    def callback(self, data, tactile_name):
        # Callback function that will be called when new data is published on the topic
        # Here we use callback_args to distinguish between sensors
        self.tactile_data[tactile_name] = np.array(data.data).reshape((16, 16))  # Assuming data is a 16x16 matrix

    # def get_latest_data(self, tactile_name):
    #     # Method to fetch the latest data received for a specific sensor
    #     return self.tactile_data.get(tactile_name, None)


if __name__ == '__main__':
    tactile_names = ['right_robot_left_finger']
    tactile_sensor = TactileSensor(tactile_names)
    while not rospy.is_shutdown():
        # Print the latest data for each sensor
        t1 = time.time()
        print('right_robot_left_finger:', tactile_sensor.tactile_data['right_robot_left_finger'])
        # print('right_robot_right_finger:', tactile_sensor.get_latest_data('right_robot_right_finger'))
        print(1/(time.time()-t1))
        # for name in tactile_names:
        #     print(f'{name}: {tactile_sensor.get_latest_data(name)}')
        # time.sleep(0.1)  # Sleep to limit the rate of the output
