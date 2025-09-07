# **Step 0: Understanding the Workflow - Filters**

We have **IQ data**:

* Stored in `hello.iq`
* Metadata in `.sigmf-meta` gives `fs` (sample rate) and `fc` (center frequency)

Our **goal**:

1. Apply digital filters (Butterworth) to IQ data
2. Observe effect in **time-domain** (magnitude & phase)
3. Observe effect in **frequency-domain** (spectrum)

---

# **Step 1: Digital Filter Basics**

### **1️⃣ Filter Coefficients**

When we do:

```python
b, a = butter(order, cutoff/(fs/2), btype='low')
```

* `butter()` **computes the coefficients** of a Butterworth filter

  * `b` → numerator coefficients (feedforward)
  * `a` → denominator coefficients (feedback)
* These coefficients define the **difference equation**:

$$
y[n] = b_0 x[n] + b_1 x[n-1] + \dots - a_1 y[n-1] - a_2 y[n-2] - \dots
$$

* This equation tells the filter **how to combine past inputs and outputs** to produce the current output.

---

### **2️⃣ Applying the Filter**

Two common methods:

1. **`lfilter(b, a, x)`**

   * Applies the filter **forward in time only**
   * Introduces **phase shift** (signal is delayed)

2. **`filtfilt(b, a, x)`**

   * Applies the filter **forward and backward**
   * Cancels phase distortion
   * Useful when you want **phase-preserving filtering**, common in IQ processing

So in practice:

```python
from scipy.signal import lfilter, filtfilt

# Forward-only filter (phase shifted)
y1 = lfilter(b, a, iq_data)

# Zero-phase filter
y2 = filtfilt(b, a, iq_data)
```

We usually prefer `filtfilt` for **analysis purposes**, so magnitude & phase plots are not distorted.

---

### **3️⃣ Normalization**

* Cutoff frequency in `butter` is **normalized to Nyquist frequency**:

$$
f_{normalized} = \frac{f_{cutoff}}{f_s/2}
$$

* Ensures filter works correctly regardless of sample rate.

---

# **Step 2: IQ Data Considerations**

* IQ data: `dtype=complex64` → **I + jQ**
* Filter **both I and Q together** (complex array)
* After filtering, we can:

  * Plot **magnitude**: `np.abs(filtered_iq)`
  * Plot **phase**: `np.angle(filtered_iq)`
  * Plot **spectrum**: FFT of filtered signal

---

# **Step 3: Reading `.sigmf-meta` every time**

* `.sigmf-meta` contains **essential info**:

  * Sample rate (`core:sample_rate`)
  * Center frequency (`core:center_freq`)
* Reading it each time ensures the **script adapts automatically** if you change the IQ file.
* Example:

```python
with open("hello.sigmf-meta") as f:
    meta = json.load(f)

fs = meta["global"]["core:sample_rate"]
fc = meta["global"]["core:center_freq"]
```

* Now you can design **any filter** correctly based on the actual sampling rate.

---

✅ Once you are comfortable with these basics, we can write **a single, clean `apply_filter.py`**:

1. Reads IQ and metadata
2. Designs Butterworth filter (any type)
3. Applies `filtfilt`
4. Plots **time-domain magnitude/phase** and **frequency-domain spectrum**

---
