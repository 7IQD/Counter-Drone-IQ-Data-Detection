# 📘 DFT & FFT Summary – Day 1

## ✅ Signal Used:
* `x = [0, 1, 0, -1]`   # 4-sample signal
* `fs = 4`              # Sampling rate = 4 Hz

## 📌 DFT Formula
$X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j \frac{2\pi}{N} kn}$

| $k$ | $X[k]$ Result | Explanation                     |
|-----|---------------|---------------------------------|
| 0   | 0             | DC (sum of signal = 0)          |
| 1   | –2j           | Pure 1 Hz sine                  |
| 2   | 0             | No energy at –2 Hz              |
| 3   | +2j           | Mirror of 1 Hz (–1 Hz comp)     |

## 📊 FFT Output (Python):
```python
X = np.fft.fft(x)
# [ 0.+0.j  0.-2.j  0.+0.j  0.+2.j ]