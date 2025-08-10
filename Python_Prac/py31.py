import numpy as np

Fs= 10 # Sampling Freq
f = 1 # Hz
t  = np.arange(0, 1, 1/Fs)
z =  np.exp(1j*2*np.pi*f*t)
phase_deg = np.rad2deg(np.unwrap(np.angle(z)))
print("Angles", phase_deg)
print("Real Values:", z.real)
print("Imaginary Values:", z.imag)

