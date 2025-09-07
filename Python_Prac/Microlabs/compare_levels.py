import soundfile as sf
import numpy as np

# Load raw and normalized files
raw_file = "C:/IQ_Files/Aud_Captured_104MHz_AF.wav"
norm_file = "C:/IQ_Files/Aud_Normalised_104MHz_AF.wav"

raw, sr = sf.read(raw_file)
norm, _ = sf.read(norm_file)

# Peak values (absolute max)
raw_peak = np.max(np.abs(raw))
norm_peak = np.max(np.abs(norm))

# Convert to dBFS (decibels relative to full scale)
raw_db = 20 * np.log10(raw_peak)
norm_db = 20 * np.log10(norm_peak)

print(f"Raw Peak: {raw_peak:.4f} → {raw_db:.2f} dBFS")
print(f"Norm Peak: {norm_peak:.4f} → {norm_db:.2f} dBFS")
