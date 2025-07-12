import numpy as np
I = np.array([1,2,3,4,5], dtype=np.float32)
Q = np.array([1.5, 2.5, 3.5, 4.5, 5.5],dtype=np.float32)

interleaved = np.empty(2*len(I), dtype=np.float32)
interleaved[0::2] = I
print("Interleaved I:initialised", interleaved)
interleaved[1::2] = Q
# print("Interleaved Q:initialised", interleaved)
# print("I array",I)
# print("Q array", Q)
# print("Interleaved IQ:", interleaved)
I_restored = interleaved[0::2]
Q_restored = interleaved[1::2]
print("I values restored", I_restored)
print("I values restored", Q_restored)