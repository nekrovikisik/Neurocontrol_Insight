# -*- coding: utf8 -*-
#
#  CyKIT  2020.06.05
#  ________________________
#  example_epoc_plus.py       
#  
#  Written by Warren
#
"""
  usage:  python.exe .\example_insight.py

"""
import csv
import os
import sys

sys.path.insert(0, '..//py3//cyUSB//cyPyWinUSB')
sys.path.insert(0, '..//py3')

import cyPyWinUSB as hid
import queue
from cyCrypto.Cipher import AES
from cyCrypto import Random

tasks = queue.Queue()


from datetime import datetime
import csv
filename = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S").replace('/', '_').replace(':', '_').replace(' ', '_')+ '.txt'
f = open(filename , 'w+')
index = 'Gyro-X;Gyro-Z;AF3;Gyro-Y;T7;Acc-X;Pz;QualityData_1;QualityData_2;Acc-Z;Acc-Y;T8;Mag-X;AF4;Mag-Z;Mag-Y;Mag-X;Gyro-X '
f.write(index + '\n')
cyHeadset = EEG_insight()
arr = []
import time
timing = time.time()
print(timing)
while 1:
#import matplotlib
    while tasks.empty():
        pass
    arr.append([float(i) for i in cyHeadset.get_data().split(', ')])
    f.write(cyHeadset.get_data().replace(', ', ';') + '\n')

    if time.time() - timing > 30.0:
        print(time.time())
        break
import numpy as np
import mne
# Read the CSV file as a NumPy array
data = np.array(arr).T

# Some information about the channels
ch_names = [f'CH_{i}' for i in range(1, 17)]  # TODO: finish this list

# Sampling rate of the Nautilus machine
sfreq = 128  # Hz

# Create the info structure needed by MNE
info = mne.create_info(ch_names, sfreq)

# Finally, create the Raw object
raw = mne.io.RawArray(data, info)

# Plot it!
raw.plot()
print(raw.info())
eog_events = mne.preprocessing.find_eog_events(raw, ch_name= 'Fp2')
