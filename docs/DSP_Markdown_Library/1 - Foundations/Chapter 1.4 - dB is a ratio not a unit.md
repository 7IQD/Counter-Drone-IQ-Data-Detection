## 1. dB is a ratio, not a unit

* dB (decibel) = a **way to compare two powers** on a logarithmic scale.
* Why log? Because our ears, radios, antennas, amplifiers — all work across *huge* ranges (from nano-watts to kilowatts).
* Without log, graphs would be either microscopic or gigantic.

---

## 2. The formula

* **Power ratio in dB**:

  $$
  \text{dB} = 10 \cdot \log_{10} \left( \frac{P}{P_\text{ref}} \right)
  $$

* But in IQ signals, we often deal with **voltages or magnitudes** (not direct power).
  Power ∝ Voltage².
  So when comparing **voltage amplitudes**:

  $$
  \text{dB} = 20 \cdot \log_{10} \left( \frac{V}{V_\text{ref}} \right)
  $$

That’s why your code uses **20·log10(|FFT|)**.
Because FFT gives us **magnitude (like volts)**, and we want **power in dB**.

---

## 3. Quick head-tricks (cheat sheet)

* **+3 dB ≈ ×2 power**
* **+10 dB = ×10 power**
* **+20 dB = ×10 voltage** (because 20 log10 handles voltage)
* **−3 dB ≈ half the power**
* **0 dB = equal (ratio = 1)**

---

## 4. Why does SDR world love dB?

* Signals span **100+ dB range** (weak GPS signals vs strong FM broadcast).
* Noise levels, signal strengths, antenna gains, FFT plots → all easier to see/log on dB scale.
* Without dB, your spectrum would just look like a **flat noisy mess**.

---

## 5. Tiny thought experiment 🧠

* Suppose your FFT bin magnitude is **0.001**.
* In raw linear scale: meh, it’s “0.001”.
* In dB scale:

  $$
  20 \cdot \log_{10}(0.001) = -60 \, \text{dB}
  $$
* Now you instantly know: “that’s 60 dB weaker than my reference” → clear, human-readable.

---

✅ **So the expert summary**:

* Use **10·log10** for power ratios.
* Use **20·log10** for amplitude/voltage (FFT magnitudes, I/Q samples).
* That’s why `20 * log10(abs(fft))` is the universal way to plot SDR spectrums.

