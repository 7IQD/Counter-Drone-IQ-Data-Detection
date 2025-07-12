import numpy as np
import matplotlib.pyplot as plt
frequencies = np.array([5, 10, 20, 40])
t = np.linspace(0, 1, 1000)

t = t[None, :]
f = frequencies[:, None]

signals = np.sin(2 * np.pi * f * t)

print(signals.shape[0])

for i in range(signals.shape[0]):
    plt.plot(t.flatten(), signals[i], label=f"{frequencies[i]} Hz")

plt.title("Multi-Tone Signal Generation using Broadcasting")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()