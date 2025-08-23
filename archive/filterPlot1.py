import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, firwin

# Filter specifications
cutoff = 0.3  # Normalized (1 = Nyquist)
num_taps_list = [11, 31, 61]  # Filter lengths

plt.figure(figsize=(15, 5))

for i, taps in enumerate(num_taps_list):
    h = firwin(numtaps=taps, cutoff=cutoff, window='hamming')
    w, H = freqz(h, worN=8000)

    # Plot Frequency Response
    plt.subplot(1, 3, i+1)
    plt.plot(w/np.pi, 20*np.log10(np.abs(H)), label=f'{taps} taps')
    plt.title(f'{taps}-tap FIR Filter\nFreq Response')
    plt.xlabel('Normalized Frequency (×π rad/sample)')
    plt.ylabel('Gain (dB)')
    plt.grid(True)
    plt.ylim([-100, 5])
    plt.axvline(cutoff, color='red', linestyle='--', label='Cutoff')
    plt.legend()

plt.tight_layout()
plt.show()