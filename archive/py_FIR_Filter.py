import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

# Create a Sample Noisy Signal
fs = 500 # Sampling frequency in Hz (samples per second)
t = np.arange(0, 1, 1/fs) # Time array from 0 to 1 second
# A signal made of two sine waves: one slow (10 Hz) and one fast (100 Hz)
signal = np.sin(2*np.pi*10*t) + .5*np.sin(2*np.pi*100*t)

# Add Gaussian noise
np.random.seed(0)
noise = .3*np.random.randn(len(t))
noisy_signal = noise + signal

#Design a Low-Pass Filter (Only Keep the 10 Hz Part)
num_taps = 51  # Number of filter coefficients (kernel size)
cutoff = 20  # Pass frequencies below 20 Hz
kernel = firwin(num_taps, cutoff, fs=fs)

#Apply the Filter to the Noisy Signal
filtered = lfilter(kernel, 1.0, noisy_signal)

plt.plot(t, noisy_signal, label='Noisy')
plt.plot(t, filtered, label='Filtered', linewidth=2)
plt.legend()
plt.title("Low-Pass FIR Filtering")
plt.grid(True)
plt.show()
