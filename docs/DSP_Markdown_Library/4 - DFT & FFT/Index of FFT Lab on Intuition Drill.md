## **Index of FFT lab on Intuition Drill**

### **Lab 1 — Meet the Players: f₀, fₛ, and N**

**Focus:** How signal frequency (f₀), sampling frequency (fₛ), and number of samples (N) connect.
**Goal:** Understand Δf = fₛ / N and how it decides bin spacing.
**Drill:** Pick N = 8, fₛ = 8 Hz → Δf = 1 Hz. Place a 2 Hz sine and see it *exactly* in bin 2.

---

### **Lab 2 — When the Bins Fit Like Lego**

**Focus:** Perfect bin alignment (integer multiples of Δf).
**Goal:** See how a signal with exactly k·Δf Hz frequency lands in one bin with no leakage.
**Drill:** Keep fₛ = 32 Hz, N = 8 → Δf = 4 Hz. Try signals at 4 Hz, 8 Hz, 12 Hz.

---

### **Lab 3 — When the Lego Bricks Don’t Fit**

**Focus:** Spectral leakage.
**Goal:** Observe what happens when f₀ is *not* a bin frequency.
**Drill:** With fₛ = 32 Hz, N = 8 → Δf = 4 Hz, put f₀ = 5 Hz and see the spread in bins.

---

### **Lab 4 — The Window Effect**

**Focus:** Why the FFT assumes the signal repeats forever.
**Goal:** Show how the rectangular window causes leakage, and how Hamming/Hann windows reduce it.
**Drill:** Use same 5 Hz case from Chapter 3, compare no window vs. Hann.

---

### **Lab 5 — Time–Frequency Tradeoff**

**Focus:** How N controls resolution.
**Goal:** See Δf get smaller as N grows, improving your ability to separate close frequencies.
**Drill:** Compare N = 8 vs. N = 64 for two signals at 10 Hz and 11 Hz.

---

### **Lab 6 — The Mirror World**

**Focus:** Positive and negative frequencies.
**Goal:** Understand fftfreq output and symmetry for real signals.
**Drill:** Plot np.fft.fftfreq and watch bins > fₛ/2 become negative.

---

### **Lab 7 — Phase is Not Just Decoration**

**Focus:** Interpreting FFT phase output.
**Goal:** Connect time-domain shift with phase change in frequency domain.
**Drill:** Delay a sine wave by ¼ cycle and see a 90° phase shift in its bin.

---

### **Lab 8 — DC: The Quiet Tenant at 0 Hz**

**Focus:** Why bin 0 means “average value.”
**Goal:** Add a constant offset to your signal and see it appear only at bin 0.
**Drill:** Sine wave vs. sine wave + 3.

---

### **Lab 9 — Aliasing: Folding Beyond Nyquist**

**Focus:** What happens when f₀ > fₛ/2.
**Goal:** Show how high-frequency signals masquerade as lower ones.
**Drill:** fₛ = 32 Hz, generate f₀ = 20 Hz and 28 Hz; watch folding.

---

### **Lab 10 — Building the FFT Reflex**

**Focus:** Putting it all together to read FFT plots like a story.
**Goal:** Predict before running: location, height, width, and phase of peaks.
**Drill:** Randomly choose f₀, fₛ, N — predict FFT outcome, then verify.

