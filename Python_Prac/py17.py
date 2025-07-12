import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)  # Time vector: 1 sec at 1kHz
print(f"{t.shape}")
signal = np.sin(2 * np.pi * 10 * t)  # 10 Hz sine wave
amplified = 2 * signal  # Scalar scaling
print(f"{amplified.shape}")
plt.plot(t, signal, label="Original")
plt.plot(t, amplified, label="Amplified")
plt.legend()
plt.xlabel("Time in sec")
plt.ylabel("Amplitude")
plt.title("Scalar Scaling of a Signal")
plt.grid(True)
plt.show()