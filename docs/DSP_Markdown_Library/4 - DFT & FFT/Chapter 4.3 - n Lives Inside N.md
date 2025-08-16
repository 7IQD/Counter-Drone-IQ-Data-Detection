## 📖 Chapter: *n Lives Inside N — The Real Connection Between n, N, and $f_s$*

---

### 🎬 Act 1 — The Big Block of Samples

Imagine you’ve just captured **N digital samples** from your IQ data stream.
This block is *exactly* what the FFT will chew on.

* $N$ = **total number of samples in the block**.
* $n$ = **which sample we’re talking about inside that block**.

So if $N = 1024$:

* $n = 0$ → first sample in the block
* $n = 512$ → middle sample
* $n = 1023$ → last sample

---

### 🎯 Act 2 — n Has No Meaning Without N

In the DFT formula:

$$
X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j \frac{2\pi}{N} nk}
$$

* The **upper limit** $N-1$ tells us how many values $n$ can take.
* **n exists only from 0 up to N-1** — because this **N** defines the FFT’s “analysis window.”
* If you change $N$, you change the range of n.
* This means **n’s life span is tied to N** — it’s part of N’s definition.

---

### ⏱ Act 3 — Where $f_s$ Comes In

Outside the math world, your SDR is sampling at $f_s$ samples/sec.

* Each **gap** between two $n$ positions in the block is $\Delta t = 1 / f_s$ seconds.
* The **time stamp** for a given $n$ in the block is:

$$
t_n = \frac{n}{f_s}
$$

* $f_s$ does **not** decide how many samples are in the block (that’s N),
  but it **does** decide how far apart those N samples are in real time.

---

### 🎵 Act 4 — Why N and n Matter for Frequency

The FFT uses **N** and $f_s$ together to set your frequency resolution:

$$
\Delta f = \frac{f_s}{N}
$$

* Bigger $N$ → smaller $\Delta f$ (better frequency resolution)
* Smaller $N$ → larger $\Delta f$ (coarser frequency resolution)

Here’s the key chain:

1. **Choose N** → defines how many n’s you have (0 to N-1)
2. $n$ indexes the samples in that N-block
3. $f_s$ tells you how those n’s map to actual time
4. Together, $N$ and $f_s$ give you your FFT frequency spacing

---

### 💡 Brain Hook

Think of $N$ as a *row of seats in a theater*, and $n$ as *seat numbers*:

* If the theater has $N = 8$ seats, seat numbers go from $n = 0$ to $n = 7$.
* If you build a bigger theater ($N = 16$), you now have seat numbers $n = 0$ to $n = 15$.
* The **distance** between seats is set by $f_s$ in time (seconds apart).

---

### 🧩 Recap Table

| Symbol     | Meaning                           | Tied To                |
| ---------- | --------------------------------- | ---------------------- |
| $N$        | Number of samples in FFT block    | Your processing choice |
| $n$        | Position of a sample in the block | Always 0 to N-1        |
| $f_s$      | Samples per second                | Hardware/sample rate   |
| $\Delta t$ | Time between samples = $1/f_s$    | From $f_s$             |
| $\Delta f$ | Frequency bin width = $f_s/N$     | From $f_s$ & N         |

---

Now the link is **explicit**:

* $n$ lives **inside** $N$ — it is meaningless without knowing N.
* $N$ is the “container,” $n$ is the “slot number” in that container.
* $f_s$ turns those slot numbers into real-world time and frequency.

---
