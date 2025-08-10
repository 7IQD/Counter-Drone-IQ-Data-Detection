import numpy as np
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt

fs = 1000  # sample rate
f = 50     # frequency
t = np.arange(0, 0.01, 1/fs)

I = 0.9 * np.cos(2 * np.pi * f * t)
Q = 0.9 * np.sin(2 * np.pi * f * t)

# Add a spike to simulate overload
I[10:13] += 0.3
Q[10:13] += 0.3

iq_float = np.empty(I.size + Q.size)
iq_float[0::2] = I
iq_float[1::2] = Q

# Scaling
peak = np.max(np.abs(iq_float))
scale_factor = 127 / peak
iq_scaled = (iq_float * scale_factor).astype(np.int8)
plt.figure(figsize=(10, 4))
plt.plot(iq_float[:40], label="Float32 IQ", linewidth=2)
plt.plot(iq_scaled[:40], label="Scaled int8 IQ", linestyle='--', marker='o')
plt.legend()
plt.title("IQ Scaling Visualization")
plt.grid(True)
plt.show()
