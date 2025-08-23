import numpy as np

# Input signal x[n] and impulse response h[n]
x = np.array([1, 2, 3])
h = np.array([1, 0, -1])

# Lengths
Nx = len(x)
Nh = len(h)
Ny = Nx + Nh - 1

# Output array
y = np.zeros(Ny)

# Manual convolution
for n in range(Ny):
    for k in range(Nx):
        if 0 <= n-k < Nh:
            y[n] += x[k]*h[n-k]
print("x[n] * h[n] = ", y)