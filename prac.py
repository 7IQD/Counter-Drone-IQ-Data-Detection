import numpy as np

# Step 1: Input signal
x = np.array([0, 1, 0, -1])
N = len(x)

# Step 2: Compute FFT
X = np.fft.fft(x)

# Step 3: Compute frequencies
fs = 4  # sampling frequency (for mapping frequency bins)
freqs = np.fft.fftfreq(N, 1/fs)

# Step 4: Print results
print("Input x[n]:", x)
print("DFT X[k]:", X)
print("Frequencies (Hz):", freqs)
print("Magnitude |X[k]|:", np.abs(X))
print("Phase ∠X[k]:", np.angle(X, deg=True))