import numpy as np
import matplotlib.pyplot as plt

filename = r"C:\IQ_Data\Prac_1.bin"
fs = 2400000 # Hz
raw = np.fromfile(filename, dtype=np.uint8)
print("Length of raw data",len(raw))

raw = raw.astype(np.float32)
 raw =(raw-127.5)/127.5
print("Raw:", raw)
raw0 = raw - raw.mean() 
print("Raw0",raw0)
print(f"Raw0 Mean:, {raw0.mean():.3f}")
print("Shape of raw", raw.shape)
if len(raw)%2 != 0:
    raw = raw[:-1]
IQ = raw.reshape(-1, 2)
print("Capture IQ Data:", IQ)
I = IQ[:,0]
print("Capture I Data:\n", IQ)
Q = IQ[:,1]
print("Capture Q Data:\n", IQ)

print("I.mean():", I.mean())
I0 = I - I.mean()
Q0 = Q - Q.mean()
print(f"Raw min/max after normalize: {raw.min():.3f}, {raw.max():.3f}")
print(f"Mean(I), Mean(Q) : {I.mean():.4f}, {Q.mean():.4f} (before DC removal)")
print(f"Mean(I0), Mean(Q0) : {I0.mean():.4f}, {Q0.mean():.4f} (after DC removal)")