import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 1000)
x_sin = np.sin(2*np.pi*10*t)
plt.plot(t, x_sin, color='blue')
plt.title("Ajay's 5 Hz Sine-Cosine Wave")
plt.xlabel("Time in Sec")
plt.ylabel("Amplitude")
plt.grid(True)
x_cos = np.cos(2 * np.pi * 10 * t)
plt.plot(t, x_cos, color='black')
plt.show()

