import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create bitstream and map to BPSK symbols
bits = np.array([1, 0, 1, 1, 0])
symbols = 2 * bits - 1             # BPSK: 1 → +1, 0 → −1
iq_samples = symbols + 0j          # Q = 0, I varies

# Step 2: Plot with proper alignment
plt.figure(figsize=(6, 6))
plt.scatter(iq_samples.real, iq_samples.imag, color='blue', s=100)

# Draw axes crossing at (0,0)
plt.axhline(0, color='black', linewidth=1)  # I-axis (horizontal)
plt.axvline(0, color='black', linewidth=1)  # Q-axis (vertical)

# Add annotations
for i, point in enumerate(iq_samples):
    label = f'bit {bits[i]} → {int(point.real)}'
    plt.text(point.real + 0.05, point.imag + 0.05, label, fontsize=9)

# Set axis limits centered around origin
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# Labels
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.title("Properly Aligned BPSK IQ Constellation")

# Make aspect ratio 1:1 so axes don't distort
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()