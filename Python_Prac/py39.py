import numpy as np

fs = 8  # sample rate
f_m = 1  # mixing frequency (Hz)
n = np.arange(4)  # sample indices

# Input real signal
x = np.array([1, 0, -1, 0])

# Mixer (complex exponential)
m = np.exp(1j * 2 * np.pi * f_m * n / fs)

# Mixed signal
y = x * m

print("x:", x)
print("m (complex exponential):", np.round(m, 3))
print("y = x * m:", np.round(y, 3))
