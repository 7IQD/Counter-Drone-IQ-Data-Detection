import os
import sys
import numpy as np

# Root directory of the project (where main.py lives)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Add src to Python path
sys.path.insert(0, os.path.join(ROOT_DIR, "src"))

from model.read_iq_file import read_iq_file
from model.compute_spectrum import compute_spectrum
from model.plot_spectrum import plot_spectrum

def main():
    # --------------------------
    # Step 1: Load IQ data
    # --------------------------
    filename = os.path.join(ROOT_DIR, "data", "raw", "Prac_FM_104_8MHz_20250820.bin")

    # Optional: automatic dtype detection or predefined
    dtype = np.int8  # can extend later for int16/uint8
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    iq = read_iq_file(filename)
    print(f"Number of IQ samples: {len(iq)}")
    # --------------------------
    # Step 2: Compute spectrum
    # --------------------------
    fs = 2.4e6            # Sampling frequency
    center_freq = 104.8e6 # Center frequency
    freq_axis_hz, power_spectrum = compute_spectrum(iq, fs, center_freq)

    print(f"Spectrum computed: {len(freq_axis_hz)} frequency bins")

    # --------------------------
    # Step 3: Plot spectrum
    # --------------------------
    plot_spectrum(freq_axis_hz, power_spectrum, 
                title="FM 104.8 MHz Spectrum", 
                freq_in_mhz=True)
if __name__ == "__main__":
    main()