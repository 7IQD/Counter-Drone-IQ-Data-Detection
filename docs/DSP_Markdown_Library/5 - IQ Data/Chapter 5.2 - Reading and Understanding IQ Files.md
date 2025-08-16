# 📖 Chapter 5.2: Understanding IQ Data Values and the "Shifted Center"
---
## 1. What is IQ Data?

When we capture IQ data from an SDR (like RTL-SDR), the receiver provides **I (In-phase)** and **Q (Quadrature-phase)** samples. These samples represent the signal in the **complex plane**:

* `I` → the x-axis projection
* `Q` → the y-axis projection

Normally, in mathematics or DSP theory, we expect these samples to range between **negative and positive values**, oscillating around **0**.
Example of an ideal sine wave (In-phase part):

-1   -0.5   0   0.5   1

This wave is **centered at zero**.
---
## 2. What RTL-SDR Actually Gives

RTL-SDR hardware doesn’t store floats like `-1…+1`. Instead, for speed and efficiency, it stores samples as **unsigned 8-bit integers**:

* Values range from **0 → 255**
* `0` = minimum
* `255` = maximum
* The **middle point is 127 or 128**, not 0

So, if you captured the same sine wave, it might look like this in the raw file:

63   95   128   160   192

## 3. Why the Signal Looks “Shifted”

If you take these raw samples (`0…255`) and plot them directly:

* Instead of oscillating around 0, the signal floats around `128`.
* This is why it looks **shifted upward** in your plots.

🔑 The “center” we are referring to is **the mathematical zero line**, not the middle of your plot or file.

So what you’re really seeing is a wave that has been “lifted up” from zero.

## 4. Fixing the Shift (Recentering)

To make the data useful for DSP, we must **recenter** it:

* Subtract `127` (or `128`) from every sample.
* This converts `0…255` into `-128…+127`.

Example:

Raw data:     63    95   128   160   192
Recentered:  -65   -33     0    32    64

Now, the signal is **properly centered around 0** again.

## 5. Visualization Example

Imagine two plots:

**Raw Plot (0…255):**

             ___
      ___---'   `---___
___---                 ---___
         (center at 128)

**Recentered Plot (-128…+127):**
       ___
  ___-'   `-___
-'             `-
       (center at 0)

The second one is what DSP algorithms expect.

## 6. Why This Matters

If you don’t recenter the data:

* Fourier transforms (FFT) will give wrong frequency content.
* IQ constellation diagrams will appear shifted.
* Demodulation won’t work correctly, because algorithms assume **zero-centered samples**.

Once you subtract the offset, everything lines up as it should.

## 7. Quick Python Example

python
import numpy as np
import matplotlib.pyplot as plt

# Pretend we read from RTL-SDR file
raw_data = np.array([63, 95, 128, 160, 192], dtype=np.uint8)

# Recenter
centered_data = raw_data.astype(np.int16) - 128

# Plot comparison
plt.figure(figsize=(10,5))

plt.subplot(2,1,1)
plt.plot(raw_data, 'o-')
plt.title("Raw SDR Data (0-255, shifted up)")
plt.axhline(128, color='r', linestyle='--', label="Shifted center at 128")
plt.legend()

plt.subplot(2,1,2)
plt.plot(centered_data, 'o-')
plt.title("Recentered SDR Data (-128 to +127)")
plt.axhline(0, color='r', linestyle='--', label="True center at 0")
plt.legend()

plt.tight_layout()
plt.show()

This shows you exactly how the **raw data floats at 128**, and how **recentering brings it to zero**.

## 8. Takeaway

* The **“shifted center”** means the samples are centered at `128` instead of `0`.
* Always subtract `128` to get proper signed samples.
* Once recentered, you can safely do FFT, filtering, demodulation, or constellation plotting.

