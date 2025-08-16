import numpy as np
import matplotlib.pyplot as plt

fs = 32 # Sampling Freq = 8 Hz
N = 8
t = np.arange(N)/fs
f_signal = 2 # Freq of Signal = 2 Hz
x = np.round(np.sin(2*np.pi*f_signal*t), 2) + np.round(np.sin(2*np.pi*4*t), 2) 
X = np.round(np.fft.fft(x), 2)
magnitude = np.abs(X)
phase = np.angle(X)
freqs = np.fft.fftfreq(N, d=1/fs)
print("Frequencies (Hz):", freqs)
print("Magnitude:", magnitude)
print("Phase (radians):", phase)

plt.stem(freqs, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()