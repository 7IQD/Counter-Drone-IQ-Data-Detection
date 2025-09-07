# 📘 Chapter 7.1: Your First Low-Pass FIR Filter – Time & Frequency Connection 🛠️

## **Objective**

* Smooth out high-frequency spikes in a signal
* See **numerical** and **visual** effects in both **time domain** and **frequency domain**
* Understand **transfer function** (freqz) as the “filter blueprint”

---

## **Step 1: Toy Signal – The Problem**

Imagine you have a **noisy sensor signal**:

| Sample n | x\[n] |              |
| -------- | ----- | ------------ |
| 0        | 1     |              |
| 1        | 2     |              |
| 2        | 10    | ← **Spike!** |
| 3        | 3     |              |
| 4        | 4     |              |
| 5        | 5     |              |

* Sampling frequency: `fs = 6 Hz` (toy example)
* Spike at n=2 → high-frequency component

> 🔍 **Observation:** Spike = sudden change → high-frequency

---

## **Step 2: FIR Filter Design 🧩**

We’ll use a **simple moving average FIR filter**:

* Length = 3
* Coefficients: `b = [1/3, 1/3, 1/3]`
* FIR → `a = [1]` → no feedback

> **Time-domain formula:**
> $y[n] = \frac{x[n] + x[n-1] + x[n-2]}{3}$

**Goal:** Smooth out spike → attenuate high frequency, keep slow trends

---

## **Step 3: Manual Computation Table 📝**

| n | x\[n] | x\[n-1] | x\[n-2] | y\[n] |
| - | ----- | ------- | ------- | ----- |
| 2 | 10    | 2       | 1       | 4.33  |
| 3 | 3     | 10      | 2       | 5     |
| 4 | 4     | 3       | 10      | 5.67  |
| 5 | 5     | 4       | 3       | 4     |

> ✅ Spike is **smoothed** in output

---

## **Step 4: Frequency Response – The Filter Blueprint 🔍**

Now we see **how the filter treats different frequencies** before applying it.

```python
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

b = [1/3, 1/3, 1/3]  # FIR
a = [1]

w, h = signal.freqz(b, a)
plt.plot(w/np.pi, 20*np.log10(abs(h)), 'r')
plt.title("Frequency Response of 3-Sample FIR Filter")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Amplitude (dB)")
plt.grid(True)
plt.show()
```

### **Interpretation Table**

| Feature         | Meaning                                                |
| --------------- | ------------------------------------------------------ |
| X-axis (0→π)    | Frequency from slow changes (0) to fastest changes (π) |
| Y-axis (dB)     | Gain: 0 dB = passed, <0 dB = attenuated                |
| Flat near 0     | Low-frequency trends pass → signal shape preserved     |
| Drops at high f | High-frequency spikes attenuated → smoothing achieved  |

> 🧩 **Link:** Time-domain spike → high-frequency → attenuated in freq response → smoothed output

---

## **Step 5: Python – Full DIY Example**

```python
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Toy real signal
x = np.array([1, 2, 10, 3, 4, 5])

# FIR moving average filter
b = np.ones(3)/3
a = [1]

# Apply filter
y = signal.lfilter(b, a, x)
print("Input x[n]:", x)
print("Filtered y[n]:", y)

# Time-domain plot
plt.figure(figsize=(8,4))
plt.plot(x, 'o-', label='Input x[n]')
plt.plot(y, 'x-', label='Filtered y[n]')
plt.title("Time-Domain FIR Filtering")
plt.legend()
plt.show()

# Frequency response
w, h = signal.freqz(b, a)
plt.figure(figsize=(8,4))
plt.plot(w/np.pi, 20*np.log10(abs(h)), 'r')
plt.title("Frequency Response of FIR Filter (dB)")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Amplitude (dB)")
plt.grid(True)
plt.show()
```
---

## **Step 6: Step-by-Step Understanding**

1. **Spike detected in time-domain** → high-frequency problem ✅
2. **FIR filter design** → choose coefficients to average 3 samples → smooth high-frequency spikes ✅
3. **Manual calculation** → see output numerically ✅
4. **Frequency response (freqz)** → see filter blueprint → high frequencies attenuated, low frequencies passed ✅
5. **Time-domain plot** → confirms smoothing effect matches freq response prediction ✅

> 💡 **Takeaway:**
> **Time-domain view:** What the signal looks like (spikes, trends)
> **Frequency-domain view:** What the filter does (attenuate or pass specific frequencies)
> **Link:** Frequency response predicts exactly what will happen to spikes

---

Let’s **strip it to the bare-bones, basic math level**, so you can see what `freqz`, `w`, and `h` really mean without heavy jargon.

---
# 🔹 freqz at Basic Math Level

### **1️⃣ Concept: One Frequency at a Time**

Imagine a filter is like a **weighting machine** for waves:

* Your input signal = a sine wave of a certain frequency $x[n] = \sin(\omega n)$
* The filter says: “I will multiply this sine by some number and maybe shift it a little in time.”

That “some number” = **h at that frequency**
That “shift in time” = **phase of h**

---

### **2️⃣ w = which frequency we are testing**

* Think of `w` as a **dial** from 0 → π rad/sample (slowest → fastest)
* Each value of `w` corresponds to a sine wave of that frequency

> Example: If `fs = 6 samples/sec`, Nyquist = 3 Hz
>
> * w = 0 → 0 Hz → DC → constant value
> * w = π → 3 Hz → highest frequency representable

---

### **3️⃣ h = how the filter treats that frequency**

* The filter multiplies that sine wave by a **complex number** $h = a + jb$
* Magnitude: $|h| = \sqrt{a^2 + b^2}$ → tells **how much of that sine passes**
* Phase: $\phi = \arctan(b/a)$ → tells **how much the sine shifts in time**

> Basic Math Analogy:

```text
Input sine: sin(ωn)
Output sine: |h| * sin(ωn + φ)
```

---

### **4️⃣ Step-by-step example (toy math)**

FIR filter: `b = [1/3, 1/3, 1/3]`, `a = [1]` (simple 3-sample moving average)

Pick frequency $ω = π$ (highest frequency possible for 6 samples/sec):

* Formula:

$$
H(e^{jω}) = b_0 + b_1 e^{-jω} + b_2 e^{-j2ω} 
= \frac{1}{3} + \frac{1}{3} e^{-jπ} + \frac{1}{3} e^{-j2π}
$$

* Compute each term (remember $e^{-jπ} = -1, e^{-j2π} = 1$)

$$
H(e^{jπ}) = 1/3 + 1/3 * (-1) + 1/3 * 1 = 1/3
$$

* Magnitude = |H| = 1/3 → the **high-frequency component is reduced**

---

### ✅ **Layman summary**

| Symbol | What it is                    | Basic Math                            |   |                    |
| ------ | ----------------------------- | ------------------------------------- | - | ------------------ |
| `w`    | frequency being tested        | 0 → π rad/sample                      |   |                    |
| `h`    | filter response               | h = b0 + b1 e^{-jw} + b2 e^{-j2w} + … |   |                    |
|        | magnitude = how strong output |                                       | h | = √(real² + imag²) |
|        | phase = how shifted in time   | φ = arctan(imag/real)                 |   |                    |

> 🎯 **Rule of thumb:**
> Time-domain spikes → high freq → check `w` near π → |h| tells how much spike survives → apply filter → smooth signal

---

