# --- Bootcamp Mission: Stage 1 ---
from rtlsdr import RtlSdr
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Configure SDR ---
sdr = RtlSdr()
sdr.sample_rate = 2.048e6  # 2.048 MS/s
sdr.center_freq = 98.5e6   # 98.5 MHz, 104 MHz and 104.8 MHz
sdr.gain = 'auto'

# --- 2. Capture Samples ---
print("Capturing samples...")
# Let's grab a big chunk to get a clear picture
num_samples = 1024 * 512
samples = sdr.read_samples(num_samples)
sdr.close()
print("Capture complete.")

# --- 3. YOUR CODE GOES HERE ---
# Task: Create and display an FFT plot of the 'samples' data.
# Use the sample_rate to correctly scale the frequency axis.
# Pro-tip: Use np.fft.fftshift() to center the plot at 0 Hz.






# --- End of Your Code ---