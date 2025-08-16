# 📖 **Chapter 2.1 - Your Signal’s “Passport”**

A signal is like a traveler — to let it into your DSP world, you’ve got to stamp its passport with some key details.

---

## 1️⃣ **Duration (T)** → *How long you watch it*

**Question:** How many seconds (or milliseconds, microseconds) are you recording or generating the signal?

* Think of it like the *length of the movie* you’re shooting.
* If you stop recording early, you miss the story.
* If you record too long, you’ll have a longer file, more samples, and better frequency resolution — but bigger processing costs.

💡 **Example:**

```
T = 1 second   →  short snapshot
T = 5 seconds  →  longer snapshot, more data to work with
```

---

## 2️⃣ **Sampling Rate (Fs)** → *How often you take pictures*

**Question:** How many times per second do you capture the signal’s value?

* Units: **Hertz (Hz)** = samples per second.
* The faster you sample, the more detail you capture — *but* there’s a law you must obey:

**Nyquist theorem:**
You can only capture frequencies up to

$$
F_{\text{max}} = \frac{F_s}{2}
$$

💡 **Example:**
If Fs = 8 Hz → Max detectable frequency = 4 Hz.

---

## 3️⃣ **Number of Samples (N)** → *How many pictures you end up with*

**Relation:**

$$
N = F_s \times T
$$

* This is just *how many data points* you have.
* **FFT eats N for breakfast** — because it decides how many *frequency bins* you get.
* More samples = finer frequency resolution.

💡 **Example:**
If Fs = 8 Hz, T = 1 s → N = 8 samples.

---

## 4️⃣ **Signal Frequency (f₀)** → *The “beat” you put in*

* This is the actual “note” or tone in the signal you’re generating.
* If you generate a sine wave at 2 Hz, it makes 2 complete cycles per second.

---

## 5️⃣ **Amplitude (A)** → *How tall the wave is*

* Bigger amplitude = higher peaks and deeper troughs.
* This doesn’t change the frequency — only the size of the wave.

---

## 6️⃣ **Phase (φ)** → *Where the wave starts*

* Two sine waves with the same frequency and amplitude but different phase look like one is shifted sideways.
* Units: degrees (°) or radians.

💡 **Example:**
φ = 0° → starts at the center going up.
φ = 90° → starts at the top.

---

## 7️⃣ **Frequency Resolution (Δf)** → *How far apart your FFT “bin” notes are*

Relation:

$$
\Delta f = \frac{F_s}{N} = \frac{1}{T}
$$

* The longer you observe (bigger T), the **smaller** Δf — you can distinguish closer frequencies.
* Short observation → coarser frequency bins.

💡 **Example:**
N = 8, Fs = 8 → Δf = 1 Hz.
You can only get 0 Hz, 1 Hz, 2 Hz … up to 4 Hz.

---

## 8️⃣ **Nyquist Limit** → *The tallest note you can hear without distortion*

$$
F_{\text{Nyquist}} = \frac{F_s}{2}
$$

* If you put a 5 Hz signal into an 8 Hz sampler, it will “pretend” to be 3 Hz — this is aliasing.

---

# 🎯 **Why this matters**

When you see:

> “A 1-second signal sampled at 8 Hz containing a 2 Hz sine wave”

You can immediately decode:

* **Duration (T)** = 1 s
* **Sampling Rate (Fs)** = 8 Hz → Nyquist limit = 4 Hz
* **Samples (N)** = 8
* **Resolution (Δf)** = 1 Hz
* **Frequency of wave (f₀)** = 2 Hz
* You’ll see a peak in FFT at bin index `2`.

---

# 🧠 **Head First Exercise**

1. Take **Fs = 10 Hz**, **T = 2 seconds**

   * What’s N?
   * What’s Δf?
   * What’s Nyquist limit?
2. Generate a sine wave of frequency 3 Hz with amplitude 2 and phase 90°.
3. Run FFT and identify the bin with the highest magnitude.
