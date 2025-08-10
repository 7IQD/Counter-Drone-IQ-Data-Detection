import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

# Settings
fs = 48000       # Sample rate
tone_duration = 0.5  # seconds
gap_duration = 0.2   # seconds
freqs = [440, 660, 660, 550, 880]  # "hello"-like tone pattern (H-E-L-L-O)

signal = np.array([], dtype=np.float32)

# Generate tones with silence gaps
for f in freqs:
    t = np.linspace(0, tone_duration, int(fs*tone_duration), endpoint=False)
    tone = 0.4 * np.sin(2 * np.pi * f * t)
    silence = np.zeros(int(fs * gap_duration))
    signal = np.concatenate((signal, tone, silence))

# Convert to IQ: I = signal, Q = 0
I = signal
Q = np.zeros_like(I)
IQ = np.stack([I, Q], axis=-1)  # shape: [samples, 2]

# Save as stereo WAV (I = Left, Q = Right)
write("hello.wav", fs, IQ.astype(np.float32))

# Plot preview
plt.plot(IQ[:1000, 0], label='I')
plt.plot(IQ[:1000, 1], label='Q')
plt.title("Simulated IQ Tone (Hello)")
plt.legend()
plt.grid()
plt.show()
