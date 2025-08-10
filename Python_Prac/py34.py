import numpy as np
import matplotlib.pyplot as plt

fs = 10000  # sampling rate
fc = 1000   # carrier frequency
t = np.arange(0, 0.01, 1/fs)

# Simulate modulation with a random message
message = np.random.choice([-1, 1], size=len(t))  # BPSK
carrier_i = message * np.cos(2 * np.pi * fc * t)
carrier_q = message * np.sin(2 * np.pi * fc * t)

# Add noise
noise_i = np.random.normal(0, 0.2, len(t))
noise_q = np.random.normal(0, 0.2, len(t))

I = carrier_i + noise_i
Q = carrier_q + noise_q

# Plot phasor
plt.figure(figsize=(6, 6))
plt.scatter(I, Q, s=2, alpha=0.5)
plt.title("Simulated Real-Time IQ Phasor Plot")
plt.xlabel("I")
plt.ylabel("Q")
plt.grid(True)
plt.axis("equal")
plt.show()
