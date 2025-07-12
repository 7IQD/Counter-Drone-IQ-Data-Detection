import numpy as np

# Step 1: Define the raw bit stream (could be any length)
bits = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=np.uint8)

# Step 2: BPSK Mapping — Convert bits to symbols
# 1 → +1, 0 → -1
symbols = 2 * bits - 1  # Vectorized formula

# Step 3: Generate I and Q
I = symbols.astype(np.float32)  # In-phase carries the data
Q = np.zeros_like(I)            # Q is zero for BPSK

# Step 4: Form complex IQ values (optional — for visualization or debugging)
iq_complex = I + 1j * Q

# Step 5: Interleave I and Q into a flat array: [I0, Q0, I1, Q1, ..., IN, QN]
iq_interleaved = np.empty(2 * len(I), dtype=np.float32)
iq_interleaved[0::2] = I  # Even indices → I
iq_interleaved[1::2] = Q  # Odd indices  → Q

# Step 6: Save to binary file (.bin format)
iq_interleaved.tofile("bpsk_iq_output.bin")

# Optional: Print to confirm
print("Bits:       ", bits)
print("Symbols:    ", symbols)
print("I values:   ", I)
print("Q values:   ", Q)
print("IQ Complex: ", iq_complex)
print("IQ Interleaved (saved):", iq_interleaved)