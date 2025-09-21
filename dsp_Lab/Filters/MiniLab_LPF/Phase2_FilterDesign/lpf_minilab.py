# lpf_minilab_lpf.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz
import lpf_phase2_iq as ex2

f_signal = 1000    # 1 Khz signal
fs = 10000           # Sampling frequency (Hz)
duration = 1
N = int(fs*duration)     # No. of samples
cutoff_hz = 1500    # Desired cutoff in Hz
numtaps = 101       # Filter length (number of taps)
# cutoff specified in Hz (since fs is given)

h_hz = ex2.get_coef(numtaps, cutoff_hz, fs=fs)
print(h_hz[:10], sum(h_hz))  # show first 10 coefficients

# compute freq response
w, H = ex2.get_freqz(h_hz, worN=4096, fs=fs)

#👉 Generate IQ signal - Pre Filter
iq_signal, t =  ex2.generate_iq(fs, f_signal, duration)
print("IQ Signal:20 samples", (iq_signal.real[:20]) + 1j*(iq_signal.imag)[:20])

iq_interferer, t = ex2.generate_iq(fs=10000, f_signal=3000, duration=1)
print("IQ Interference", iq_interferer[:20])

iq_signal = iq_signal + iq_interferer

# 👉 IQ signal - Pre Filter - Apply lfilter# Apply FIR filter
iq_filt = ex2.apply_lfilter(b=h_hz, a=[1.0], x=iq_signal)
print("Filtered IQ", (iq_filt.real[:10]) + 1j*(iq_filt.imag[:10]))

# Time-domain signals
I_pre = iq_signal.real
Q_pre = iq_signal.imag
I_post = iq_filt.real
Q_post = iq_filt.imag

# Frequency-domain signals (dB)
fft_I_pre = 20*np.log10(np.abs(np.fft.fftshift(np.fft.fft(I_pre))) + 1e-12)
fft_Q_pre = 20*np.log10(np.abs(np.fft.fftshift(np.fft.fft(Q_pre))) + 1e-12)
fft_I_post = 20*np.log10(np.abs(np.fft.fftshift(np.fft.fft(I_post))) + 1e-12)
fft_Q_post = 20*np.log10(np.abs(np.fft.fftshift(np.fft.fft(Q_post))) + 1e-12)

freq = np.fft.fftshift(np.fft.fftfreq(N, 1/fs))

# 2x2 Subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 8))
plt.suptitle("IQ Signal: FIR Low-Pass Filtering (Time & Frequency Domain)", fontweight='bold')
# Time-domain I
axs[0, 0].plot(t[:200], I_pre[:200], label='I pre-filter')
axs[0, 0].plot(t[:200], I_post[:200], label='I post-filter')
axs[0, 0].set_title("I-channel: Time Domain")
axs[0, 0].set_xlabel("Time [s]")
axs[0, 0].set_ylabel("Amplitude")
axs[0, 0].grid(True)
axs[0, 0].legend()

# Time-domain Q
axs[0, 1].plot(t[:200], Q_pre[:200], label='Q pre-filter')
axs[0, 1].plot(t[:200], Q_post[:200], label='Q post-filter')
axs[0, 1].set_title("Q-channel: Time Domain")
axs[0, 1].set_xlabel("Time [s]")
axs[0, 1].set_ylabel("Amplitude")
axs[0, 1].grid(True)
axs[0, 1].legend()

# Frequency-domain I (dB)
axs[1, 0].plot(freq, fft_I_pre, label='I pre-filter')
axs[1, 0].plot(freq, fft_I_post, label='I post-filter')
axs[1, 0].set_title("I-channel: Frequency Domain (dB)")
axs[1, 0].set_xlabel("Frequency [Hz]")
axs[1, 0].set_ylabel("Magnitude [dB]")
axs[1, 0].grid(True)
axs[1, 0].legend()

# Frequency-domain Q (dB)
axs[1, 1].plot(freq, fft_Q_pre, label='Q pre-filter')
axs[1, 1].plot(freq, fft_Q_post, label='Q post-filter')
axs[1, 1].set_title("Q-channel: Frequency Domain (dB)")
axs[1, 1].set_xlabel("Frequency [Hz]")
axs[1, 1].set_ylabel("Magnitude [dB]")
axs[1, 1].grid(True)
axs[1, 1].legend()

plt.tight_layout()
plt.show()
