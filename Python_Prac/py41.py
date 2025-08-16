import numpy as np
import matplotlib.pyplot as plt
N = 8
DeltaT = 1/N          # time between samples
Fs = 1 / DeltaT
print ("Sampling Frequency in Hz", Fs)
t = np.arange(N)* DeltaT 
print("Time Intervals:", t)
# Simple sine wave: 1 Hz
f_signal = 1  # Hz
x = np.round(np.sin(2 * np.pi * f_signal * t), 2)
print("Digital samples x[n]:", x)
plt.plot(t, x)
plt.show()

