import os
import numpy as np
from read_iq_file import read_iq_file
from analyse_fft import compute_spectrum
from plot_spectrum import plot_spectrum

# Step 0: Resolve path
script_dir = os.path.dirname(__file__)
files_dir = os.path.join(script_dir, "data")

# Get list of files in data folder
files = os.listdir(files_dir)

# Store IQ data in dictionary
iq_dict = {}

# Loop over each file and read IQ data
for f in files: 
    iq_data  = read_iq_file(f, dtype=np.int8, root_dir=files_dir)
    iq_dict[f] = iq_data # filename is the key 
    
# Example: print first few samples from first file
for filename, iq_data in iq_dict.items():
    print(f"{filename}:{iq_data[:10]}") # print only first 10 samples for readability
    print()
    # Now analyse the IQ Data in Frequency Domain
    print("Analysing files in Freq domain; One by One")
    
    # Analyse the data in Frequency Domain
    fs = 2.048e06  # Sampling Frequency 
    freq_axis_hz, power_spectrum = compute_spectrum(iq_data, fs, center_freq=0)
    
    # Now the plot the data
    plot_spectrum(freq_axis_hz, power_spectrum, title="Power-Spectrum Plot" + f"{filename}", xlabel="Frequency (Hz)", ylabel="Power (dB)", freq_in_mhz=False)
