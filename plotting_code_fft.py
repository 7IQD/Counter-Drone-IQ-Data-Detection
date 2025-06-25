import numpy as np
import matplotlib.pyplot as plt

# 1. Define time-domain signal
x = np.array([1, 2, 3, 4])  # 4-point signal
print(x)
# 2. Compute FFT
X = np.fft.fft(x) 
#This is where the Fast Fourier Transform happens.
#X is now a list of complex numbers, representing frequency bins.
#Each X[k] shows how much of frequency component k is present in the signal.
# Example: X[0] is the DC component (average), X[1] is the first frequency bin, and so on.
N = len(x) #N is just 4 here — the number of samples.
k = np.arange(N)  
# create frequency bin indices

# Now Plot Time Domain Sub Plot
# Create larger figure
plt.figure(figsize=(14, 4))  # Wider
plt.subplot(1, 3, 1)
plt.stem(k, x)
#This is a discrete-time plot: it draws vertical lines ("stems") from the x-axis (baseline) to each point (k, x[k])
#It also places a dot or marker at the top of each stem.

plt.title("Time Domain")
plt.xlabel("Sample index (n)")
plt.ylabel("x[n]")
plt.grid(True)

# Now Plot Magnitude Sub Plot
plt.subplot(1, 3, 2)
plt.stem(k, np.abs(X))
# plots magnitude of FFT
#[10.00, 2.83, 2.00, 2.83] --- calculated magnitude 
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency bin (k)")
plt.ylabel("|X[k]|")
plt.grid(True)

#Magnitude Spectrum
plt.subplot(1, 3, 3)
plt.stem(k, np.angle(X))
plt.title("Phase Spectrum")
plt.xlabel("Frequency bin (k)")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.show()