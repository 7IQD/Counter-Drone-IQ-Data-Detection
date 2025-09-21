import numpy as np
#Design Configuration
num_symbols = 8 #→ short enough to plot clearly, long enough to see pattern.
sps = 8 # → 8 samples per symbol (a common “lab” value).
span = 6 # → filter spans 6 symbols (3 on each side).
beta = 0.35 #→ roll-off factor (a gentle slope, not too sharp).
N = sps*span + 1 # Filter Length
print("Filter Length", N)
filter_delay = (N-1)//2
print("Filter Delay", filter_delay)

#generate symbols
bits = np.random.randint(0, 2, size=num_symbols)
symbols = 2*bits - 1  # map 0->-1, 1->+1
print("Bits:    ", bits)
print("Symbols: ", symbols)

upsampled = np.zeros(num_symbols*sps)  # upsampled sequence
print ("Length of upsampled sequence:", len(upsampled))
upsampled[::sps] = symbols
print(upsampled)

def rc_taps(beta, sps, span):
    t = np.arange(-span*sps, span*sps+1) / sps
    h = np.sinc(t) * np.cos(np.pi*beta*t) / (1 - (2*beta*t)**2 + 1e-8)
    h[t==0] = 1.0  # avoid singularity at 0
    return h / np.sum(h)
h = rc_taps(beta=beta, sps=sps, span=span)
print("Coefficients Identified for the Filter", h[:10])
tx = np.convolve(upsampled, h, mode='full')
print("Filtered Pulse Waveform", tx[:10])

decision_indices = filter_delay + np.arange(len(symbols))*sps

# RX side: apply matched filter (no noise yet)
rx = np.convolve(tx, h, mode='full')
# --- Decision indices ---
decision_indices = filter_delay*2 + np.arange(len(symbols))*sps

# --- Sample at decision points ---
rx_samples = rx[decision_indices]
detected_symbols = np.sign(rx_samples)

print("Decision indices:", decision_indices)
print("Rx samples:      ", np.round(rx_samples, 3))
print("Detected symbols:", detected_symbols)
