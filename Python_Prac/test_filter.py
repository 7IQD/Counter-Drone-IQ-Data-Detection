import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter

fs = 1000 # Sampling Freq in Hz
t = np.linspace(0, 1, fs, endpoint=False)

#Build a signal - Mix of 3 frequencies
signal = np.sin(2*np.pi*5*t) # 5 Khz
+ np.sin(2*np.pi*50*t)       # 50 Khz 
+ np.sin(2*np.pi*200*t)      # 200 Khz

# Plot original signal
plt.figure(figsize=(10,4))
plt.plot(t, signal)
plt.title("Original Signal - (5 Hz- 50 Hz-200Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()