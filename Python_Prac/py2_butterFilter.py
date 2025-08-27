
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Create the Noisy Scene ---
sample_rate = 1e6
N = 20000 # More samples to see the filter work better
t = np.arange(N) / sample_rate
print("Length of t vector is: ", len(t))

# A good signal at 25kHz and some noise
good_signal = np.cos(2 * np.pi * 25e3 * t)
# High frequency noise starting at 100kHz
noise = np.cos(2 * np.pi * 100e3 * t) * 0.5
noisy_signal = good_signal + noise

# --- 2. Design the Butterworth Bouncer ---
order = 2   # Try changing the order to 2 and 12
cut_off_hz = 50e03 # Our cut-off is nicely between good_signal and the noisy
normal_cutoff = cut_off_hz/(sample_rate/2)
b, a  = signal.butter(order, normal_cutoff, btype='low')

# --- 3. APPLY THE FILTER (The Magic Step!) ---
filtered_signal = signal.lfilter(b, a, noisy_signal)

# --- 4. Visualize the Result (Time Domain) ---
# Let's just look at the first 500 samples to see the wave forms
plt.figure(figsize=(10,4))
plt.plot(t[:500], noisy_signal[:500], 'r-', label='Noisy Signal')
plt.plot(t[:500], filtered_signal[:500], 'b-', linewidth=2, label='Filtered Signal')
plt.title('Before vs After Filtering')
plt.xlabel('Time(seconds)')
plt.legend()
plt.grid(True)
plt.show()