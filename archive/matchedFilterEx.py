import numpy as np
import matplotlib.pyplot as plt

# Known signal (template to detect)
s = np.array([1, 2, 1])

# Received signal (includes s embedded inside noise)
x = np.array([0, 0, 1, 2, 1, 0, 0])

# Matched filter: time-reversed version of s
h = s[::-1]  # reverse s

# Apply convolution
y = np.convolve(x, h, mode='full')

# Time axis
n_x = np.arange(len(x))
n_y = np.arange(len(y))

# Plot
plt.figure(figsize=(10, 4))
plt.stem(n_x, x, basefmt=" ", linefmt='b-', markerfmt='bo', label='Received signal x[n]')
plt.stem(n_y, y, basefmt=" ", linefmt='r-', markerfmt='ro', label='Matched filter output y[n]')
plt.title("Matched Filter Detecting Pattern [1, 2, 1] in Signal")
plt.xlabel("Sample index n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Print output
print("Matched Filter Output y[n]:", y)
