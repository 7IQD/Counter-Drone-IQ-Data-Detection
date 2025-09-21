import numpy as np

num_symbols = 10
sps = 8  # samples per symbol

bits = np.random.randint(0, 2, size=num_symbols)
symbols = 2*bits - 1  # map 0->-1, 1->+1

print("Bits:    ", bits)
print("Symbols: ", symbols)

upsampled = np.zeros(len(symbols)*sps)
upsampled[::sps] = symbols
print("Upsampled (first 32):", upsampled[:32])

def rc_taps(beta, sps, span):
    t = np.arange(-span*sps, span*sps+1) / sps
    h = np.sinc(t) * np.cos(np.pi*beta*t) / (1 - (2*beta*t)**2 + 1e-8)
    h[t==0] = 1.0  # avoid singularity at 0
    return h / np.sum(h)

h = rc_taps(beta=0.35, sps=sps, span=2)
tx = np.convolve(upsampled, h, mode='full')
delay = (len(h)-1)//2
sampled = tx[delay::sps]  # sample at symbol centers

print("Sampled (after RC filter):", np.round(sampled[:10], 3))
print("Original vs sampled:")
for i in range(len(symbols)):
    print(f"{symbols[i]:+d}  -->  {sampled[i]:+.3f}")
import matplotlib.pyplot as plt

# tx = RC-filtered waveform
# sps = samples per symbol
# symbols = original BPSK symbols
# h = RC filter taps

delay = (len(h)-1)//2           # filter delay (group delay)
symbol_centers = np.arange(len(symbols))*sps + delay
sampled = tx[delay::sps]        # sample at centers

plt.figure(figsize=(10,3))
plt.plot(tx[:len(symbols)*sps], '-o', markersize=3, label='RC-filtered waveform')

# mark the symbol decision points
for i, center in enumerate(symbol_centers):
    if center < len(tx):
        plt.plot(center, sampled[i].real, 'ro')  # red dot at decision instant

plt.title("RC-filtered waveform with symbol decision points")
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

