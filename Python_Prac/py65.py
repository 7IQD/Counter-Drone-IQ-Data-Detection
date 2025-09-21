import numpy as np
import matplotlib.pyplot as plt

# --- Step 1 (re-creation for context) ---
sample_array = np.zeros(64)
sample_array[32] = 1

# --- Step 2 (re-creation for context) ---
alpha = 0.5
samples_per_symbol = 8
filter_length = 64
n = np.arange(-filter_length // 2, filter_length // 2)

h_rrc = np.sinc(n / samples_per_symbol) * np.cos(np.pi * alpha * n / samples_per_symbol) / (1 - (2 * alpha * n / samples_per_symbol)**2)
h_rrc[n == samples_per_symbol / (2 * alpha)] = np.pi / 4.0 * np.sinc(1 / (2 * alpha))
h_rrc[n == -samples_per_symbol / (2 * alpha)] = np.pi / 4.0 * np.sinc(1 / (2 * alpha))
h_rrc /= np.sum(h_rrc)

filtered_array = np.convolve(sample_array, h_rrc, mode='same')

# --- Step 3: Plot the Results ---

plt.figure(figsize=(10, 6))

# Plot the original impulse
plt.stem(np.arange(len(sample_array)), sample_array, basefmt=" ", linefmt='b-', markerfmt='bo', label='Original Impulse (Pre-RRC)')

# Plot the filtered, shaped pulse
plt.plot(np.arange(len(filtered_array)), filtered_array, 'r-', linewidth=2, label='RRC Filtered Pulse (Post-RRC)')

plt.title('RRC Pulse Shaping: From an Impulse to a Shaped Pulse')
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()