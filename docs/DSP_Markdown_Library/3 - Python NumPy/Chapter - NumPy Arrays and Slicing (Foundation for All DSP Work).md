## **1. NumPy Arrays and Slicing (Foundation for All DSP Work)**

**Goal:** Comfortably manipulate signals in Python without confusion over shapes, indexing, or slicing.
**Mini-practicals:**

* Create 1D and 2D arrays (real & complex).
* Slice: `arr[start:stop:step]` for different patterns.
* View vs. copy behaviour (`arr[::2]` vs `.copy()`).
* Reshaping IQ streams: `(len(data)//2, 2)` to separate I and Q.
* Complex number creation: `I + 1j*Q`.

---

## **2. FFT with NumPy**

**Goal:** Move confidently between time and frequency domain.
**Mini-practicals:**

* Use `np.fft.fft()` and `np.fft.fftfreq()` for a synthetic sine wave.
* Plot amplitude spectrum (linear and dB).
* Understand **bin spacing** (`fs/N`) and symmetry in FFT output.
* Work with `np.fft.fftshift()` for centered spectra.

---

## **3. Plotting IQ Data & Spectra (Matplotlib)**

**Goal:** See your signals clearly and interpret them.
**Mini-practicals:**

* Plot **time-domain I and Q** separately.
* Make a **constellation diagram** (scatter plot: I vs Q).
* Plot **spectrum** from FFT (frequency vs. magnitude).
* Use subplots to compare time vs frequency domain.

---

## **4. Simple DSP Tasks**

**Goal:** Apply basic processing steps that almost every SDR task needs.
**Mini-practicals:**

* Windowing: multiply by Hamming, Hann, or Blackman window.
* Low-pass filtering with `scipy.signal.firwin()` + `lfilter()`.
* Decimation (`signal.decimate`) for bandwidth reduction.
* Simple AM/FM demod in Python from synthetic IQ data.

---

## **5. SDR-Specific Scripts**

**Goal:** Read actual IQ recordings and visualize them like a spectrum analyzer.
**Mini-practicals:**

* Read `.bin` IQ file (interleaved float32 or int16).
* Reshape to complex array (`I + 1j*Q`).
* Plot time-domain, spectrum, and constellation.
* Try live visualization from RTL-SDR (using `pyrtlsdr` or `rtl_sdr` CLI → pipe to Python).

---

✅ **Sequence to Learn:**
NumPy arrays/slicing → FFT basics → plotting IQ data → simple DSP tasks → SDR file/scripts.
This way, each skill directly supports the next, so you avoid "knowing in theory but stuck in practice" moments.

---
