import numpy as np
import matplotlib.pyplot as plt

# Time settings
N = 8
t = np.arange(N)
print(t)
# Test signal: pure tone
x = np.array([0, 0.71, 1, 0.71, 0, -0.71, -1, -0.71])

# FFT
X = np.fft.fft(x)
print("FFT result:", np.round(X, 2))
mag = np.round(np.abs(X), 2)
angle = np.round(np.rad2deg(np.round(np.angle(X), 2)),2)
print("Magnitude of each Sample", mag)
print("Angle of each Sample", angle)
