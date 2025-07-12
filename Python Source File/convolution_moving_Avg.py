import numpy as np
import matplotlib.pyplot as plt

# Define input signal x[n]
x = np.array([1, 2, 3, 4], dtype=float)

# Define impulse response h[n] = moving average filter
h = np.array([1/3, 1/3, 1/3])

# Perform convolution
y = np.convolve(x, h, mode='valid')

# Define time axes
n_x = np.arange(len(x))
n_y = np.arange(len(y))

# Plot input and output
plt.stem(n_x, x, basefmt=" ", linefmt='b-', markerfmt='bo', label='Input x[n]')
plt.stem(n_y, y, basefmt=" ", linefmt='g-', markerfmt='go', label='Output y[n]')

plt.title("Convolution with Moving Average Filter")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
