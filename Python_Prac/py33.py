import numpy as np
import matplotlib.pyplot as plt

# Generate a test signal with a 50 Hz peak
fs = 1000  # Sampling rate
t = np.arange(0, 1.0, 1.0/fs)
signal = np.sin(2 * np.pi * 50 * t)  # 50 Hz sine wave

# FFT
fft_result = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(len(signal), d=1/fs)
magnitude = np.abs(fft_result)

# Only keep positive frequencies
positive_freqs = fft_freqs[:len(fft_freqs)//2]
positive_magnitude = magnitude[:len(magnitude)//2]

# Find peak frequency
peak_freq = positive_freqs[np.argmax(positive_magnitude)]
print("Peak frequency:", peak_freq)

# Plot
plt.plot(positive_freqs, positive_magnitude)
plt.title("FFT Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
