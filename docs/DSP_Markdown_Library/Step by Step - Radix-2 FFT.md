**Input signal**:
Let’s say we have 8 real samples:

$$
x = [x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7]
$$

---

## 🧠 Step-by-Step Breakdown (Radix-2 FFT)

### 🟨 Step 1: Divide the signal into even and odd indices:

* **Even samples**: $x_0, x_2, x_4, x_6$
* **Odd samples**: $x_1, x_3, x_5, x_7$

---

### 🟨 Step 2: Recursively divide again:

Now recursively split even and odd:

* Evens of evens: $x_0, x_4$
* Odds of evens: $x_2, x_6$
* Evens of odds: $x_1, x_5$
* Odds of odds: $x_3, x_7$

Now each of these subgroups has **2 elements**, so you apply:

$$
X[0] = a + b, \quad X[1] = a - b
$$

You now have **DFTs of size 2** computed for each subgroup:

* $X_{\text{even even}}$: from $x_0, x_4$
* $X_{\text{even odd}}$: from $x_2, x_6$
* $X_{\text{odd even}}$: from $x_1, x_5$
* $X_{\text{odd odd}}$: from $x_3, x_7$

---

### 🟦 Step 3: Combine results bottom-up using Twiddle Factors

Let’s move upward one level:
Now combine the results of the two sub-DFTs (of size 2) into a DFT of size 4.

#### For the even half:

You combine:

* $X_{\text{even}}[k] = X_{\text{even even}}[k] + W_4^k \cdot X_{\text{even odd}}[k]$
* $X_{\text{even}}[k+2] = X_{\text{even even}}[k] - W_4^k \cdot X_{\text{even odd}}[k]$

Where $k = 0,1$, and $W_4^k = e^{-j\frac{2\pi}{4}k}$

Similarly for the odd half:

* $X_{\text{odd}}[k] = X_{\text{odd even}}[k] + W_4^k \cdot X_{\text{odd odd}}[k]$
* $X_{\text{odd}}[k+2] = X_{\text{odd even}}[k] - W_4^k \cdot X_{\text{odd odd}}[k]$

---

### 🟥 Step 4: Final recombination (size 8 DFT from two 4-point DFTs)

Now combine full even and odd results:

$$
X[k] = X_{\text{even}}[k] + W_8^k \cdot X_{\text{odd}}[k] \\
X[k+4] = X_{\text{even}}[k] - W_8^k \cdot X_{\text{odd}}[k]
$$

Where $k = 0,1,2,3$, and $W_8^k = e^{-j\frac{2\pi}{8}k}$

---

## 🔁 Summary of What Happens After the Last Pair is Reached:

1. You **compute 2-point DFTs** at the bottom: $a+b$, $a-b$
2. Then **combine pairs of these 2-point results** into 4-point DFTs using twiddle factors
3. Then **combine those into 8-point DFTs** — again using twiddle factors
4. This **recursively assembles the full FFT output**: $X[0], X[1], \dots, X[7]$

---
## 📘 Analogy (Quick Intuition)

Think of FFT as:

* **Chopping a big problem into tiny problems**
* **Solving the tiny problems**
* **Merging them cleverly using twiddle factors** (which are like "phase shifts" that align results in frequency)
---
