## **📖 Headfirst DSP: The Power of $e^{j 2\pi f_m t}$ — with Time!**
---
### **1. First, the idea**

You already know that

$$
e^{j\theta} = \cos(\theta) + j\sin(\theta)
$$

is just a point moving around the **unit circle** in the complex plane.

When we say:

$$
e^{j 2\pi f_m \frac{n}{f_s}}
$$

we’re saying:

* **Spin around the circle** at a rate $f_m$ (mixer frequency)
* **Take discrete steps** based on $n$ (sample index)
* Each step is **$\frac{1}{f_s}$ seconds apart** (sampling frequency)
* So the **angle at sample $n$** is:

  $$
  \theta_n = 2\pi f_m \cdot \frac{n}{f_s}
  $$

---

### **2. Timing element explained visually**

Think of a **clock**:

* $f_s$ = how many ticks per second you get (sampling rate)
* $n$ = which tick we’re at (sample number)
* $\frac{n}{f_s}$ = **time since start** (in seconds)

So:

* At $n = 0$ → $t = 0$ sec → start at phase 0°
* At $n = 1$ → $t = \frac{1}{f_s}$ sec → phase moves forward
* At $n = 2$ → $t = \frac{2}{f_s}$ sec → phase moves further
* And so on.

---

### **3. Example: see the numbers**

Let’s take:

* Mixer frequency $f_m = 1000$ Hz
* Sampling rate $f_s = 8000$ Hz
* Samples $n = 0, 1, 2, 3$

Then:

$$
t_n = \frac{n}{f_s}
$$

and

$$
\theta_n = 2\pi f_m t_n
$$

| n | t (sec)  | θ (radians)   | cos(θ) | sin(θ) | Complex value   |
| - | -------- | ------------- | ------ | ------ | --------------- |
| 0 | 0.0000   | 0.0000        | 1.000  | 0.000  | $1.000+0.000j$  |
| 1 | 0.000125 | 0.7854 (45°)  | 0.707  | 0.707  | $0.707+0.707j$  |
| 2 | 0.000250 | 1.5708 (90°)  | 0.000  | 1.000  | $0.000+1.000j$  |
| 3 | 0.000375 | 2.3562 (135°) | -0.707 | 0.707  | $-0.707+0.707j$ |

---

### **4. What’s the “rotation” really?**

* The **rotation per sample** in radians is:

$$
\Delta\theta = \frac{2\pi f_m}{f_s}
$$

* This is how much the phasor moves **each time you take a sample**.
* More $f_m$ → spins faster
* More $f_s$ → spins slower (because you’re taking smaller time steps)

---

### **5. Big picture — why you care**

* **Mixing**: Multiplying your signal by this complex exponential shifts its frequency up or down
* **Filtering**: Often done after mixing to isolate what you want
* **Signal scaling**: Controlled by amplitude, phase rotation rate controlled by $f_m$

---

💡 **Memory trick**:
Think of $f_s$ as **“frames per second”** in a movie, $n$ as the **frame number**, and $f_m$ as **how fast the character spins**. The formula just tells you where the character is facing in each frame.

---

