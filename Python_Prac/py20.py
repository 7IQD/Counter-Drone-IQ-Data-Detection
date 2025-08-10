import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

# Step 1: Simple test signal (step)
signal = np.array([1]*10 + [5]*10)
t = np.arange(len(signal))

# Step 2: FIR kernel
kernel = firwin(numtaps=3, cutoff=0.25)
print("Kernel:", kernel)

# Step 3: Apply filter
filtered = lfilter(kernel, 1.0, signal)

# Step 4: Plot
plt.plot(t, signal, '--o', label='Original')
plt.plot(t, filtered,'--o', label='Filtered', linewidth=2)
plt.title("FIR Filter Effect on Step Signal")
plt.grid(True)
plt.legend()
plt.show()
