# **Chapter 4.6: Types of Windows — Choosing the Right Edge Fader**
---
## **4.1 Why Different Windows Exist**

* FFT assumes **repeating signals**.
* Abrupt edges → **spectral leakage**.
* Different windows **shape the edges differently**, trading off:

  1. **Leakage reduction** (clean FFT peak)
  2. **Main lobe width** (frequency resolution)
  3. **Side lobe amplitude** (spurious frequencies)

> Think of each window as a **different “fade-in/fade-out curve”**.
---
## **4.2 Common Window Types**

| Window                    | Shape / Behavior                          | When to Use / Intuition                                      |
| ------------------------- | ----------------------------------------- | ------------------------------------------------------------ |
| **Rectangular**           | Flat (no fade)                            | Best frequency resolution, poor leakage; like **no ramp**.   |
| **Hanning / Hann**        | Smooth, symmetric 0 → 1 → 0               | Most commonly used; balances leakage and resolution.         |
| **Hamming**               | Similar to Hanning, slightly higher edges | Reduces side-lobes more; good for audio signals.             |
| **Blackman**              | Very smooth edges, wider main lobe        | Best leakage reduction; slightly worse frequency resolution. |
| **Bartlett / Triangular** | Linear ramp up and down                   | Simple, good for quick experiments; moderate leakage.        |
| **Kaiser**                | Adjustable shape via parameter β          | Flexible control: trade-off leakage vs resolution.           |
---
## **4.3 Headfirst Intuition**

* **Edges define leakage:** higher fade → less leakage.
* **Middle defines amplitude preservation:** flatter middle → better energy retention.
* **Trade-off:** Narrow main lobe → better frequency resolution; wider main lobe → less leakage.
* Windows are **applied sample-by-sample**: same principle as Hanning.

> Think of it like **choosing a slope for a ramp**: shallow slope = smooth transition (less leakage), steep slope = abrupt (more leakage).
---
## **4.4 Choosing a Window: Simple Rules**

1. **Hanning:** default, general-purpose, audio/FFT.
2. **Hamming:** if you want slightly lower side-lobes.
3. **Blackman:** if spectral leakage is critical (e.g., measuring small signals near strong tones).
4. **Rectangular:** only if edges naturally align with zero or you want maximum frequency resolution.
5. **Kaiser:** when you want **custom control** over trade-offs.
---
### **4.5 Practical Example in Python**

```python
import numpy as np

N = 16
windows = {
    "Rectangular": np.ones(N),
    "Hanning": np.hanning(N),
    "Hamming": np.hamming(N),
    "Blackman": np.blackman(N)
}

for name, w in windows.items():
    print(f"{name} window: {np.round(w, 2)}")
```

**Observation:**

* Rectangular → all ones → no fade.
* Hanning / Hamming → smooth fade 0 → 1 → 0.
* Blackman → even smoother edges, lower side-lobes.

---
### **4.6 Key Takeaways**
1. **Window = edge shaping tool**; different windows shape differently.
2. **Trade-offs**: leakage vs resolution vs side-lobe amplitude.
3. **Default:** Hanning → safe and general-purpose.
4. **Remember:** Behavior matters more than internal formula.

