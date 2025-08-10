import numpy as np
import matplotlib.pyplot as plt

# 1. Set parameters
fs = 1000     # Sampling rate in Hz
f = 50        # Frequency of the signal in Hz
n = 32        # Number of samples (frame size)

# 2. Generate time vector
t = np.arange(0, n) / fs

# 3. Generate I and Q components
i = np.cos(2 * np.pi * f * t)        # In-phase
q = np.sin(2 * np.pi * f * t)        # Quadrature

# 4. Combine into complex IQ samples
iq = i + 1j * q                      # Complex baseband signal

# 5. Calculate peak magnitude
peak = np.max(np.abs(iq))

# 6. Compute scale factor to fit into int8 range (-128 to 127)
scale = 127 / peak if peak != 0 else 1

# 7. Apply scaling
iq_scaled = iq * scale              # Still complex float

# 8. Convert to int8
i_scaled = np.real(iq_scaled).astype(np.int8)
q_scaled = np.imag(iq_scaled).astype(np.int8)

# 9. Interleave I and Q
iq_interleaved = np.column_stack((i_scaled, q_scaled)).flatten()

# 10. Save to binary file
with open("iq_output.iq", "wb") as f:
    f.write(iq_interleaved.tobytes())

print("IQ data saved to 'iq_output.iq' (32 samples, int8 interleaved).")

# 11. Plot for visualization
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Original I/Q (float)")
plt.plot(i, label='I')
plt.plot(q, label='Q')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Scaled I/Q (int8)")
plt.stem(i_scaled, linefmt='C0-', markerfmt='C0o', basefmt=" ", label='I')
plt.stem(q_scaled, linefmt='C1-', markerfmt='C1o', basefmt=" ", label='Q')
plt.legend()

plt.tight_layout()
plt.show()
