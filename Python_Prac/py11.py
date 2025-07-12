import numpy as np

# # Generate 8 random bits: 0 or 1
# bits = np.random.randint(0, 2, 8)
# print("Bitstream:", bits)

# symbols = 2*bits -1
# print("Mapped BPSK symbols", symbols)
# samples_per_symbol = 100
# symbol_stream = np.repeat(symbols, samples_per_symbol)
# print("Length of symbol stream (samples):", symbol_stream)
symbols = np.array([1, -1, 1, -1])          # Just 4 symbols
symbol_rate = 1000
samples_per_symbol = 5
fs = symbol_rate * samples_per_symbol

symbol_stream = np.repeat(symbols, samples_per_symbol)
t = np.linspace(0, len(symbols)/symbol_rate, len(symbol_stream), endpoint=False)

print("Symbols:        ", symbols)
print("Symbol stream:  ", symbol_stream)
print("Sample rate fs: ", fs)
print("Time step Ts:   ", 1/fs)
print("Time vector:    ", t)
