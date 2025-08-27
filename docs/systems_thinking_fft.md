# 🌱 Systems Thinking in DSP with Python

This chapter is a journey into understanding **FFT and DSP concepts** through the lens of **Systems Thinking** (inspired by Peter Senge’s archetypes).
Each exercise is structured with **steps, reflection, and system loop** to help you see both the **technical skill** and the **mental model** behind it.

---

## 🌱 Stage 1: Build the Mental Map

### Exercise 1 – FFT as a Mirror

**Steps**

1. Take one IQ file.
2. Compute FFT (`np.fft.fft`) and plot spectrum.
3. Change sampling frequency `fs` (e.g. `1e6 → 2e6`).

**Reflection**

* How does the x-axis (frequency scale) stretch or compress?
* Does the signal itself move, or only the axis?

**System Loop Learned**
*"The world doesn’t change, only the lens does."*
👉 Like Senge’s **Shifting the Burden**: sometimes we change the **representation**, not the **reality**.

---

## 🌱 Stage 2: Causality in Amplitude

### Exercise 2 – Scaling the Input

**Steps**

1. Multiply IQ samples by 2 before FFT.
2. Compare power spectrum with the original.

**Reflection**

* Did the peaks shift position?
* Did their height change? By how much in dB?

**System Loop Learned**
*"Energy in time → energy in frequency."*
👉 Like **Limits to Growth**: more input, more output — but only vertically (magnitude), not position.

---

## 🌱 Stage 3: Sensitivity to Phase

### Exercise 3 – Add Phase Shift

**Steps**

1. Multiply IQ samples by `np.exp(1j*np.pi/4)`.
2. Plot spectrum vs. original.

**Reflection**

* Does spectrum shape change?
* Why does the power spectrum remain the same?

**System Loop Learned**
*"Phase is hidden in power view."*
👉 Like **Fixes that Fail**: you think you changed something, but the effect hides elsewhere (phase vs. magnitude).

---

## 🌱 Stage 4: Windows as Archetypes

### Exercise 4 – Windowing

**Steps**

1. Apply a Hamming window before FFT.
2. Compare with no window.

**Reflection**

* Why do sidelobes reduce?
* Why does the main peak widen?

**System Loop Learned**
*"Reducing noise costs resolution."*
👉 Classic **Tragedy of the Commons**: gain on one side, loss on another.

---

## 🌱 Stage 5: System Comparison

### Exercise 5 – Compare Two Files

**Steps**

1. Plot spectrum of two different IQ files on the same axis.
2. Try to identify where they differ.

**Reflection**

* Which differences are due to the signals themselves, and which are due to scaling/fs?
* Can you separate “signal property” from “system lens”?

**System Loop Learned**
*"Reality is a mix of structure + perspective."*
👉 Like **Mental Models**: two observers, same reality, different interpretations.

---
