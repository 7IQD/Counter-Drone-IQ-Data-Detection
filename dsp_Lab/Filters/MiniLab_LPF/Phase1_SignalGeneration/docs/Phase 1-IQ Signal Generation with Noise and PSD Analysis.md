# **Phase 1: IQ Signal Generation with Noise and PSD Analysis**

---

### **What the code does**

1. **Generates a clean IQ signal**:

   * I = cos(2πft), Q = sin(2πft)
   * `t` is the time vector based on sampling frequency `fs` and duration.

2. **Adds Gaussian noise**:

   * Noise scaled to achieve a desired **SNR**.
   * `np.sqrt(noise_power/2)` ensures the **total noise power** is correct for complex IQ (I & Q share power equally).

3. **Computes PSD**:

   * FFT of the noisy signal, shifted so frequency vector is centered at 0.
   * Power spectral density calculated as `|FFT|² / N` and converted to dB: `10 * log10(PSD)`.

4. **Plots three subplots**:

   * Clean IQ signal (I & Q)
   * Noisy IQ signal (I & Q)
   * PSD of IQ + noise

5. **Saves the figure**:

   * Automatically creates a `plots` folder if it doesn’t exist.
   * Saves figure as `Phase1_IQ_PSD.png`.

---

### **Key concepts to reinforce with practice**

* **Noise & SNR**: Understand why we scale by `sqrt(noise_power/2)` and how SNR is calculated.
* **RMS / signal power**: `np.mean(np.abs(iq_signal)**2)` gives the average power of the signal.
* **FFT & PSD**: How time-domain signals map to frequency-domain and why we use `fftshift`.
* **dB scale**: Power is logarithmic; remember `10*log10()` for power, not `20*log10()` (which is for amplitude).

---

### ✅ **Next steps for Phase 1**

* Play with **different SNR values** and observe the PSD: see how the noise floor rises.
* Try **longer durations or different frequencies** and see the effect on FFT resolution.
* Optionally, experiment with **adding noise only to I or Q** and see the difference in PSD.

---

### **Practice Guide / Exercises**

1. **Exercise 1 – Vary SNR**:
   Generate IQ signals with SNR = 0, 10, 20, 30 dB. Plot PSD and compare how noise floor changes.

2. **Exercise 2 – Vary Signal Frequency**:
   Keep SNR fixed, vary `f_signal` (500 Hz, 1 kHz, 2 kHz). Observe peak location in PSD.

3. **Exercise 3 – Time vs Frequency**:
   Double the duration. Observe how FFT resolution improves (peaks become sharper).

4. **Exercise 4 – Noise in I or Q only**:
   Add Gaussian noise to only I or only Q. Observe PSD and time-domain differences.

5. **Exercise 5 – Save multiple plots**:
   Automate saving clean IQ, noisy IQ, and PSD plots with meaningful filenames in the `plots` folder.

---

This forms a **compact, headfirst foundation** for understanding IQ signals, noise, RMS, and PSD — ready to move into **Phase 2: Filter Design**.


