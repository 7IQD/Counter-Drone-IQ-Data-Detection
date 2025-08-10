Compute the 4‑point DFT of the time‑domain sequence

$$
x[n] = [\,1,\;2,\;3,\;4\,],\quad n = 0,1,2,3
$$

—but **do it with the FFT method** (divide & conquer).

---

## 2. Step 1: Split Signal into Even and Odd Samples

We introduce `n` here to index time samples.

* **Even indices** (`n = 0,2`):

  $$
  x_{\rm even}[m] = x[2m],\quad m=0,1  
  \quad\Longrightarrow\quad [\,x[0],\,x[2]\,] = [\,1,\,3\,]
  $$
* **Odd indices** (`n = 1,3`):

  $$
  x_{\rm odd}[m] = x[2m+1],\quad m=0,1  
  \quad\Longrightarrow\quad [\,x[1],\,x[3]\,] = [\,2,\,4\,]
  $$

> 🔍 Here, `n` has been re‑parametrized into a **new index** `m` (runs 0→1) for each half.

---

## 3. Step 2: Compute 2‑Point DFTs of Each Half

Now we compute the **base‑case DFTs** of length‑2 directly, using `m`:

### 3.1 Even half DFT

$$
E[k] = \sum_{m=0}^{1} x_{\rm even}[m] \,e^{-j\frac{2\pi}{2}km}
\quad\text{for }k=0,1
$$

* For $k=0$:
  $\;E[0]=x_{\rm even}[0]+x_{\rm even}[1]=1+3=4$
* For $k=1$:
  $\;E[1]=x_{\rm even}[0]-x_{\rm even}[1]=1-3=-2$

### 3.2 Odd half DFT

$$
O[k] = \sum_{m=0}^{1} x_{\rm odd}[m] \,e^{-j\frac{2\pi}{2}km}
\quad\text{for }k=0,1
$$

* For $k=0$:
  $\;O[0]=2+4=6$
* For $k=1$:
  $\;O[1]=2-4=-2$

> 🔍 **Notice:** after this step, all sums over **time indices** (`m`) are done, and we have two small DFT results: **E\[·]** and **O\[·]**.

---

## 4. Step 3: Combine via the FFT “Twiddle” Rule

Now we switch to the **frequency index** `k`—we no longer refer to `n` or `m`. We use:

$$
W_4^k = e^{-j\frac{2\pi}{4}k}
$$

$$
X[k] = E[k] + W_4^k \,O[k], \quad
X[k+2] = E[k] - W_4^k \,O[k]
$$

for $k=0,1$.

* **Twiddle factors**:
  $W_4^0 = 1,\; W_4^1 = e^{-j\pi/2} = -j$.

### 4.1 For $k=0$:

$$
X[0] = E[0] + 1\cdot O[0] = 4 + 6 = 10 \\
X[2] = E[0] - 1\cdot O[0] = 4 - 6 = -2
$$

### 4.2 For $k=1$:

$$
X[1] = E[1] + (-j)\,O[1] = (-2) + (-j)(-2) = -2 + 2j \\
X[3] = E[1] - (-j)\,O[1] = (-2) - (-j)(-2) = -2 - 2j
$$

> 🔍 **Key Point:** here **only** `k` appears—**no** `n` or `m`. They’ve done their work in Step 2.

---

## 5. Final Result

$$
\boxed{X = [\,10,\;-2 + 2j,\;-2,\;-2 - 2j\,]}
$$

---

## 6. The “Disappearance” of `n` (and `m`)

1. **DFT step (time sums)** uses `n` (or `m` after splitting).
2. **FFT combine step** uses only `k`, because you are now working **purely in the frequency domain**, merging **already‑computed** partial results.
3. Once you’ve “summed over time” to get **E\[k]** and **O\[k]**, you **never need** to revisit `n` or `m`.

---

### ✅ Teaching Takeaway

* **Use `n`** when you’re summing over time samples to get any DFT.
* **Once that’s done**, you enter the FFT’s **merge phase**—only the frequency bin index `k` matters.
* This clean separation is what makes FFT both **correct** (it computes the DFT) and **efficient** (it reuses partial results without re‑summing time samples).

