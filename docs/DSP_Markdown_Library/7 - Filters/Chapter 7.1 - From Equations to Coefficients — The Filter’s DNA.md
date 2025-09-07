# **Chapter 7.1 : From Equations to Coefficients — The Filter’s DNA**

When you hear the word *filter*, you might imagine a coffee filter or a water filter — something that blocks the bad stuff and lets the good stuff pass.

A **digital filter** does the same thing, but instead of coffee grounds or dirt, it blocks *frequencies*.

Now, how do we *describe* such a filter in math?

It all starts with a difference equation:

$$
y[n] = b_0 x[n] + b_1 x[n-1] + b_2 x[n-2] + \dots - a_1 y[n-1] - a_2 y[n-2] - \dots
$$

This equation has two main parts:

1. **Feedforward path (the b’s)**

   * These multiply the *input signal* values (`x[n]`, `x[n-1]`, …).
   * They shape how the incoming signal contributes to the output.
   * Think of them as the *new ingredients you add today*.

2. **Feedback path (the a’s)**

   * These multiply the *previous output* values (`y[n-1]`, `y[n-2]`, …).
   * They “feed back” old outputs into the calculation.
   * Think of them as the *memory of past results* that still influence today.

Together, the **b-coefficients and a-coefficients** are the *DNA of the filter*.
They completely describe how the filter reacts to any signal.

---

### A Simple Example

Suppose you design a low-pass filter with `signal.butter`.
It might return something like this:

```python
b = [0.0004, 0.0016, 0.0024, 0.0016, 0.0004]
a = [1.0, -3.18, 3.86, -2.11, 0.43]
```

At first glance, these numbers look meaningless.
But in reality:

* The **b’s** are controlling how the current and past input samples mix in.
* The **a’s** are controlling how much of the past outputs echo back in.

This is why filters can have memory: what you hear (or see in a signal) at time `n` depends not just on the present input, but also on the echoes of the past.

---

### Why This Matters

Without b’s and a’s, you don’t have a filter — you just have raw data.

Every filter design method you use (`butter`, `cheby`, `ellip`, etc.) is really just a way of **spitting out the right set of b’s and a’s**.

But here’s the problem:

Looking at those coefficients directly doesn’t tell you much.
Are they cutting high frequencies? Boosting lows? Where’s the cutoff?

That’s why we need the next chapter — **an x-ray vision tool** that lets us *see* what these numbers are doing: the **Frequency Response**.
