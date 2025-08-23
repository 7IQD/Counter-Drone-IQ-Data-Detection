import numpy as np

z  = 3+4j
print("Complex part:", z)
print("Real part:", z.real)
print("Imaginary part:", z.imag)
print("Magnitude:", np.abs(z))
print("Phase in Radians:", np.angle(z))
print("Phase in Degrees:", np.angle(z, deg=True))

# Now with NumPy array of complex numbers
arr = np.array([1+1j, 2+2j, 3+4j], dtype=np.complex64)
print("\nArray of complex Nos:", arr)
print("Magnitude of complex Nos:", np.round(np.abs(arr),2))
print("Phase in Radians:", np.round(np.angle(arr), 2))
print("Phases (deg):", np.round(np.angle(arr, deg=True),2))
