Here's a **well-organized reference table** of commonly used **discrete-time filters** — especially useful for DSP and SDR applications — with their:

* **Type & Impulse Response (`h[n]`)**
* **Purpose**
* **Physical Interpretation**
* **Key Use Cases / Notes**

---

## 📘 Practical Filters Reference Table (for DSP/SDR)

| Type of Filter         | Impulse Response `h[n]`                       | Purpose                           | Interpretation                                           | Notes / Use Case                                                |
| ---------------------- | --------------------------------------------- | --------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------- |
| **Moving Average**     | `[1/N, 1/N, ..., 1/N]` (length N)             | Smoothing / noise reduction       | Averages local values to reduce random fluctuations      | Low-pass filter; reduces high-frequency noise in IQ signals     |
| **First Difference**   | `[1, -1]`                                     | Change detection                  | Outputs slope between adjacent points                    | Edge detection, start of signal burst, FM demodulation          |
| **Second Difference**  | `[1, -2, 1]`                                  | Curvature detection               | Measures rate of change of slope                         | Detects inflection points or fast changes; useful in BPSK demod |
| **Echo Filter**        | `[1, 0, 0.5]`                                 | Simulate multipath / echoes       | Adds delayed version of signal                           | Models wireless reflections or reverberation                    |
| **Spike Detector**     | `[-1, 2, -1]`                                 | Peak emphasis                     | Highlights central peaks over neighbors                  | Used in transient or attack detection (e.g. radar, sonar)       |
| **Matched Filter**     | Time-reversed known sequence                  | Signal detection                  | Maximizes SNR for that pattern                           | Used in packet/preamble detection in SDRs                       |
| **Sinc Filter**        | `sinc()` (windowed)                           | Ideal low-pass filter             | Preserves slow-varying trends; removes fast ones         | Basis of anti-aliasing filters, resampling IQ data              |
| **Gaussian Filter**    | Discrete Gaussian (e.g., `[0.25, 0.5, 0.25]`) | Gentle smoothing                  | Smooths without harsh cutoffs                            | Better than moving average for preserving shape                 |
| **High-Pass Filter**   | `[1, -2, 1]`, or `[-1, 1]`                    | Isolate sharp variations          | Removes slow background changes                          | Detects fast signal transitions (used in envelope removal)      |
| **Band-Pass Filter**   | Derived from difference of low-pass filters   | Keep signal in certain freq range | Keeps modulated carrier, removes baseband or out-of-band | Used in demodulators, channel extraction                        |
| **Integrator**         | `[1, 1, 1, ..., 1]` (cumulative sum)          | Energy accumulation               | Summed energy over time                                  | Used in power detection, moving average of amplitude            |
| **Differentiator**     | `[1, -1]`, or `[0.5, 0, -0.5]` (central diff) | Detect rate of change             | Tracks signal slope                                      | Basis for phase/frequency tracking in SDRs                      |
| **Impulse (Identity)** | `[1, 0, 0, ...]`                              | No filtering                      | Pass-through (reference)                                 | Used to validate convolution system behavior                    |
| **Delta Comb**         | `[1, 0, 0, 1, 0, 0, 1, ...]`                  | Sub-sampling / echo-like response | Regular echoes                                           | Used in modeling pulse trains or sampling effects               |

---

## 🧠 Bonus: How to Design or Recognize a Filter

| Feature        | What to Look For                                                |
| -------------- | --------------------------------------------------------------- |
| **Smoothing**  | Positive taps summing to 1, centered                            |
| **High-pass**  | Positive and negative taps, sum = 0                             |
| **Matched**    | Reverse of known pattern (maximize correlation)                 |
| **Symmetry**   | Linear phase; non-distorting                                    |
| **Decay**      | Echo or reverberation                                           |
| **Spike-like** | Central large value with flanking negatives (second derivative) |

---

## 🎯 Relevance to Your SDR Standards Project

When handling IQ data:

* You'll need to **simulate channel effects** → use echo, multipath filters.
* For **pre/post-processing**: smooth noise (`moving average`), detect modulation changes (`difference filters`), extract carriers (`band-pass`).
* When testing compliance → use **matched filters** to detect known signal structures.
