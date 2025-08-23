import os
import numpy as np

# ------Config--------
file_path = r"C:\Users\Ani\Desktop\Ajay Bharatiya\Counter-Drone-IQ-Data-Detection\data\raw\Prac_FM_104_8MHz_20250820.bin"
dtype = np.uint8 # change if your capture was int16 or float32
if not os.path.exists(file_path):
    print("❌File does not exist:", file_path)
else:
    print("✅File exists:", file_path)

# === Step 2: Check file size ===
file_size = os.path.getsize(file_path)
print("File Size(bytes):", file_size)

# === Step 3: Load and print first samples ===
data = np.fromfile(file_path, dtype=dtype)
iq_data = data.reshape(-1,2)
print("First 10 IQ sample of captured data", iq_data[:10])

