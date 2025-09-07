# Filters - Plan

This folder contains scripts for applying and experimenting with **digital filters** on IQ data. The focus is on learning **time- and frequency-domain effects** of different filter types.

---

## Step 1 — Apply Filters (`apply_filter.py`)

1. Open `Filters/apply_filter.py`.
2. The script implements three filter types:

   - Low-pass filter
   - High-pass filter
   - Band-pass filter

3. For each filter:

   - Load `hello.iq` (IQ sample file)
   - Apply the selected filter
   - Plot **time-domain magnitude/phase** and **frequency spectrum**

---

## Step 2 — Filter Design

- Filters are implemented using **Butterworth filters** for simplicity.
- Key parameters:

  - `order` → controls filter steepness
  - `cutoff` → cutoff frequency (low, high, or band)

- Use `scipy.signal.butter` to generate filter coefficients.
- Apply the filter with `scipy.signal.filtfilt` for **zero-phase filtering**.

---

## Step 3 — Visualization

- Use **subplots** to compare:

  - Raw vs filtered IQ in **time domain**
  - Raw vs filtered IQ in **frequency domain**

- Save plots in the `plots/` folder for reference.

---

## Step 4 — Experiment

- Adjust filter orders and cutoff frequencies to see their effect.
- Observe how the **frequency spectrum changes** and which frequencies are suppressed or passed.
