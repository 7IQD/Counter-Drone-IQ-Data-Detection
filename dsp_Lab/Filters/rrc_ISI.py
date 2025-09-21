import numpy as np
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt 
# choose a tiny I sequence and Q sequence (simple QPSK example)
I = np.array([1, -1, 1, 1, -1])
Q = np.array([1,  1, -1, 1, -1])
sps = 32                        # samples per symbol (plot resolution)
ups_I = np.repeat(I, sps)       # spike train for I
ups_Q = np.repeat(Q, sps)       # spike train for Q
# print("Upscaled I:", len(ups_I))
# print("Upscaled Q:", ups_Q)
print(ups_I[16],ups_I[48],ups_I[80],ups_I[112],ups_I[144])

# --- get RRC taps (black box) ---

def rrc_taps(beta, sps, span):
    N = span * sps + 1
    t = (np.arange(N) - (N-1)/2) / sps
    h = np.zeros_like(t, dtype=float)
    for i, tt in enumerate(t):
        if abs(tt) < 1e-8:
            h[i] = 1.0 - beta + (4*beta/np.pi)
        elif abs(abs(4*beta*tt) - 1.0) < 1e-8:
            h[i] = (beta/np.sqrt(2)) * ((1+2/np.pi)*np.sin(np.pi/(4*beta)) + (1-2/np.pi)*np.cos(np.pi/(4*beta)))
        else:
            h[i] = (np.sin(np.pi*tt*(1-beta)) + 4*beta*tt*np.cos(np.pi*tt*(1+beta))) / (np.pi*tt*(1-(4*beta*tt)**2))
    return h / np.sum(h)   # normalize energy

beta = 0.35
span = 6
taps = rrc_taps(beta, sps, span)   # <-- this is the "magic cookie-cutter"; treat it as black box
print("These are tap values", len(taps))
Nfft = len(ups_I) + sps * span   # ensure linear convolution, no wrap-around

#Converts time-domain spike train into frequency domain.
X_I = np.fft.fft(ups_I, Nfft)

#FFT of RRC filter
H = np.fft.fft(taps, Nfft)

#Multiply in frequency domain
Y_I = X_I * H

#Inverse FFT → back to time domain
shaped_I_signal = np.fft.ifft(Y_I).real

#Compute Group Delay
gd = (len(taps) - 1) // 2  # number of samples delay
print("The length of taps", len(taps))
print("Group Delay Samples", gd)
print("Length of shaped_I_signal ", len(shaped_I_signal))

#Crop / shift waveform
shaped_I_signal_aligned = shaped_I_signal[gd : gd + len(ups_I)]

# --- Step 5: Plot pre- and post-filter ---
plt.figure(figsize=(12,5))
plt.plot(ups_I, 'o-', label='Original spikes (upsampled)')
plt.plot(shaped_I_signal_aligned, '-', label='RRC-shaped & aligned')
plt.title('Pre- and Post-RRC Filtering')
plt.xlabel('Sample index')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()

