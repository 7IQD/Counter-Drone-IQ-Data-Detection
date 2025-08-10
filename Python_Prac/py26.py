import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create float samples from -1.0 to +1.0
x = np.linspace(-1.0, 1.0, 100)
print(x)
# Step 2: Scale and quantize
x_scaled = (x * 127).astype(np.int8)
print("Scaled x values", x_scaled)
# Step 3: Recover (dequantize) back to float
x_recovered = x_scaled / 127.0
# Step 4: Calculate quantization error
error = x - x_recovered
print("Error Values:", error)
# Step 5: Plot original vs recovered and error
plt.figure(figsize=(12, 5))

# plt.subplot(1, 2, 1)
# # plt.plot(x, x_recovered, label='Recovered Float', color='green')
# # plt.plot(x, x, '--', label='Original Float', color='gray')
# plt.plot(x, x_recovered, label='Recovered', color='blue')
# plt.plot(x, x, '--', label='Original y=x', color='gray')
# plt.title('Original vs Recovered')
# plt.xlabel('Original Float')
# plt.ylabel('Recovered')
# plt.legend()
# plt.grid(True)

# plt.subplot(1, 2, 2)
plt.plot(x, error, color='red')
plt.title('Quantization Error')
plt.xlabel('Original Float')
plt.ylabel('Error (Original - Recovered)')
plt.grid(True)

plt.tight_layout()
plt.show()