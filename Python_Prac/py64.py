import numpy as np
import matplotlib.pyplot as plt

# Message bits
symbols = np.array([1+1j, -1+1j, 1-1j])

# BPSK mapping: 0 -> +1, 1 -> -1
# symbols = np.where(bits == 0, 1, -1)

# Symbol duration in samples
Ts = 3
waveform = np.repeat(symbols, Ts)  # repeat each symbol for visualization

# Plot
plt.figure(figsize=(10,3))
plt.plot(waveform, drawstyle='steps-post')
plt.title("BPSK: Bits → Symbols → Waveform")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
