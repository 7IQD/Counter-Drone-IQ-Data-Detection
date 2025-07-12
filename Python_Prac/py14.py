# Generate random I and Q arrays
import numpy as np
I = np.random.uniform(-1, 1, size=10).astype(np.float32)
Q = np.random.uniform(-1, 1, size=10).astype(np.float32)

# Interleave
interleaved = np.empty(2 * len(I), dtype=np.float32)
interleaved[0::2] = I
interleaved[1::2] = Q

# De-interleave
I_restored = interleaved[0::2]
Q_restored = interleaved[1::2]

# Check
print("Original I:", I)
print("Restored I:", I_restored)
print("Original Q:", Q)
print("Restored Q:", Q_restored)