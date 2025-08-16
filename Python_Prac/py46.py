import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(8)
X = np.fft.fft(x)
X_shifted = np.fft.fftshift(X)

plt.subplot(1,2,1); 
plt.stem(np.abs(X)); 
plt.title("Normal FFT")

plt.subplot(1,2,2); 
plt.stem(np.abs(X_shifted)); 
plt.title("FFT Shifted")
plt.show()
