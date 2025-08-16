import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1e4  # Sampling frequency, Hz
t = np.arange(0, 1, 1/fs)  # 1 second of samples
f_signal = 200  # Signal frequency in Hz

# Simulate IQ components
I = np.cos(2 * np.pi * f_signal * t) # In-phase
Q = np.sin(2 * np.pi * f_signal * t + 5*np.pi%4)  # Quadrature

# Complex representation
IQ = I + 1j*Q

# Magnitude and Phase
magnitude = np.abs(IQ)
phase = np.angle(IQ)

# Plot I & Q
plt.figure(figsize=(12,4))
plt.plot(t, I, label='I')
plt.plot(t, Q, label='Q')
plt.title('I and Q Components')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# Plot Phasor (Complex plane)
plt.figure(figsize=(6,6))
plt.plot(I, Q, '-o')
plt.title('Phasor Plot (I vs Q)')
plt.xlabel('I')
plt.ylabel('Q')
plt.axis('equal')
plt.grid(True)
plt.show()


# Plot Magnitude and Phase
plt.figure(figsize=(12,4))
plt.subplot(2,1,1)
plt.plot(t, magnitude)
plt.title('Magnitude of IQ Signal')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t, phase)
plt.title('Phase of IQ Signal')
plt.xlabel('Time (s)')
plt.ylabel('Phase (radians)')
plt.grid(True)
plt.tight_layout()
plt.show()
