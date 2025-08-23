import os
import sys

# Root directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Add src to sys.path so Python can find model package
# Add src to Python path
sys.path.insert(0, os.path.join(ROOT_DIR, "src"))

# Optional: check Python sees src/model
print("sys.path:", sys.path)
print("ROOT_DIR:", ROOT_DIR)
import numpy as np
from model.read_iq_file import read_iq_file
from model.compute_spectrum import compute_spectrum



center_freq = 104.8e6  # Signal freq 104.8 MHz
fs = 2.4e06            # Sampling Freq = 2.4 Mbps
filename = r"C:\Users\Ani\Desktop\Ajay Bharatiya\Counter-Drone-IQ-Data-Detection\data\raw\Prac_FM_104_8MHz_20250820.bin"
iq = read_iq_file(filename)
N =  len(iq)           # No of samples 

def compute_spectrum(iq, fs):

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

    # ... after you compute spec_centering and power_spectrum ...
    rf_axis_hz = spec_centering + center_freq  # shift baseband bins to RF
    rf_axis_mhz = rf_axis_hz / 1e6
    return freqbin, power_spectrum

compute_spectrum(iq, fs)