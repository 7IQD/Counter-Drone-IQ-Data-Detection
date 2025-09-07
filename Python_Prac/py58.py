import numpy as np
from scipy.signal import lfilter, decimate
from scipy.io.wavfile import write

# File paths
file_in = r"C:\Users\Ani\capture_104_filtered.bin"  # filtered or raw
file_out = r"C:\Users\Ani\capture_filtered.wav"

# Parameters
fs_iq = 104e6  # IQ sampling rate
fs_audio = 48000  # output WAV sampling rate
dtype = np.float32

# Read binary
raw_data = np.fromfile(file_in, dtype=dtype)
I = raw_data[::2]
Q = raw_data[1::2]
IQ = I + 1j*Q

# Optional: filtering
# IQ_filtered = IQ  # no filter
# OR use your bandpass filter
# IQ_filtered = your_bandpass_filter(IQ, ...)

# Convert to real for WAV
audio = np.real(IQ)  # or IQ_filtered

# Downsample safely
factor = int(fs_iq / fs_audio)
audio_down = decimate(audio, factor)

# Normalize and save
audio_down = audio_down / np.max(np.abs(audio_down))
audio_int16 = np.int16(audio_down * 32767)
write(file_out, fs_audio, audio_int16)
