import soundfile as sf
import numpy as np
import hashlib

# File paths
raw_file = "C:/IQ_Files/Aud_Captured_104MHz_AF.wav"
norm_file = "C:/IQ_Files/Aud_bp_filter_104MHz_AF.wav"

# --- 1. Hash the raw binary content ---
def file_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

raw_hash = file_hash(raw_file)
norm_hash = file_hash(norm_file)

print("=== File Hashes ===")
print(f"Raw  : {raw_hash}")
print(f"Norm : {norm_hash}")

# --- 2. Load and compare audio sample arrays ---
raw, sr = sf.read(raw_file)
norm, _ = sf.read(norm_file)

# Quick checks
same_length = len(raw) == len(norm)
diff_samples = np.sum(raw != norm)

print("\n=== Audio Array Comparison ===")
print(f"Same Length? {same_length}")
print(f"Number of Different Samples: {diff_samples}")
if diff_samples == 0:
    print("👉 The audio data is identical.")
else:
    print("👉 The audio data differs.")
