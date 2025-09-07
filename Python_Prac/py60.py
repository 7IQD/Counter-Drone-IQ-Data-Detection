import numpy as np
import os

# Parameters
fs = 20000 # Samples per Sec
fc = 1e06 # Carrier Freq in Hz
t = 0.5 # in Sec
f = 1000 # in Hz
t =  np.arange(0, 0.5, 1/fs)
noise_amp = 0.2 # noise amplitude

print(len(t))  # Should print 10000
print(t[-10:]) # Last 10 samples, should be around 0.4995 s
I = np.sin(2*np.pi*f*t) + noise_amp*np.random.randn(len(t))
Q = np.cos(2*np.pi*f*t) + noise_amp*np.random.randn(len(t))
iq = I + 1j*Q
# Save IQ data as binary file
iq.astype(np.complex64).tofile('hello.iq')


