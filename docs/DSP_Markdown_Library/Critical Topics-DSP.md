
### 🔁 TOPICS 

#### **1. Windowing and Spectral Leakage**

* Why it’s needed before FFT
* Common windows: Hamming, Hanning, Blackman
* Effect on frequency resolution and leakage

#### **2. Filtering in Frequency and Time Domains**

* FIR vs IIR filters
* Design using Python (`scipy.signal.firwin`, `butter`, `lfilter`)
* Understanding poles, zeros, and frequency response
* Practical: Build a bandpass filter and apply to signal

#### **3. Sampling Theorem and Aliasing**

* Nyquist rate
* Aliasing and how to detect/fix it
* Practical resampling using `scipy.signal.resample`

#### **4. Z-Transform and System Stability**

* A generalization of the DTFT
* Region of convergence (ROC), causality
* Connection to filter design and stability

#### **5. Correlation and Cross-Correlation**

* Matched filtering, signal detection
* Auto-correlation vs cross-correlation
* Application to synchronization, timing, and pattern matching

#### **6. Power Spectral Density (PSD) and Spectrograms**

* Welch method, periodogram
* Visualizing time-varying spectra
* Practical with `matplotlib.specgram` or `scipy.signal.welch`

#### **7. Modulation and Demodulation (Analog + Digital)**

* AM, FM, BPSK, QPSK, etc.
* IQ representation of modulated signals
* Simulations using NumPy and SDR tools

#### **8. Real-Time DSP Concepts**

* Overlap-add / Overlap-save
* Block processing
* Latency and buffer management in SDR

---

### 🛠️ Suggested Python Practicals Alongside

| Concept     | Python Tool                                              |
| ----------- | -------------------------------------------------------- |
| Windowing   | `np.hamming`, `np.blackman`                              |
| Filtering   | `scipy.signal.firwin`, `lfilter`, `freqz`                |
| Spectrogram | `matplotlib.pyplot.specgram`, `scipy.signal.spectrogram` |
| Correlation | `np.correlate`, `scipy.signal.correlate`                 |
| Modulation  | Simulate AM/FM/BPSK using NumPy                          |
| PSD         | `scipy.signal.welch`, `matplotlib.mlab.psd`              |

---

### 🧠 Learning Strategy

* Alternate **conceptual topics** (like Z-transform) with **practical labs** (like filtering).
* Consolidate your understanding by **visualizing signals** before and after applying a technique.
* Use **Think DSP**, **PySDR**, and real RTL-SDR signals to practice each concept on actual IQ data.

---

Would you like me to build a **4-week learning plan** using these topics based on your current pace (e.g. 1–2 topics per week with practice)?
