Here’s a **compiled set of concise yet complete notes** on:

* **Fundamental Frequency**
* **Normalized Frequency**
* **Normalization Factor $\frac{k}{N}$**
* **DFT Bin Interpretation**
* **Real-World Mapping**

---

# 📘 **Understanding Frequency in DFT: A Practical Guide**

---

## 🔹 1. **Fundamental Frequency**

**Definition**:
The **fundamental frequency** in the context of DFT is the **lowest non-zero frequency** that can be resolved by the transform.

$$
f_{\text{fundamental}} = \frac{f_s}{N}
$$

Where:

* $f_s$: Sampling frequency (Hz)
* $N$: Number of time-domain samples in DFT

**Interpretation**:

* It's the frequency corresponding to **1 full cycle** over **N samples**.
* All other DFT bin frequencies are **integer multiples (harmonics)** of this.

---

## 🔹 2. **Normalized Frequency**

**Definition**:
The frequency expressed as a **fraction of the sampling rate**, i.e., **cycles per sample**.

$$
f_{\text{norm}} = \frac{f_{\text{actual}}}{f_s} = \frac{k}{N}
$$

Where:

* $k$: DFT bin index
* $N$: DFT size
* $f_{\text{actual}}$: Actual frequency in Hz

**Units**: Cycles per sample (unitless)

**Range**:

* For real signals, normalized frequency typically spans $[0, 0.5]$ due to symmetry (Nyquist limit).
* For complex signals, full range is $[0, 1)$ or $[-0.5, 0.5)$

---

## 🔹 3. **Normalization Factor $\frac{k}{N}$**

**This is the core frequency index of DFT** — it determines:

* The rate of rotation of the complex exponential used in bin $k$
* The **harmonic component** DFT is measuring

$$
X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j 2\pi \frac{k}{N} n}
$$

* $\frac{k}{N}$: Normalized frequency
* $k$: Bin number = $k$-th harmonic

---

## 🔹 4. **Harmonic Interpretation**

Each DFT bin $k$ measures how much of the $k$-th harmonic (i.e., sinusoid completing $k$ cycles in $N$ samples) is present in the signal.

$$
f_k = k \cdot f_{\text{fundamental}} = \frac{k}{N} \cdot f_s
$$

So:

* **Bin 0** → DC component (0 Hz)
* **Bin 1** → 1 cycle over N samples → fundamental
* **Bin 2** → 2nd harmonic
* ...
* **Bin $N/2$** → Nyquist frequency (if $N$ is even)

---

## 🔹 5. **Physical Interpretation of Frequencies**

| Type                        | Formula                 | Units         | Meaning                                 |
| --------------------------- | ----------------------- | ------------- | --------------------------------------- |
| Fundamental                 | $\frac{f_s}{N}$         | Hz            | Lowest non-zero freq. DFT can detect    |
| Actual freq. of bin $k$     | $\frac{k}{N} \cdot f_s$ | Hz            | Frequency component measured in bin $k$ |
| Normalized freq. of bin $k$ | $\frac{k}{N}$           | cycles/sample | Fraction of sampling rate               |
| Harmonic number             | $k$                     | dimensionless | $k$-th sinusoid in the basis            |
## 🔹 6. **Example:**
Let’s say:
* $f_s = 8000 \, \text{Hz}$
* $N = 8$
Then:

* $f_{\text{fundamental}} = \frac{8000}{8} = 1000 \, \text{Hz}$
* Bin 2:
  * Normalized frequency = $\frac{2}{8} = 0.25$
  * Actual frequency = $0.25 \cdot 8000 = 2000 \, \text{Hz}$
  * Harmonic = 2nd

## 🔹 7. **Why It Matters**

* **Normalized frequency** lets you work **independent of sampling rate** — useful for algorithms, plotting, etc.
* **Actual frequency** gives **physical meaning** — e.g., audio tone, RF carrier.
* **Fundamental frequency** shows your resolution: you **can’t distinguish** between signals closer than $\frac{f_s}{N}$.
* Understanding $\frac{k}{N}$ is essential to interpreting DFT results correctly.

## 📝 Summary Table

| Concept               | Expression              | Interpretation                                   |
| --------------------- | ----------------------- | ------------------------------------------------ |
| Fundamental frequency | $\frac{f_s}{N}$         | Lowest resolvable frequency                      |
| Normalized frequency  | $\frac{k}{N}$           | Cycles per sample                                |
| Actual frequency      | $\frac{k}{N} \cdot f_s$ | Hz                                               |
| Harmonic number       | $k$                     | k-th sinusoidal basis                            |
| Nyquist frequency     | $\frac{f_s}{2}$         | Maximum representable frequency for real signals |


