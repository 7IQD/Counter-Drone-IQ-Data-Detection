import numpy as np

N = 8
t = np.linspace(0, 1, N, endpoint=False)
signal = np.sin(2*np.pi*1*t + np.pi/4)  # Phase-shifted sine
window = np.hanning(N)
signal_windowed = signal * window

# Print table
print("\nSample n| x[n] | w[n] | x[n]*w[n]")
for n in range(N):
    print(f"{n:2d}| {signal[n]:6.3f} | {window[n]:6.3f} | {signal_windowed[n]:6.3f}")
