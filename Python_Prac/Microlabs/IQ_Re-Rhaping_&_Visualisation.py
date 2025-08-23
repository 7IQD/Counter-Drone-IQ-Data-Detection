import numpy as np
import matplotlib.pyplot as plt
N = 1024
fs = 2.4e6                 # sampling frequency
filename = r"C:\IQ_Data\Prac_1.bin"
raw = np.fromfile(filename, dtype=np.uint8)
I = (raw[0::2].astype(np.float32) - 128)/128.0
Q = (raw[1::2].astype(np.float32) - 128)/128.0

print("In phase 'I' data:", I[:10])
print("Quadrature Phase 'Q':", Q[:10])
iq = I + 1j*Q
# Truncate or select a block of N samples
iq = iq[:N]
fft_data = np.fft.fftshift(np.fft.fft(iq, N))
power_spectrum = 20*np.log10(np.abs(fft_data)+ 1e-12)

#Frequency axis
# Frequency axis (also shifted)
freq_axis = np.fft.fftshift(np.fft.fftfreq(N, 1/fs))

#plot
plt.figure(figsize=(10,6))
plt.plot(freq_axis, power_spectrum)
plt.title("FFT Spectrum of Captured IQ Data")
plt.xlabel("Normalised Frequency[cycles/sample]")
plt.ylabel("Power(dB)")
plt.grid(True)
plt.show()

