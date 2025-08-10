
import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
# Setup RTL-SDR
sdr = RtlSdr()
sdr.sample_rate = 2.4e6       # Hz
sdr.center_freq = 98.4e6       # Hz (try an FM radio band)
sdr.gain = 'auto'
# Read IQ samples
samples = sdr.read_samples(256*1024)
sdr.close()
# FFT and frequency axis
fft_vals = np.fft.fftshift(np.fft.fft(samples))
power_db = 20 * np.log10(np.abs(fft_vals))
freqs = np.linspace(-sdr.sample_rate/2, sdr.sample_rate/2, len(power_db)) + sdr.center_freq
# Plot
plt.figure(figsize=(10, 5))
plt.plot(freqs / 1e6, power_db, color='green')
plt.title("Live Spectrum from RTL-SDR")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dB)")
plt.grid(True)
plt.tight_layout()
plt.show()
