import numpy as np

# Step 1: Define parameters
fs = 1000          # Sampling rate in Hz
f_base = 50        # Baseband signal frequency in Hz
duration = 1       # seconds

t = np.arange(0, duration, 1/fs)  # Time vector
# print(t, t.dtype)
print("Data type of t:", t.dtype)
print("Each element size (bytes):", t.itemsize)
print("Total bytes used by t:", t.nbytes)
# print("Sampling rate (fs):", fs)
# print("Signal frequency (f_base):", f_base)
# print("Duration (s):", duration)
print("Time vector (first 10 values):", t[:10])
# print("Total samples:", len(t))