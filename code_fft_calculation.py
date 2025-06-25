#Step 1: Code (Fast version using NumPy)

import numpy as np

x = np.array([1, 2, 3, 4])  # time-domain signal
X = np.fft.fft(x)

print("FFT result:")
print(np.round(X, 2))
#These are the 4 frequency bins: X[0], X[1], X[2], X[3].