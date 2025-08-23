import numpy as np
import matplotlib.pyplot as plt
fs = 2.4e6  # Sampling rate in Hz (adjust to your SDR)

#Step 1: Load IQ Data
filename = r"C:\IQ_Data\Prac_1.bin"
raw = np.fromfile(filename, dtype=np.uint8)

# Convert to float32 and center around 0
I = raw[0::2].astype(np.float32) - 127.5
Q = raw[1::2].astype(np.float32) - 127.5

# Combine I & Q into complex64
IQ = (I + 1j*Q).astype(np.complex64)
N = len(IQ)

#Step 2: Calculation of Bins
spectrum = np.fft.fft(IQ)
spectrum_shifted = np.fft.fftshift(spectrum)

#Step 3: Compute Power
power = np.abs(spectrum_shifted)**2

#Step 4: Create Frequency Vector
# Now IQ, fs, N are already defined we Compute FFT
freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs))

# Find peak
peak_index = np.argmax(power)
peak_freq  = freq[peak_index] 
peak_power = power[peak_index]

#Step 5: Plot Power Spectrum
# === Find peak ===
peak_index = np.argmax(power)
peak_freq = freq[peak_index]
peak_power = 10*np.log10(power[peak_index])

# === Plot ===
plt.figure(figsize=(10,5))
plt.plot(freq, 10*np.log10(power), label="Spectrum")
plt.scatter([peak_freq], [peak_power], color="red", zorder=5, label="Peak")

plt.annotate(f"{peak_freq:.1f} Hz\n{peak_power:.1f} dB",
             xy=(peak_freq, peak_power),
             xytext=(peak_freq, peak_power+10),
             ha="center", color="red", fontsize=10,
             arrowprops=dict(facecolor="black", arrowstyle="->"))

plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (dB)")
plt.title("Spectrum with Peak Marker")
plt.legend()
plt.show()