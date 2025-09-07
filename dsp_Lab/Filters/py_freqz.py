import numpy as np
from scipy.signal import firwin, freqz
import matplotlib.pyplot as plt

numtaps = 21
fs = 4000 #sampling freq
cut_off = 1000 # 1 Khz
# FIR filter (cutoff 1 kHz at fs=4 kHz)
h = firwin(numtaps, cut_off, fs=fs)
#print("The coeficients", h[:10])

# Case 1: without fs
w_rad, H_rad = freqz(h, worN=1024)
# print(w_rad[:10]) #10 frequency points between 0 and 4000 Hz
# print(H_rad[:10]) #10 complex values (magnitude + phase)

# Case 2: with fs
w_Hz, H_Hz = freqz(h, worN=1024, fs=fs)
# print(w_Hz[:10]) #8 frequency points between 0 and 4000 Hz
# print(H_Hz[:10]) #8 complex values (magnitude + phase)

# Print side by side
print("Without fs (radians/sample):")
for i in range(len(w_rad)):
    print(f"w{[i]}= {w_rad[i]:.3f}rad/sample, H{[i]}={H_rad[i]:.3f}")

print("With fs (Hz/sample):")
for i in range(len(w_Hz)):
    print(f"w{[i]}= {w_Hz[i]:.3f}Hz, H{[i]}={H_Hz[i]:.3f}")

#Load the Plot of Linear scale (|H| vs frequency)
magnitude  = np.abs(H_Hz)
dB = 20*np.log10(magnitude)

plt.figure(figsize=(10,6)) 
plt.subplot(2,1,1)
plt.title("Linear |H| vs frequency")
plt.xlabel("Frequency[Hz]")
plt.ylabel("Magnitude|H|")
plt.grid(True)
plt.plot(w_Hz, magnitude)

#Load the Plot of dB scale (|H| vs frequency)
plt.subplot(2,1,2)
plt.title("dB|H| vs frequency")
plt.xlabel("Frequency[Hz]")
plt.ylabel("dB|H|")
plt.grid(True)
plt.tight_layout()
plt.plot(w_Hz, dB)

plt.show()



