import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 48000  # Sample rate in Hz
f = 1000    # Signal frequency
duration = 0.01  # in seconds
t = np.arange(0, duration, 1/fs)

# Generate I/Q as complex sine wave
signal = np.exp(2j * np.pi * f * t)
I = np.real(signal)
Q = np.imag(signal)

# Plot
plt.plot(t, I, label='I')
plt.plot(t, Q, label='Q')
plt.title("Synthetic IQ Signal (1000 Hz)")
plt.legend()
plt.grid()
plt.show()

I8 = (I * 127).astype(np.int8)
Q8 = (Q * 127).astype(np.int8)

# Interleave [I0, Q0, I1, Q1, ...]
IQ_interleaved = np.empty((I8.size + Q8.size,), dtype=np.int8)
IQ_interleaved[0::2] = I8
IQ_interleaved[1::2] = Q8

# Save to binary file
with open("hello.iq8", "wb") as f:
    f.write(IQ_interleaved.tobytes())
