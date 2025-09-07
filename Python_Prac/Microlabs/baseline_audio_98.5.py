# ====== Step 1: QUICK LISTEN (WBFM baseline) ======
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io.wavfile import write

# -------- SETTINGS (edit these) --------
FILE         = r"C:\Users\Ani\Desktop\Ajay Bharatiya\Counter-Drone-IQ-Data-Detection\Bootcamp_Mission\Stage1_Recon\data\iq_98.5.bin"
FS           = 2_400_000          # sample rate of capture (Hz)
FMT          = "u8"               # "u8" (rtl_sdr), "i16", or "f32"
CENTER_FREQ  = 98.5e6             # SDR was tuned here
TARGET_FREQ  = 98.5e6             # station you want
AUDIO_FS     = 48_000             # output WAV sample rate
# --------------------------------------


# -- loader for common formats (interleaved I,Q) --
def load_iq(path, fmt):
    raw = np.fromfile(path, dtype={"u8":np.uint8, "i16":np.int16, "f32":np.float32}[fmt])
    if raw.size % 2: raw = raw[:-1]
    i = raw[0::2].astype(np.float32)
    q = raw[1::2].astype(np.float32)
    if fmt == "u8":
        i = (i - 127.5)/128.0; q = (q - 127.5)/128.0
    elif fmt == "i16":
        i = i/32768.0; q = q/32768.0
    return i + 1j*q

x = load_iq(FILE, FMT)

# -- quick QC prints (optional) --
print("Samples:", len(x), "FS:", FS)
print("DC(I), DC(Q):", np.mean(x.real), np.mean(x.imag))

# 1) Shift station to baseband
shift_hz = TARGET_FREQ - CENTER_FREQ
n = np.arange(len(x))
x_bb = x * np.exp(-1j*2*np.pi*shift_hz*n/FS)

# 2) Band-limit ~ WBFM (≈200 kHz)
cutoff = 120_000  # keep the mono baseband + most energy
numtaps = 801
lp = signal.firwin(numtaps, cutoff, fs=FS)
x_filt = signal.lfilter(lp, 1.0, x_bb)

# 3) Decimate to manageable rate (e.g., 240 kHz)
decim = max(1, FS // 240_000)
FSd = FS // decim
i_d = signal.decimate(x_filt.real, decim, ftype='fir', zero_phase=True)
q_d = signal.decimate(x_filt.imag, decim, ftype='fir', zero_phase=True)
z = i_d + 1j*q_d

# 4) FM demod (discriminator)
y = np.angle(z[1:] * np.conj(z[:-1]))

# 5) De-emphasis (India/Europe = 50 µs)
tau = 50e-6
alpha = 1.0/(1.0 + FSd*tau)
b = [alpha]; a = [1.0, alpha-1.0]
y_de = signal.lfilter(b, a, y)

# 6) Audio LPF (≤15 kHz) and resample to 48 kHz
audio_lpf = signal.firwin(401, 16_000, fs=FSd)
y_a = signal.lfilter(audio_lpf, 1.0, y_de)
# resample
gcd = np.gcd(FSd, AUDIO_FS)
up, down = AUDIO_FS//gcd, FSd//gcd
audio = signal.resample_poly(y_a, up, down)

# 7) Normalize & save
audio = audio / (np.max(np.abs(audio)) + 1e-9)
write("baseline.wav", AUDIO_FS, (audio*0.9*32767).astype(np.int16))
print("Saved: baseline.wav")

# (Optional) Quick spectrum peek
f, pxx = signal.welch(z, fs=FSd, nperseg=32768, return_onesided=True)
plt.semilogy(f/1e3, pxx); plt.title("Baseband PSD (after LPF+decim)")
plt.xlabel("kHz"); plt.grid(True); plt.show()
