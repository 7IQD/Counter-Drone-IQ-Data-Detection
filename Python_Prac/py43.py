import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 1000       # Sampling rate (Hz)
T = 1 / Fs      # Sample spacing
N = 1000        # Number of samples
f_signal = 50   # Hz

t = np.arange(N) * T
x = np.sin(2 * np.pi * f_signal * t)

# FFT
X = np.fft.fft(x)
freqs = np.fft.fftfreq(N, T)

# Magnitude & Phase
mag = np.abs(X) / N
phase = np.angle(X)

# Plot
plt.figure(figsize=(10, 5))
plt.stem(freqs, mag, basefmt=" ")
plt.title("FFT Magnitude")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

# Insights
for i, f in enumerate(freqs[:N//2]):  # Only positive freqs
    if mag[i] > 0.05:  # Ignore tiny
        print(f"Bin {i}: {f} Hz → Magnitude {mag[i]:.3f}, Phase {phase[i]:.2f} rad")