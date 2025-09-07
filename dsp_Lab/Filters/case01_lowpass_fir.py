# DSP Labs - Case 1
# FIR Low-pass Filter for Speech (fs=8kHz, cutoff=1kHz)

import numpy as np
from scipy.signal import firwin, lfilter, freqz
import matplotlib.pyplot as plt

fs = 8000        # Sampling frequency (Hz)
cutoff_hz = 1000    # Desired cutoff in Hz
numtaps = 51     # Filter length (number of taps)
# cutoff specified in Hz (since fs is given)
h_hz = firwin(numtaps, cutoff_hz, fs=fs)
print(h_hz[:10])  # show first 10 coefficients
cutoff_norm = cutoff_hz / (fs/2)  # = 1000 / 4000 = 0.25
h_norm = firwin(numtaps, cutoff_norm)  # no fs this time
print("First 5 coeffs (Hz method):", h_hz[:5])
print("First 5 coeffs (Norm method):", h_norm[:5])
