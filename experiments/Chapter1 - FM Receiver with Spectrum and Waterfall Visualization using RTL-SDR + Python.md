# 📡 Practical Project Synopsis

**Title:** *FM Receiver with Spectrum and Waterfall Visualization using RTL-SDR + Python*
---
## 1. **Why this is Important**

* **Foundation Project:** FM reception is the “Hello World” of SDR — it forces you to understand IQ sampling, tuning, filtering, demodulation, and visualization.
* **Defence/Research Relevance:** The same concepts used in FM reception (tuning, demodulation, FFT, visualization) are *directly applicable* in spectrum monitoring, signal intelligence (SIGINT), and communication validation.
* **Visible Output:** A working FM receiver with live spectrum/waterfall plots is *impressive and tangible*. Anyone can see/hear the result → instant credibility.
---
## 2. **Reason for Selecting This**

* It’s a **complete pipeline project**: from raw IQ samples → DSP processing → audio playback + plots.
* Uses **low-cost hardware (RTL-SDR)** that is widely available.
* Teaches all the **core DSP/SDR building blocks**:

  * Sampling & IQ data
  * FFT-based spectrum analysis
  * Filtering & demodulation
  * Visualization (time-domain, frequency-domain, waterfall)

👉 It’s not toy work — it’s a practical stepping stone toward more advanced defence-related SDR tools (e.g., spectrum scanners, drone signal detection).
---
## 3. **What We Will Achieve**

1. **FM Receiver** that tunes to a local broadcast frequency and plays audio.
2. **Real-time Spectrum Plot** (FFT vs frequency).
3. **Waterfall Plot** showing signal energy over time.
4. A **modular Python script** where each DSP block (tuner, filter, demodulator, plotter) is clearly coded and can be reused in future projects.
5. **Documented GitHub repo + short write-up**, making this your first public portfolio item.
---
## 4. **Pre-Requisites**

### 🔹 Hardware

* **RTL-SDR dongle** (cheap, USB plug-in SDR receiver).
* Laptop/PC with USB and Python environment.
* Simple antenna (stock whip or dipole).

### 🔹 Software

* **Python 3.9+**
* Required Python libraries:

  * `numpy` (numerical DSP operations)
  * `scipy` (signal processing filters, resampling)
  * `matplotlib` (plotting FFT + waterfall)
  * `rtlsdr` (Python bindings for RTL-SDR)
  * `sounddevice` (to play demodulated audio)
  * *(optional)* `pyqtgraph` (for fast waterfall plots)

👉 Installation via pip:

```bash
pip install numpy scipy matplotlib pyrtlsdr sounddevice pyqtgraph
```

---

## 5. **Python Skills Needed**

* **Functions & def calls:** for modular DSP blocks (e.g., `def demodulate_fm(iq_samples):`)
* **Numpy:** array operations, FFT (`np.fft.fft`), absolute value for spectrum.
* **Matplotlib:** `plt.plot()` for spectrum, `imshow()` for waterfall.
* **Scipy.signal:** filters (`butter`, `lfilter`, `decimate`).
* **Sounddevice:** `sd.play()` for audio playback.

👉 You don’t need advanced OOP — just functional programming + clear structuring.

---

## 6. **Interlinking of Blocks (DSP Chain)**

Here’s how the pipeline fits together:

```
[RTL-SDR Source] 
      ↓
 [IQ Samples (complex)] 
      ↓
 [Tuner → shifts frequency to baseband] 
      ↓
 [Bandpass Filter → isolate FM channel] 
      ↓
 [FM Demodulator → extract audio from IQ] 
      ↓
 [Low-pass Filter + Decimation → audio bandwidth (0–15 kHz)] 
      ↓
 [Audio Output → speaker (sounddevice)] 
      ↓
 [FFT Analysis → spectrum plot] 
      ↓
 [Waterfall Visualization → time vs frequency vs power]
```
👉 This modular chain means you’ll later be able to swap **FM demodulator** with, say, a **drone telemetry decoder** or a **signal classifier**.

---

## 7. **Expected Outputs**

* **Real-time spectrum plot:** showing peaks at FM stations.
* **Waterfall plot:** colorful “heatmap” of signal energy over time.
* **Audio playback:** local FM radio station decoded.
* **Codebase:** well-documented Python script with modular DSP functions.
* **README + screenshots:** uploaded to GitHub as your **first portfolio project.**


