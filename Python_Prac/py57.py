import numpy as np
import matplotlib.pyplot as plt
f1,f2 = 5, 50 # in Hz
fs= 500 #500 samples/sec
N = 500
t = np.linspace(0, 1, fs, endpoint=True)
print(len(t))
x = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

#Process FFT for computation
X = np.fft.fft(x) 
freqs = np.fft.fftfreq(len(x), 1/fs)
half = len(freqs) // 2

# Shift both frequency and spectrum
shift_freqs = np.fft.fftshift(freqs)
X_shifted = np.fft.fftshift(X)

#Plot the Plots
plt.figure(figsize=(10,4))
plt.plot(t,x)
plt.title("Sine Plot")
plt.show()

#load Freq Spectrum
# Plot unshifted spectrum (default FFT order)
plt.figure(figsize=(10,4))
plt.stem(freqs[:half], np.abs(X)[:half])  # Only first half (positive freqs)
plt.title("Unshifted Frequency Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()

# Plot shifted spectrum (centered at 0 Hz)
plt.figure(figsize=(10,4))
plt.stem(shift_freqs, np.abs(X_shifted))
plt.title("Shifted Frequency Spectrum (fftshift)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()