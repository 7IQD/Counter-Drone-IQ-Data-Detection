import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter

kernel = firwin(31, cutoff=100, fs=1000)
plt.stem(kernel)
plt.title("FIR Filter Kernel")
plt.grid(True)
plt.show()