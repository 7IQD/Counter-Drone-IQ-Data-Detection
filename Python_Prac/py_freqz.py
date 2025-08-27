import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Example: 5-point moving average filter (FIR)
b = np.ones(11) / 11.0   # numerator (FIR taps)
a = [1.0]              # denominator (FIR only)

fs = 1000.0  # sampling frequency (Hz)

# Frequency response
w, h = freqz(b, a, worN=512, fs=fs)  # w = frequency axis, h = complex response

# Plot magnitude (in dB)
plt.subplot(2, 1, 1)
plt.plot(w, 20*np.log10(np.abs(h)))
plt.title("Magnitude response of 5-point moving average")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)

# Plot phase
plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(h)))
plt.title("Phase response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.show()
