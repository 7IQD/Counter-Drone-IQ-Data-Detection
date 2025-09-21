from scipy.signal import firwin, freqz
import matplotlib.pyplot as plt
import numpy as np

# Design a simple LPF
b = firwin(numtaps=51, cutoff=0.2)  # normalized freq (0-1)
w, h = freqz(b)  # frequency response

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(w/np.pi, np.abs(h))
plt.title("Magnitude Response")
plt.xlabel("Normalized Frequency")
plt.ylabel("Gain")

plt.subplot(1,2,2)
plt.plot(w/np.pi, np.angle(h))
plt.title("Phase Response")
plt.xlabel("Normalized Frequency")
plt.ylabel("Phase (radians)")
plt.show()
