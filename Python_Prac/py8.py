import numpy as np
import matplotlib.pyplot as plt

# Simulated IQ data: row 0 = I, row 1 = Q
iq = np.array([
    [1, 2, 3, 4, 5],      # I samples
    [10, 20, 30, 40, 50]  # Q samples
])

# X-axis: sample positions (0, 1, 2, 3, 4)
x = np.arange(iq.shape[1])  # shape[1] = number of columns

# Plot I and Q
plt.plot(x, iq[0], label="I", marker='o')
plt.plot(x, iq[1], label="Q", marker='s')

# Plot styling
plt.title("I and Q Components")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()