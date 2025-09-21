# 🧪 Complete Lab: RRC Filter Design & Analysis

*(focus: β = roll-off, span = duration, sps = samples per symbol)*

---

## **Part 1 – Time Domain Pulse Shape vs β**

**Goal:** See how roll-off changes pulse width.

* **Setup:** span = 12, sps = 32, β = \[0.1, 0.25, 0.5].
* **Do:** generate one RRC pulse for each β.
* **Plot:** overlay them in time.
* **Measure:** main lobe width, tail length.
* **Rule:** higher β → wider pulse, faster decay.

---

## **Part 2 – Truncation Effect (span)**

**Goal:** See how span (filter length) affects tails.

* **Setup:** β = 0.25, sps = 32, span = \[4, 8, 12].
* **Do:** generate pulses, compare with reference span=20.
* **Plot:** overlay, zoom on tails.
* **Measure:** % energy lost.
* **Rule:** larger span = less truncation loss.

---

## **Part 3 – Frequency Response vs β**

**Goal:** See bandwidth expansion with β.

* **Setup:** span = 12, sps = 32, β = \[0.1, 0.25, 0.5].
* **Do:** compute FFT (Nfft = 4096).
* **Plot:** magnitude vs normalized frequency.
* **Measure:** bandwidth at −3 dB.
* **Rule:** higher β = wider spectrum, but gentler roll-off.

---

## **Part 4 – Frequency Response vs span**

**Goal:** See sidelobe distortion from short spans.

* **Setup:** β = 0.25, sps = 32, span = \[4, 8, 12].
* **Do:** FFT for each.
* **Plot:** overlay.
* **Measure:** sidelobe height.
* **Rule:** short span = higher sidelobes (bad stopband).

---

## **Part 5 – Single Symbol Sampling**

**Goal:** Confirm RRC gives correct value at symbol instant.

* **Setup:** one QPSK symbol = 1+0j, span = 12, β = 0.25.
* **Do:** upsample, filter, compensate for delay.
* **Plot:** waveform with sampling instant marked.
* **Measure:** sample vs original symbol.
* **Rule:** error ≈ 0.

---

## **Part 6 – Multi-Symbol ISI Check**

**Goal:** See eye diagram, verify no ISI.

* **Setup:** 10 random QPSK symbols, span = 12, β = 0.25.
* **Do:** upsample, filter.
* **Plot:**

  * waveform in time,
  * eye diagram overlayed.
* **Measure:** sample error at symbol centers.
* **Rule:** ISI < −40 dB (essentially zero).

---

## **Part 7 – β × span Grid Study**

**Goal:** Quantify tradeoffs.

* **Setup:** β ∈ \[0.1, 0.25, 0.5], span ∈ \[4, 8, 12].
* **Do:** generate filter, compute metrics:

  * bandwidth (−3 dB),
  * sidelobe level,
  * tail energy loss.
* **Output:** results table.
* **Rule:** low β saves bandwidth but needs longer span.

---

## **Part 8 – Optional Noise Test (end-to-end)**

**Goal:** See effect on BER.

* **Setup:**

  * Random QPSK stream, 1000 symbols,
  * β = 0.25, span = 8,
  * AWGN at SNR = \[0, 5, 10, 15] dB.
* **Do:** Tx → RRC → noise → matched filter → Rx.
* **Plot:** BER vs SNR curve.
* **Rule:** matched filter recovers original symbols; BER follows QPSK theory.

---

