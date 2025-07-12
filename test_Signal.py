import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 8000
t = np.arange(0, 1, 1/fs)
x = np.sin(2*np.pi*500*t) + 0.5*np.sin(2*np.pi*2000*t)

# Plot first 300 samples
plt.plot(t[:300], x[:300])
plt.title("Original Signal: 500 Hz + 2000 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

from scipy.signal import firwin, freqz

cutoff = 1000     # Hz
numtaps = 51      # Length of filter

h = firwin(numtaps, cutoff, fs=fs, window='hamming')

# Plot impulse response h[n]
plt.stem(h, basefmt=" ")
plt.title("Impulse Response h[n] - FIR Low-Pass Filter")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

w, H = freqz(h, worN=8000, fs=fs)

plt.plot(w, 20 * np.log10(np.abs(H)))
plt.title("Frequency Response of FIR Low-Pass Filter")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.show()
from scipy.signal import lfilter

y = lfilter(h, 1.0, x)

# Plot result
plt.plot(t[:300], x[:300], label='Original')
plt.plot(t[:300], y[:300], label='Filtered')
plt.title("Signal Before and After FIR Low-Pass Filtering")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

def plot_fft(signal, fs, title):
    N = len(signal)
    freq = np.fft.rfftfreq(N, 1/fs)
    X = np.abs(np.fft.rfft(signal))

    plt.plot(freq, X)
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show()

plot_fft(x, fs, "Original Signal Spectrum")
plot_fft(y, fs, "Filtered Signal Spectrum")