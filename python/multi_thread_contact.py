import numpy as np
import serial
import threading
import cv2
import time
from scipy.ndimage import gaussian_filter
# import matplotlib.pyplot as plt
# import seaborn as sns
# os.system('cls')

contact_data_norm = np.zeros((16,16))
WINDOW_WIDTH = contact_data_norm.shape[1]*30
WINDOW_HEIGHT = contact_data_norm.shape[0]*30
cv2.namedWindow("Contact Data_left", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Contact Data_left",WINDOW_WIDTH, WINDOW_HEIGHT)
THRESHOLD =12
NOISE_SCALE =60

def readThread(serDev):
    global contact_data_norm,flag
    data_tac = []
    num = 0
    t1=0
    backup = None
    flag=False
    current = None
    while True:
        if serDev.in_waiting > 0:
            try:
                line = serDev.readline().decode('utf-8').strip()
            except:
                line = ""
            if len(line) < 10:
                if current is not None and len(current) == 16:
                    backup = np.array(current)
                    print("fps",1/(time.time()-t1))
                    t1 =time.time()
                    data_tac.append(backup)
                    num += 1
                    if num > 30:
                        break
                current = []
                continue
            if current is not None:
                str_values = line.split()
                int_values = [int(val) for val in str_values]
                matrix_row = int_values
                current.append(matrix_row) 

    data_tac = np.array(data_tac)
    median = np.median(data_tac, axis=0)
    flag=True
    print("Finish Initialization!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    while True:
        if serDev.in_waiting > 0:
            try:
                line = serDev.readline().decode('utf-8').strip()
                # print("fps",1/(time.time()-t1))
                # t1 =time.time()
            except:
                line = ""
            if len(line) < 10:
                if current is not None and len(current) == 16:
                    backup = np.array(current)
                    # print(backup)
                current = []
                if backup is not None:
                    contact_data= backup-median-THRESHOLD
                    contact_data = np.clip(contact_data, 0, 100)
                    
                    if np.max(contact_data) < THRESHOLD:
                        contact_data_norm = contact_data /NOISE_SCALE
                    else:
                        # contact_data_norm = np.log(contact_data + 1) / np.log(2.0)
                        contact_data_norm = contact_data / np.max(contact_data)

                continue
            if current is not None:
                str_values = line.split()
                int_values = [int(val) for val in str_values]
                matrix_row = int_values
                current.append(matrix_row) 
                    
                continue
        

# PORT = "left_gripper_right_finger"
PORT ='/dev/ttyUSB0'
BAUD = 2000000
# serDev = serial.Serial(PORT,2000000) 
serDev = serial.Serial('/dev/ttyUSB0',BAUD)
exitThread = False
serDev.flush()
serialThread = threading.Thread(target=readThread, args=(serDev,))
serialThread.daemon = True
serialThread.start()


def apply_gaussian_blur(contact_map, sigma=0.1):
    return gaussian_filter(contact_map, sigma=sigma)

def temporal_filter(new_frame, prev_frame, alpha=0.2):
    """
    Apply temporal smoothing filter.
    'alpha' determines the blending factor.
    A higher alpha gives more weight to the current frame, while a lower alpha gives more weight to the previous frame.
    """
    return alpha * new_frame + (1 - alpha) * prev_frame

# Initialize previous frame buffer
prev_frame = np.zeros_like(contact_data_norm)

if __name__ == '__main__':

    print('receive data test')

    while True:

        for i in range(300):
            if flag:
                temp_filtered_data = temporal_filter(contact_data_norm, prev_frame)
                prev_frame = temp_filtered_data

                # Scale to 0-255 and convert to uint8
                temp_filtered_data_scaled = (temp_filtered_data * 255).astype(np.uint8)

                # Apply color map
                colormap = cv2.applyColorMap(temp_filtered_data_scaled, cv2.COLORMAP_VIRIDIS)

                cv2.imshow("Contact Data_left", colormap)
                cv2.waitKey(1)
            time.sleep(0.01)

                        