import numpy as np
import matplotlib.pyplot as plt

# Original 3 IQ samples
iq_3 = np.array([1+1j, 0.81+0.81j, 0.31+0.31j])
h = np.array([0.2, 0.5, 0.3])
h_rev = h[::-1]  # Reverse taps for convolution

# Manual convolution (FIR filtering)
y = np.convolve(iq_3, h_rev)

# Align filtered output with original samples (centered)
x_orig = np.arange(len(iq_3))
x_filt = x_orig  # center y[1:4] over original samples
y_centered = y[1:-1]  # middle values for alignment

plt.figure(figsize=(6,4))
plt.plot(x_orig, np.abs(iq_3), 'o-', label='Original IQ')
plt.plot(x_filt, np.abs(y_centered), 's-', label='Filtered IQ (aligned)')
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.title("FIR Filter Effect - Vertical Alignment")
plt.grid(True)
plt.legend()
plt.show()
