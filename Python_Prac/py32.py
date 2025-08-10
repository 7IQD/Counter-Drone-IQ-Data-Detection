import numpy as np
import matplotlib.pyplot as plt

# Time base
fs =  1000
f = 50
t = np.arange(0, 1, 1/fs)
theta = 2 * np.pi * f * t
signal = np.cos(2*np.pi*f*t)

fft_values = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(len(t), 1/fs)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Unit Circle (Phasor Path)")
plt.xlabel("cos(θ) - I")
plt.ylabel("sin(θ) - Q")
plt.axis('equal')

plt.subplot(1, 2, 2)
plt.plot(t, x, label='cos(θ) = I')
plt.plot(t, y, label='sin(θ) = Q')
plt.title("I and Q Waveforms")
plt.xlabel("Time")
plt.legend()
plt.tight_layout()
plt.show()
