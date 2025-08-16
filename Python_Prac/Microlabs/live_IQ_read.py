from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

filename = r"C:\IQ_Data\Prac_1.bin"
data = np.fromfile(filename, dtype=np.uint8)
print(f"Total Samples Read: {len(data)}")
if len(data) % 2 != 0:
    print("Odd No of Samples")
    data = data[:-1]
else:
    print("Already the file contains Even No of Samples")
iq_data = data.reshape(-1, 2)
#print (iq_data)
I = iq_data[:1000,0]
Q = iq_data[:1000,1]
print(f"{I}\n{Q}")
magnitude = np.sqrt(I**2 + Q**2)
phase = np.arctan2(Q, I)

plt.figure(figsize=(12,5))

plt.subplot(2,1,1)
plt.plot(magnitude)
plt.title("Magnitude of IQ Samples")
plt.xlabel("Sample Index")
plt.ylabel("Magnitude")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(phase)
plt.title("Phase of IQ Samples")
plt.xlabel("Sample Index")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.show()


# plt.figure(figsize=(10,4))
# plt.title("Display of IQ Data Capture")
# plt.plot(I[:1000], label='I')
# plt.plot(Q[:1000], label='Q')
# plt.legend()
# plt.xlabel("Sample Index")
# plt.ylabel("Amplitude")
# plt.show()

# Plot Phasor (Complex plane)
#phase = np.pi%2
# I_shifted = I*np.cos(phase) - Q*np.sin(phase)
# Q_shifted = I*np.sin(phase) + Q*np.cos(phase)
# print("I_Shifted Signal:", I_shifted)
# print("Q_Shifted Signal:", Q_shifted)
# plt.figure(figsize=(6,6))
# plt.plot(I_shifted, Q_shifted)
# #plt.scatter(I_shifted, Q_shifted, s=5)
# plt.title('Phasor Plot (I vs Q)')
# plt.xlabel('I_shifted')
# plt.ylabel('Q_shifted')
# plt.axis('equal')
# plt.grid(True)
# plt.show()

# #Constellation Plot
# plt.figure(figsize=(5,5))
# plt.scatter(I[:2000], Q[:2000], s=1)
# plt.title("IQ Constellation (First 2000 samples)")
# plt.xlabel("I")
# plt.ylabel("Q")
# plt.axis('equal')
# plt.show()

