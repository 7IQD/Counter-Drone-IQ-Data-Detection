import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500) # 500 Samples
signal = np.sin(2 * np.pi * 5 * t) # 5 Hz Signal

np.random.seed(0)
noise = .5*np.random.randn(len(t))
noisy_signal= signal + noise

plt.plot(t, signal, label= 'Clean Signal')
plt.plot(t, noisy_signal, label= 'Signal with Gaussain Noise', alpha=.7)
plt.legend()
plt.grid()
plt.title("White Gaussian Noise")
plt.show()

