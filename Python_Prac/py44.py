import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 1000       # Sampling rate (Hz)
T = 1 / Fs      # Sample spacing
N = 1000        # Number of samples
t = np.arange(N) * T
f1, f2 = 50, 120
x = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

X = np.fft.fft(x)
mag = np.abs(X) / N
freqs = np.fft.fftfreq(N, T)

plt.stem(freqs[:N//2], mag[:N//2])
plt.title("FFT of Two Tones")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()
