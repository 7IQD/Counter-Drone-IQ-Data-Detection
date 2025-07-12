import numpy as np

signal = np.array([2, 4, 6, 8, 10])
kernel = np.array([1, 0, -1])

def apply_filter(signal, kernel):
    output = []
    for i in range(len(signal)-len(kernel)+1):
        segment = signal[i:i+len(kernel)]
        y = np.dot(segment, kernel)
        output.append(y)
    return np.array(output)
filtered_signal = apply_filter(signal, kernel)
print("Filterd Output:", filtered_signal)