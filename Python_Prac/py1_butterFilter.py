import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

sample_rate  = 1e6 #1,000,000 samples per sec
cut_off_hz = 50e3 # We want to cut off everything above 50KHz

#Designing a Butterworth Bouncer....
# 1. Set the steepness (the order)
order = 4

# 2. Normalize the cutoff frequency (the crucial step!)
nyquist = sample_rate/2
normal_cutoff = cut_off_hz/nyquist

# 3. Design the filter!
b, a  = signal.butter(order, normal_cutoff, btype='low', analog=False)

print("This is 'b':", b)

print("This is 'a':", a)

'''
Ouput:
This is 'b': [0.0004166 0.0016664 0.0024996 0.0016664 0.0004166]
This is 'a': [ 1.         -3.18063855  3.86119435 -2.11215536  0.43826514]
'''
