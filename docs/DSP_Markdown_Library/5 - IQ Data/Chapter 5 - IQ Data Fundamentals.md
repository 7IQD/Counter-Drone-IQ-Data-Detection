# 📚 **IQ Data Fundamentals**

## 📘 **Chapter 1 — What is IQ Data?**

### 🧠 The Core Idea

IQ data is a way of representing a signal **as two components**:

* **I (In-phase)**: aligned with cosine wave
* **Q (Quadrature)**: aligned with sine wave (90° shifted)

Together they form a **complex number**:

$$
s(t) = I(t) + j \cdot Q(t)
$$

This representation allows SDR systems to track both **amplitude and phase** of signals — crucial for modulation, demodulation, and filtering.

---

### ✅ **Why I/Q Instead of Just Amplitude?**

| Challenge                          | IQ Benefit                              |
| ---------------------------------- | --------------------------------------- |
| Track both magnitude & phase       | Complex signal (I + jQ) captures both   |
| Shift signals up/down in frequency | IQ enables complex mixing               |
| Demodulate AM/FM/PSK/QAM           | Requires IQ to decode phase & amplitude |
| Digital filtering in baseband      | IQ makes it mathematically simple       |

---

### 🧪 **Python Example: Generate a Simple IQ Signal**

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 1000    # Sample rate
f = 50       # Signal frequency
t = np.arange(0, 0.1, 1/fs)  # Time axis

I = np.cos(2 * np.pi * f * t)  # In-phase
Q = np.sin(2 * np.pi * f * t)  # Quadrature

plt.plot(t, I, label='I (cos)')
plt.plot(t, Q, label='Q (sin)')
plt.grid(); plt.legend(); plt.title("I and Q vs Time")
plt.show()
```

---

### 🌀 **Plotting I vs Q (Phasor View)**

```python
plt.plot(I, Q)
plt.xlabel("I"); plt.ylabel("Q")
plt.title("Phasor Plot (I vs Q)")
plt.axis("equal"); plt.grid()
plt.show()
```

📍 **You’ll see a circle** — this is how the signal rotates in the IQ plane.

---

## 📘 **Chapter 2 — Real-Time IQ: Why It Looks Like Noise**

In theory, IQ signals are clean. But in real-world SDR receivers:

* Data changes dynamically
* Signals are modulated
* Noise and interference are added

So, the **phasor plot becomes a scatter cloud** of points — each point still being an (I, Q) sample.

---

### 📡 **Why the Random-Looking IQ Plot?**

| Factor               | What It Causes                    |
| -------------------- | --------------------------------- |
| Amplitude Modulation | Dots move in/out (radius changes) |
| Phase Modulation     | Dots rotate (angle changes)       |
| Noise                | Dots jitter randomly              |
| Multipath/Reflection | Smearing or distorted cloud       |
| Symbol transitions   | Spread in constellation clusters  |

---

### 🧪 **Simulate a Realistic IQ Constellation**

```python
fs = 10000  # Sampling frequency
fc = 1000   # Carrier frequency
t = np.arange(0, 0.01, 1/fs)

# Simulated BPSK signal with noise
message = np.random.choice([-1, 1], size=len(t))
I = message * np.cos(2 * np.pi * fc * t) + np.random.normal(0, 0.2, len(t))
Q = message * np.sin(2 * np.pi * fc * t) + np.random.normal(0, 0.2, len(t))

plt.figure(figsize=(6, 6))
plt.scatter(I, Q, s=2, alpha=0.5)
plt.title("Simulated Real-Time IQ Phasor Plot")
plt.xlabel("I"); plt.ylabel("Q")
plt.axis("equal"); plt.grid()
plt.show()
```

🔍 Each point is an (I, Q) sample — phase + amplitude encoded as position in the complex plane.

---

## 🔁 **How It All Comes Together**

* **I/Q samples** represent how signals vary **in time and phase**
* **In real time**, signals look random due to channel effects
* **Each I/Q pair** is a complete representation of a signal state at that moment

---

## 🧠 **Mini Summary Table**

| Concept        | What It Means                               |
| -------------- | ------------------------------------------- |
| I component    | Cosine-aligned part of signal               |
| Q component    | Sine-aligned part (90° shifted)             |
| Complex signal | I + jQ = full signal state                  |
| Phasor plot    | Visual plot of signal in I-Q space          |
| Constellation  | Clustered view of modulated symbols         |
| Random dots    | Result of noise, modulation, channel fading |

---


