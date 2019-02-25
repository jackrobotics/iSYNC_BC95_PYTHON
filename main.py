import serial
from time import sleep, time
from nb_iot import *

bc95 = iSYNC_NB('COM55')
bc95.setupDevice()

previous_time = time()
interval = 5
cnt = 0
while True:
    current_time = time()
    if current_time - previous_time >= interval:
        cnt += 1
        msg = "iSYNC Python test "+str(cnt)
        bc95.iSYNC_POST("5c6aa6a9f0a80317c5d064e1",msg)
        # bc95.iSYNC_GET("5c6aa6a9f0a80317c5d064e1")
        previous_time = current_time
        
    bc95.response()