Objective:
We’ll convolve a sinusoidal signal:

𝑥
[
𝑛
]
=
sin
⁡
(
2
𝜋
𝑓
𝑛
)
x[n]=sin(2πfn)
with the filter 
ℎ
[
𝑛
]
=
[
1
,
−
1
]
h[n]=[1,−1]

This filter gives the discrete difference, so:

Where the sine is increasing, the output will be positive

Where the sine is decreasing, the output will be negative

At peaks/troughs, the output will be near zero
What You'll See:
Input: smooth blue sinusoid

Output: red plot showing positive spikes when sine is rising, and negative dips when it's falling

Around the sine wave’s peaks and troughs, the output approaches zero (since the slope is near flat)

🧠 Physical Interpretation:
This is like measuring:

Slope

Speed of change

Also called discrete derivative

Used in:

FM demodulation

Instantaneous frequency estimation

Detecting fast vs. slow variation in IQ signals