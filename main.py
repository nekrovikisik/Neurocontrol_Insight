from CyKit.Examples.example_insight import EEG_insight

import csv
import os
import sys
import numpy as np
import mne
import queue
from datetime import datetime
import time

tasks = queue.Queue()

def writeData():
    index = 'Gyro-X;Gyro-Z;AF3;Gyro-Y;T7;Acc-X;Pz;QualityData_1;QualityData_2;Acc-Z;Acc-Y;T8;Mag-X;AF4;Mag-Z;Mag-Y;Mag-X;Gyro-X '
    filename = datetime.utcnow().strftime("%d_%m_%Y_%H_%M_%S")
    f = open(f'{filename}.txt', 'w+')
    f.write(index + '\n')
    cyHeadset = EEG_insight(); timing = time.time()
    arr = []
    print(timing)
    while time.time() - timing <= 30.0:
        print(time.time())
        arr.append([float(i) for i in cyHeadset.get_data().split(', ')])
        f.write(cyHeadset.get_data().replace(', ', ';') + '\n')
    return arr

arr = writeData
data = np.array(arr).T
