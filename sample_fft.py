import numpy as np
import matplotlib.pyplot as plt
fs= 1 # Sample rate = 1 Hz
t = np.arange(100)
s = np.sin(0.15*2*np.pi*t)
S = np.fft.fft(s)
plt.plot(t,s)
plt.xlabel("Sample Index")
plt.ylabel("Signal Amplitude")
S_mag = np.abs(S)
S_phase = np.angle(S)
plt.plot(t,S_mag,'.-')
plt.plot(t,S_phase,'.-')
plt.show()

