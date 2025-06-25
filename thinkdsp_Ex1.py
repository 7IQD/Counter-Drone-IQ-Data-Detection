import numpy as np
import matplotlib.pyplot as plt

print("Ajay's first FFT")

# Step 1: Generate sine wave
fs = 1000        # Sampling rate in Hz
f = 10           # Sine wave frequency
duration = 1     # seconds
t = np.arange(0, duration, 1/fs)
x = np.sin(2 * np.pi * f * t)

# Step 2: Plot time-domain waveform
plt.figure(figsize=(10, 3))
plt.plot(t[:200], x[:200])
plt.title("Time Domain: 10 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

X = np.fft.fft(x)
N = len(X)
X_mag = np.abs(X) / N   # Normalize
freqs = np.fft.fftfreq(N, 1/fs)

# Step 4: Plot magnitude spectrum (only positive freqs)
plt.figure(figsize=(10, 3))
plt.stem(freqs[:N//2], X_mag[:N//2])
plt.title("Frequency Domain: FFT of Sine Wave")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()