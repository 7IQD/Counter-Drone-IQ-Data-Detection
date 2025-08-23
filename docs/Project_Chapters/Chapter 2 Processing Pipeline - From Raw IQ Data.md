# 📖 Processing Pipeline: From Raw IQ Data → Spectrum

### **Step 1. Read Raw IQ Data (from file)**

* Input: Binary file of **unsigned 8-bit integers (`uint8`)**.
* RTL-SDR stores data as **\[I0, Q0, I1, Q1, …]**.
* Action: Read file → convert to NumPy array.

```python
raw = np.fromfile(filename, dtype=np.uint8)
### **Step 2. Reshape into I & Q pairs**

* Group samples into pairs: `(I, Q)`.
* Shape: `(N/2, 2)`.

iq_pairs = raw.reshape(-1, 2)
I = iq_pairs[:,0].astype(np.float32)
Q = iq_pairs[:,1].astype(np.float32)

### **Step 3. Center and Normalize to \[-1, 1]**

* Raw range = \[0, 255].
* Subtract **127.5** to re-center around 0.
* Divide by 127.5 to scale to \[-1, 1].

I = (I - 127.5) / 127.5
Q = (Q - 127.5) / 127.5

### **Step 4. Form Complex IQ Signal**

* DSP works with **complex baseband samples**:

  $$
  x[n] = I[n] + jQ[n]
  $$

x = I + 1j*Q

### **Step 5. Perform FFT**

* Use **N-point FFT** to transform into frequency domain.
* Apply `fftshift` to center spectrum (DC in middle).

X = np.fft.fft(x, N)        # N-point FFT
X = np.fft.fftshift(X)      # shift 0 Hz to center

### **Step 6. Frequency Axis**

* Build frequency bins aligned with `fftshift`.
* Sampling frequency = `fs`.
* Bin spacing = `fs / N`.

freqs = np.fft.fftfreq(N, d=1/fs)
freqs = np.fft.fftshift(freqs)

### **Step 7. Spectrum Magnitude / Power**

* Magnitude Spectrum: `|X[k]|`
* Power Spectrum (dB):

  $$
  P[k] = 20 \log_{10} (|X[k]|)
  $$

magnitude = np.abs(X)
power_db = 20 * np.log10(magnitude + 1e-12)  # avoid log(0)

### **Step 8. Plot Spectrum**

* Plot `power_db` vs `freqs`.

import matplotlib.pyplot as plt

plt.plot(freqs/1e6, power_db)  # frequency in MHz
plt.title("Spectrum")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dB)")
plt.grid(True)
plt.show()

✅ **End Result**: A frequency spectrum of your captured IQ data, scaled, centered, and plotted in dB.
So, the **perfect structured sequence** is:

1. **Read raw file** (`uint8`)
2. **Reshape to I, Q pairs**
3. **Re-center & normalize** (\[0,255] → \[-1,1])
4. **Form complex IQ signal** (I + jQ)
5. **FFT** (transform to frequency domain)
6. **Shift FFT bins** (DC → center)
7. **Build frequency axis**
8. **Compute magnitude & power**
9. **Plot spectrum**
