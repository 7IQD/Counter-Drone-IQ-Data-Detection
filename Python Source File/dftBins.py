import numpy as np

x = np.array([1, 0, -1, 0])
X = np.fft.fft(x)
print(X)
for k in range(len(x)):
    print(f"X{k}={X[k]}")
