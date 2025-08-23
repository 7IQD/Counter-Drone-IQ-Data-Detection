import numpy as np
import matplotlib.pyplot as plt
import os
center_freq = 104.8e6  # Signal freq 104.8 MHz
fs = 2.4e06            # Sampling Freq = 2.4 Mbps

filename = r"C:\Users\Ani\Desktop\Ajay Bharatiya\Counter-Drone-IQ-Data-Detection\data\raw\Prac_FM_104_8MHz_20250820.bin"
raw = np.fromfile(filename, dtype=np.int8)
print("Here is the raw data:", raw)

# Split into I and Q
I = raw[0::2].astype(np.float32) - 127.5
Q = raw[1::2].astype(np.float32) - 127.5

# Normalize
I /= 127.5
Q /= 127.5
print("Normalized I:", I)
print("Normalized Q:", Q)

# Form complex signal
iq = I + 1j*Q
N =  len(iq)  # No of samples 

#Bin Spectrum Centering through FFT Shift
freqbin = np.fft.fft(iq)
freqbin_centering = np.fft.fftshift(freqbin)

# Correct magnitude of iq data
mag = np.abs(freqbin_centering)

# Optional: phase (in radians)
angle = np.angle(freqbin_centering)

power_spectrum = 20 * np.log10(np.abs(freqbin_centering))

#Now Freq Spectrum Centering thorugh FFTfreq Shift
spectrum = np.fft.fftfreq(N, 1/fs)
spec_centering = np.fft.fftshift(spectrum)

center_freq = 104.8e6  # Hz

# ... after you compute spec_centering and power_spectrum ...
rf_axis_hz = spec_centering + center_freq  # shift baseband bins to RF
rf_axis_mhz = rf_axis_hz / 1e6


# Plot
plt.figure(figsize=(10,4))
plt.title("Power-Spectrum Plot")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power(dB)")

# Use spec_centering (frequency axis) and power_spectrum (y axis)
plt.plot(rf_axis_mhz, power_spectrum)
plt.grid(True)
plt.show()