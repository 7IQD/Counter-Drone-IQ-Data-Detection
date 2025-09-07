# 🎯 Counter-Drone DSP Journey — Milestone Map

## **Stage 1: DSP Foundations (Month 1–3)**

Goal: Build confidence with signals, filters, and frequency response.

* ✅ **Milestone 1** (Month 1):

  * Implement & understand **Low-Pass FIR filter** (we’re already here!).
  * Be able to explain `firwin`, `freqz`, `np.abs(H)` in your own words.

* ✅ **Milestone 2** (Month 2):

  * Design **High-Pass, Band-Pass, Notch filters**.
  * Interpret plots (linear vs dB).
  * Save + organize results in repo (your lab book grows!).

* ✅ **Milestone 3** (Month 3):

  * Work with a **recorded audio IQ file** (e.g., FM radio).
  * Apply your filters to real data → hear/see effect.
  * First taste of “real IQ processing.”

---

## **Stage 2: Practical IQ Handling (Month 4–6)**

Goal: Comfort with IQ files (the heart of SDR and drones).

* ✅ **Milestone 4** (Month 4):

  * Load an **IQ dataset** (public FM, ADS-B, Wi-Fi captures).
  * Plot **constellation, spectrogram**.
  * Begin to “see” signals, not just numbers.

* ✅ **Milestone 5** (Month 5):

  * Practice **decimation, resampling, filtering** on IQ.
  * Be able to zoom into a signal within a wider band.

* ✅ **Milestone 6** (Month 6):

  * Detect a known **signal presence** (FM carrier, ADS-B pulse) in IQ.
  * First step towards “detection” — core to counter-drone.

---

## **Stage 3: Drone-Specific Exploration (Month 7–9)**

Goal: Apply DSP to signals relevant for drones.

* ✅ **Milestone 7** (Month 7):

  * Study drone communication bands (2.4 GHz, 5.8 GHz, GPS).
  * Collect or use shared IQ samples around these frequencies.

* ✅ **Milestone 8** (Month 8):

  * Implement **energy detection / spectrogram scan**.
  * Be able to “see” when a drone transmitter is ON vs OFF in IQ data.

* ✅ **Milestone 9** (Month 9):

  * Separate **drone control vs noise** using filters + detection.
  * First mini “counter-drone prototype” in lab environment.

---

## **Stage 4: Applied Counter-Drone (Month 10–12)**

Goal: Move from playing with data → structured detection methods.

* ✅ **Milestone 10** (Month 10):

  * Implement simple **signal classification** (e.g., “is this drone Wi-Fi or not?”).
  * Work with features: bandwidth, symbol rate, spectral shape.

* ✅ **Milestone 11** (Month 11):

  * Try out **direction finding basics** (theory + simulation with 2 antennas).
  * Start thinking not just “is there a drone?” but “where is it?”

* ✅ **Milestone 12** (Month 12):

  * Package results into a **small report or GitHub showcase**.
  * This becomes your **first visible proof** of capability.

---

## **Stage 5: Specialization (Month 12–18)**

Goal: Choose focus — stay defensive (counter-drone detection/jamming) or prepare offensive (own drone comms).

* ✅ **Milestone 13** (Month 13–15):

  * Defensive: implement **robust detection (machine learning, SDR automation)**.
  * Offensive: experiment with **your own drone SDR link**.

* ✅ **Milestone 14** (Month 16–18):

  * Defensive: simulate **jamming / GPS spoof detection** in IQ.
  * Offensive: test **resilient comms / FHSS ideas**.

At this stage → you are not a “student learning filters” anymore. You’re someone who can **demonstrate applied counter-drone DSP**.

---

# ⚖️ Reality Check

* By **Month 3** → you’ll have strong DSP basics + first hands-on IQ work.
* By **Month 6** → you’ll be processing real-world signals (huge boost!).
* By **Month 12** → you’ll have a mini working counter-drone detection prototype.
* By **Month 18** → you’ll be able to show **original work** in defensive/offensive comms.

---
