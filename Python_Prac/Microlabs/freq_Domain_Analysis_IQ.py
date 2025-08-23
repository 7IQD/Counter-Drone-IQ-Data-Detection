import numpy as np
import matplotlib.pyplot as plt
# 1. Load the raw IQ samples
filename = r"C:\IQ_Data\Prac_1.bin"
raw = np.fromfile(filename, dtype=np.uint8)
I = raw[0::2].astype(np.float32) - 127.5
Q = raw[1::2].astype(np.float32) - 127.5

# Combine the I & Q into complex64
IQ = I +1j*Q.astype(np.complex64)
print("raw to IQ", IQ)

# 2. Apply FFT to move from time → frequency domain
spectrum = np.fft.fft(IQ)
print("Spectrum Data - post fft:", spectrum)

# 3. Shift zero frequency (DC) to the center for better plotting
spectrum_shifted = np.fft.fftshift(spectrum)
print("Spectrum Data Shifted - post fftshift:", spectrum_shifted)
# 4. Convert to power (magnitude squared)
power = np.abs(spectrum_shifted) ** 2

# 5. Plot the result
# Spectrum - First
plt.plot(spectrum)
plt.title("Frequency Spectrum")
plt.xlabel("Frequency Bin")
plt.ylabel("Spectrum")
plt.show()

# Spectrum Shifted- Second
plt.plot(spectrum_shifted)
plt.title("Shifted Frequency Spectrum")
plt.xlabel("Frequency Bin")
plt.ylabel("Spectrum")
plt.show()

# Now Power
plt.plot(power)
plt.title("Power vs Frequency Bin Spectrum")
plt.xlabel("Frequency Bin")
plt.ylabel("Power")
plt.show()