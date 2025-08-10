import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000            # Sample rate (Hz)
fc = 100             # Carrier frequency (Hz)
t = np.arange(0, 0.1, 1/fs)  # Time vector: 0 to 0.1s

# Real signal: cosine carrier with a little phase shift
x = np.cos(2 * np.pi * fc * t + np.pi/4)  # Shifted cosine = phase info

# Quadrature demodulation (downconversion)
I = x * np.cos(2 * np.pi * fc * t)        # Mix with cos
Q = x * -np.sin(2 * np.pi * fc * t)       # Mix with -sin (quadrature)

# Low-pass filter step skipped (optional in demo)

# Form complex IQ
IQ = I + 1j * Q

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, I, label="I (cos*signal)")
plt.plot(t, Q, label="Q (-sin*signal)")
plt.title("I and Q Components from Real Sampled Signal")
plt.xlabel("Time (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
