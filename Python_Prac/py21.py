import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

# Sample signal: mix of low and high frequency
fs = 1000
t = np.arange(0, 1, 1/fs)
signal = np.sin(2 * np.pi * 30 * t) + 0.5*np.sin(2 * np.pi * 300 * t)

# Design High-pass FIR Filter
hp_kernel = firwin(numtaps=51, cutoff=100, fs=fs, pass_zero=False)
print(hp_kernel)

# Apply filter
filtered = lfilter(hp_kernel, 1.0, signal)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, signal, label="Original Signal, 30Hz+ 300 Hz", alpha=0.6)
plt.plot(t, filtered, label="High-pass Filtered Signal without 30 Hz", linewidth=2)
plt.legend()
plt.title("High-Pass FIR Filter (Blocks 30 Hz, Keeps 300 Hz)")
plt.grid(True)
plt.show()
