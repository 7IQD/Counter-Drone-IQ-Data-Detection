import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Our "do-nothing" filter coefficients
b_nothing = [1] # Numerator coefficients (input side)
a_nothing = [1] # Denominator coefficients (output side)

# Let's ask freqz what's up!
w_nothing, h_nothing = signal.freqz(b_nothing, a_nothing)
# What did we get?
print(f"w_nothing (angular frequencies): {w_nothing[:5]}...") # Showing just a few
print(f"h_nothing (complex frequency response): {h_nothing[:5]}...") # Showing just a few
# Plotting the Magnitude
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(w_nothing, np.abs(h_nothing))
plt.title('Magnitude Response (Do-Nothing Filter)')
plt.xlabel('Angular Frequency (rad/sample)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.axhline(1, color='red', linestyle='--', label='Unity Gain')
plt.legend()

# Plotting the Phase
plt.subplot(1, 2, 2)
plt.plot(w_nothing, np.angle(h_nothing))
plt.title('Phase Response (Do-Nothing Filter)')
plt.xlabel('Angular Frequency (rad/sample)')
plt.ylabel('Phase (radians)')
plt.grid(True)
plt.axhline(0, color='red', linestyle='--', label='Zero Phase')
plt.legend()

plt.tight_layout()
plt.show()