import numpy as np
import matplotlib.pyplot as plt
Fs=1000
f=100
T=1
t=np.arange(0,T, 1/Fs)
I = np.cos(2*np.pi*f*t)
Q = np.sin(2*np.pi*f*t)
# Step 3: Form complex signal
IQ = I + 1j * Q

#plt.figure(figsize=(12,4))
# plt.subplot(1, 2, 1)
# plt.plot(t,I,label='I-Cos')
# plt.plot(t,I,label='Q-Sin', linestyle='--')
# plt.title('I and Q vs Time')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.legend()

# # Step 5: Plot IQ constellation (complex plane)
# plt.subplot(1, 2, 2)
# plt.plot(IQ.real, IQ.imag)
# plt.title(f'Complex IQ Signal(Circular Rotation)')
# plt.xlabel('I')
# plt.ylabel('Q')
# plt.grid(True)
# plt.axis('equal')


# plt.tight_layout()
# plt.show()

phase = np.angle(IQ)

plt.figure(figsize=(10,4))
plt.plot(t, phase)
plt.title('Phase vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Phase (radians)')
plt.grid(True)
plt.show()