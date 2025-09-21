import numpy as np
from scipy.signal import convolve

# ------------------------------
# Step 1: Define symbols
# ------------------------------
symbols = np.array([
    1, -1, 1, 1, -1, -1, 1, -1,
    1, 1, -1, 1, -1, 1, -1, 1,
    -1, 1, 1, -1, 1, -1, 1, 1,
    -1, 1, -1, 1, 1, -1, -1, 1
], dtype=float)

N_symbols = len(symbols)

# ------------------------------
# Step 2: Upsample
# ------------------------------
sps = 8  # samples per symbol
upsampled = np.zeros(N_symbols * sps)
upsampled[::sps] = symbols  # place symbol at first sample of each block

# ------------------------------
# Step 3: Tx RC filter
# ------------------------------
def rrc_filter(beta, N, sps):
    n = np.arange(-(N//2), N//2 + 1)
    h = np.zeros_like(n, dtype=float)
    eps = 1e-8  # tolerance for float comparison
    for i, ni in enumerate(n):
        denom = 1 - (2*beta*ni/sps)**2
        if abs(ni) < eps:
            h[i] = 1 - beta + (4*beta/np.pi)
        elif abs(denom) < eps:
            h[i] = (beta/np.sqrt(2)) * (
                ((1 + 2/np.pi) * np.sin(np.pi/(4*beta))) +
                ((1 - 2/np.pi) * np.cos(np.pi/(4*beta)))
            )
        else:
            h[i] = np.sinc(ni / sps) * np.cos(np.pi * beta * ni / sps) / denom
    return h
beta = 0.25
N_taps = 33
h_tx = rrc_filter(beta, N_taps, sps)

# Convolve with Tx filter
y_tx = convolve(upsampled, h_tx, mode='full')

# Normalize
y_tx /= np.max(np.abs(y_tx))

# ------------------------------
# Step 4: Channel (ideal for now)
# ------------------------------
y_chan = y_tx.copy()  # no noise for now

# ------------------------------
# Step 5: Rx matched filter
# ------------------------------
y_rx = convolve(y_chan, h_tx, mode='full')  # matched RC filter
total_delay = (N_taps - 1) + (N_taps - 1)//2  # Tx + Rx delay approximation

d_i = [] #decision indices
d_i = total_delay +  np.arange(len(symbols))*sps
print("These are the decision indices", d_i)
print("Total No. of deciison points are:", len(d_i))
recovered_symbols = np.sign(y_rx[d_i])
print("List of recovered Symbols", recovered_symbols)

# Calculating BER
errors = recovered_symbols != symbols
c_error = np.sum(errors)
print("Count of errors", c_error)
if (c_error != 0):
    print("Bit Error Rate:", c_error/len(symbols))
else:
    print("No BER")