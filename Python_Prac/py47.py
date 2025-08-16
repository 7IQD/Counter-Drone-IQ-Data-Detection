import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
Fs = 50        # samples per second
N = 20         # number of samples
t = np.linspace(0, 1, N, endpoint=False)

# Signal: simple sine wave
signal = np.sin(2*np.pi*5*t)

# Window: Hanning
window = np.hanning(N)
signal_windowed = signal * window

# Plot original vs windowed signal
plt.stem(t, signal, basefmt=" ", linefmt='r', markerfmt='ro', label='Original')
plt.stem(t, signal_windowed, basefmt=" ", linefmt='b', markerfmt='bo', label='Windowed')
plt.title("Signal: Original vs Windowed")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

# FFT comparison
X_original = np.fft.fft(signal)
X_windowed = np.fft.fft(signal_windowed)
freqs = np.fft.fftfreq(N, d=1/Fs)

plt.stem(freqs, np.abs(X_original), linefmt='r', markerfmt='ro', basefmt=" ", label='Original FFT')
plt.stem(freqs, np.abs(X_windowed), linefmt='b', markerfmt='bo', basefmt=" ", label='Windowed FFT')
plt.title("FFT Magnitude: Original vs Windowed")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.legend()
plt.show()
