
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

# Sampling setup
fs = 1000  # Hz
t = np.arange(0, 1, 1/fs)

# Create signal with three frequencies: 50 Hz, 150 Hz, 300 Hz
signal = (np.sin(2 * np.pi * 50 * t) + 
          np.sin(2 * np.pi * 150 * t) + 
          np.sin(2 * np.pi * 300 * t))

# Design band-pass filter kernel
numtaps = 51
cutoff= [100, 200]
bp_kernel = firwin(numtaps, cutoff, fs=fs, pass_zero=False)
# Apply filter
filtered_signal = lfilter(bp_kernel, 1.0, signal)
# Plot filtered signal
plt.plot(t, signal)
plt.plot(t, filtered_signal)
plt.title("Band-Pass Filtered Signal (100–200 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
