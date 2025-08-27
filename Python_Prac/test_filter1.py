import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Parameters
fs = 1000        # Sampling frequency (Hz)
t = np.linspace(0, 1.0, fs, endpoint=False)   # 1 second time axis
x = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*100*t)   # 5 Hz + 100 Hz

# Butterworth filter
b, a = butter(N=4, Wn=0.1, btype='low')  # cutoff = 0.1 * (fs/2) = 50 Hz
y = lfilter(b, a, x)

# Plot
plt.figure(figsize=(10,4))
plt.plot(t, x, label="Original Signal (5Hz + 100Hz)")
plt.plot(t, y, label="Filtered Signal (Low-pass 50Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.title("Butterworth Low-pass Filter Example")
plt.show()
