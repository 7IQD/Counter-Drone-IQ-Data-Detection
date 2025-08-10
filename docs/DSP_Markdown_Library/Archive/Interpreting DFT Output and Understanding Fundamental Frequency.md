### 📘 Chapter: Interpreting DFT Output and Understanding Fundamental Frequency
---
## 🎯 Chapter Objective
To clearly understand:
* What each DFT/FFT output value means
* How to calculate and interpret frequency bins
* What "fundamental frequency" is and why it matters
* How sampling rate and FFT size affect frequency resolution
* How to read FFT plots with confidence
---
## ✅ 1. What Does the DFT Actually Do?
The Discrete Fourier Transform (DFT) takes a time-domain signal and decomposes it into a set of **sinusoids** of different frequencies, amplitudes, and phases.
The DFT is defined as:
$$
X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j 2\pi kn/N}
$$
Where:
* $x[n]$: input signal (time domain)
* $X[k]$: output spectrum (frequency domain)
* $N$: number of samples
* $k$: index of the DFT bin
Each $X[k]$ tells you how much of frequency $f_k$ is present in the original signal.
---
📏 2. Frequency of Each Bin — The Key Formula
To map a DFT bin $k$ to its real-world frequency:
$$
f_k = \frac{k}{N} \cdot f_s
$$
Where:
* $f_k$: frequency represented by bin $k$
* $f_s$: sampling rate (Hz)
* $N$: number of samples (FFT size)
This tells us that:
* $X[0]$ = DC (0 Hz)
* $X[1]$ = fundamental frequency
* $X[k]$ = contains the strength (amplitude & phase) of $f_k$
---
🔁 3. What Is the Fundamental Frequency?
The **fundamental frequency** is the smallest frequency that your DFT can detect — it's the spacing between each frequency bin:
$$
f_{\text{fundamental}} = \frac{f_s}{N}
$$
It sets the **frequency resolution** of your FFT.
🔢 Example:
If:
* $f_s = 800$ Hz
* $N = 8$
Then:
* $f_{\text{fundamental}} = \frac{800}{8} = \boxed{100 \text{ Hz}}$
* Bin $k = 1$ represents 100 Hz
* Bin $k = 2$ → 200 Hz, and so on.
This means: **You can't detect anything in between these bins!** If your signal has a frequency at 125 Hz, it won't appear clearly unless you increase $N$.
---
📊 4. Interpreting DFT Output: Magnitude and Phase
Each $X[k]$ is a **complex number**:
$$
X[k] = \text{Re}(X[k]) + j\cdot \text{Im}(X[k])
$$
From this you can derive:
* **Amplitude** (strength of that frequency):
  $$
  |X[k]| = \sqrt{\text{Re}^2 + \text{Im}^2}
  $$
* **Phase** (angle/offset of that frequency):
  $$
  \angle X[k] = \tan^{-1}\left(\frac{\text{Im}}{\text{Re}}\right)
  $$
Use these to:
* Visualize the **spectrum**
* Reconstruct or modify specific frequency components
---
🧠 5. Symmetry of DFT for Real Signals
If your input $x[n]$ is real (not complex), then:
$$
X[N - k] = \overline{X[k]} \quad \text{(complex conjugate)}
$$
This means:
* You only need to look at the **first N/2+1 bins**
* The second half of the spectrum mirrors the first
That's why NumPy's `np.fft.rfft()` (real FFT) gives only the meaningful part.
---
📈 6. How to Read FFT Plots
import numpy as np
import matplotlib.pyplot as plt
fs = 800
N = 8
t = np.arange(N) / fs
x = np.cos(2 * np.pi * 100 * t)  # Cosine at 100 Hz
X = np.fft.fft(x)
freqs = np.fft.fftfreq(N, d=1/fs)
plt.stem(freqs, np.abs(X), use_line_collection=True)
plt.title("DFT Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
🔍 Interpreting the Plot

| Bin $k$ | Frequency $f_k$    | Meaning                                     |
| ------- | ------------------ | ------------------------------------------- |
| 0       | 0 Hz (DC)          | Average value (bias)                        |
| 1       | 100 Hz             | Main peak — cosine frequency                |
| 2       | 200 Hz             | No content here                             |
| 4       | 400 Hz (Nyquist)   | Half the sampling rate                      |
| 5–7     | Mirror of bins 1–3 | Symmetric, usually ignored for real signals |
✏️ Quick Practice Example
**Given:**
* $f_s = 1000$ Hz
* $N = 500$
**Then:**
* Fundamental frequency $f_{\text{fund}} = 1000 / 500 = 2$ Hz
* Bin $k = 100$ = $2 \times 100 = 200$ Hz
* You can only resolve multiples of 2 Hz
---
🎓 Key Takeaways
| Concept               | Key Point                                    |
| --------------------- | -------------------------------------------- |
| DFT output $X[k]$     | Complex value for frequency $f_k$            |
| Frequency per bin     | $f_k = \frac{k}{N} f_s$                      |
| Fundamental frequency | Smallest detectable frequency = $f_s / N$    |
| FFT resolution        | Increase $N$ for finer resolution            |
| Real signal DFT       | Symmetric — use first $N/2+1$ bins           |
| FFT plots             | Show magnitude (amplitude) of each frequency |
---
📘 What's Next?
In the next section, we’ll:
* Apply these fundamentals to **real noisy signals**
* See how **FIR filters** change the spectrum
* Compare **before/after FFT plots**
---
