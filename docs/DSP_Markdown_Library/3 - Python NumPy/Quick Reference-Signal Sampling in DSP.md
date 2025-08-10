🧠 Quick Reference: Signal Sampling in DSP

| Term                         | Meaning                          | Think of it as...               |
| ---------------------------- | -------------------------------- | ------------------------------- |
| `f`                          | Signal frequency (Hz)            | How fast the wave "spins"       |
| `Fs`                         | Sampling rate (samples/sec)      | How often we *look* at the wave |
| `T = 1/Fs`                   | Time between samples             | Like a camera shutter interval  |
| `t[n] = n / Fs`              | Time of sample `n`               | When sample `n` was taken       |
| `x[n] = exp(j·2π·f·t[n])`    | Sampled complex signal           | Each point on a spinning circle |
| `Samples per cycle = Fs / f` | How many samples for 1 full wave | Important for DFT/FFT!          |
| `Total time = N / Fs`        | Total capture duration           | If you collected N samples      |
