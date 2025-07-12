import numpy as np
import matplotlib.pyplot as plt

# Input signal
x = np.array([1, 2, 3, 4], dtype=float)

# Filter: First-order difference
h = np.array([1, -1])

# Convolution
y = np.convolve(x, h, mode='full')

# Time axes
n_x = np.arange(len(x))
n_y = np.arange(len(y))

# Plot
plt.stem(n_x, x, basefmt=" ", linefmt='b-', markerfmt='bo', label='Input x[n]')
plt.stem(n_y, y, basefmt=" ", linefmt='r-', markerfmt='ro', label='Output y[n] = x[n] * h[n]')
plt.title("Convolution with [1, -1] (Difference Filter)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

print("Output y[n] =", y)