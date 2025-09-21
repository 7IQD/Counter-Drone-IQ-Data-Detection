import numpy as np
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt 

def rrc_taps(beta, sps, span):
    N = span * sps + 1
    t = (np.arange(N) - (N-1)/2) / sps
    h = np.zeros_like(t, dtype=float)
    for i, tt in enumerate(t):
        if abs(tt) < 1e-8:
            h[i] = 1.0 - beta + (4*beta/np.pi)
        elif abs(abs(4*beta*tt) - 1.0) < 1e-8:
            h[i] = (beta/np.sqrt(2)) * (
                (1+2/np.pi)*np.sin(np.pi/(4*beta)) +
                (1-2/np.pi)*np.cos(np.pi/(4*beta))
            )
        else:
            h[i] = (np.sin(np.pi*tt*(1-beta)) +
                    4*beta*tt*np.cos(np.pi*tt*(1+beta))) / \
                   (np.pi*tt*(1-(4*beta*tt)**2))
    return t, h / np.sum(h)   # return both time axis and normalized taps
beta = 0.6
t, h = rrc_taps(beta=beta, span=12, sps=32)

plt.plot(t, h / np.max(np.abs(h)))
plt.xlabel("Time (symbols)")
plt.ylabel("Normalized amplitude")
plt.title(f"RRC pulse: beta={beta}, span=12, sps=32")
plt.grid(True)
plt.show()

