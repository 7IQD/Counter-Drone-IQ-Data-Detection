**Chapter 1: IQ Signals and the Geometry of Communication**

**1.1 Introduction**
In modern wireless communication systems, signals are represented and processed using their In-phase (I) and Quadrature (Q) components. This I/Q representation forms the foundational concept in software-defined radio (SDR) and digital signal processing (DSP). This chapter introduces IQ signals from both mathematical and geometric perspectives, highlighting their relevance in capturing the full essence of RF signals.

**1.2 The Concept of IQ**
An IQ signal is a complex signal expressed as:

```
s(t) = I(t) + jQ(t)
```

Here, I(t) is the real part (in-phase), and Q(t) is the imaginary part (quadrature component). Together, they capture amplitude and phase variations over time.

**1.3 The Phasor and the Complex Plane**
IQ signals can be visualized as rotating vectors (phasors) on the complex plane:

* I(t): x-axis projection
* Q(t): y-axis projection

As the signal evolves, the phasor rotates, and the magnitude and phase change, encoding data.

**1.4 Geometric Interpretation of Modulation**
Modulation schemes like AM, FM, PSK, QAM, and FSK can be seen geometrically as changes in:

* Length of the vector (amplitude)
* Angle with respect to I-axis (phase)
* Rotation rate (frequency)

For example:

* QPSK maps bits to points in four quadrants
* QAM uses a constellation of amplitude and phase combinations

**1.5 Sampling and Digitization**
In SDR systems, RF signals are downconverted and sampled as discrete IQ pairs:

* Analog mixer shifts the signal to baseband
* ADC digitizes I(t) and Q(t) at high sampling rates

These samples form the raw IQ data that is the basis for all further processing.

**1.6 Why IQ Matters in Counter-Drone Systems**
Drones often use standardized communication protocols in ISM bands. Their signals have distinctive IQ patterns:

* Specific modulation styles (e.g., FHSS, OFDM, DSSS)
* Consistent timing and spectral footprints

Analyzing the IQ geometry enables:

* Signal classification
* Detection of drone presence
* Feature extraction for ML pipelines

**1.7 Summary**
IQ representation is not just a signal format — it is a geometric language of modern communication. Understanding the behavior of signals in the IQ plane is critical for detecting and analyzing drone transmissions using SDR platforms.
