# --- Bootcamp Mission: Stage 1 ---
from rtlsdr import RtlSdr
import numpy as np
import os
import matplotlib.pyplot as plt

freqs = [98.5e6, 104.0e6, 104.8e6]  # FM stations of interest
# Get the folder where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create a path relative to the script
save_dir = os.path.join(script_dir, "data")
os.makedirs(save_dir, exist_ok=True)

# --- 1. Configure SDR ---
sdr = RtlSdr()
sdr.sample_rate = 2.048e6  # 2.048 MS/s
sdr.gain = 'auto'
num_samples = 1024 * 256  # enough to see a clear spectrum
# Center Signal Freq at 98.5 MHz, 104 MHz and 104.8 MHz

for fc in freqs:
    sdr.center_freq = fc
    # --- 2. Capture Samples ---
    print(f"Capturing samples...{fc/1e06}Mhz")
    # Let's grab a big chunk to get a clear picture
    samples = sdr.read_samples(num_samples)
    # Save as complex64
    filename = os.path.join(save_dir, f"iq_{fc/1e06}.bin" )
    samples.astype(np.complex64).tofile(filename)
    print(f"saved{filename}")

sdr.close()
print("Capture complete.")

