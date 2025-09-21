import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve
import os

def generate_iq(fs, f_signal, duration):
    """
    Generate a simple IQ signal: I = cos(2πft), Q = sin(2πft)
    
    Parameters:
        fs (int): Sampling frequency in Hz
        f_signal (int): Baseband signal frequency in Hz
        duration (float): Duration of the signal in seconds
    
    Returns:
        iq (np.ndarray): Complex IQ signal
        t (np.ndarray): Time vector
    """
    N = int(fs*duration) # No of samples
    t =  np.linspace(0, duration, N, endpoint=False)
    I = np.cos(2*np.pi*f_signal*t)
    Q = np.sin(2*np.pi*f_signal*t)
    iq = I + 1j*Q
    print("Length of iq", len(iq))
    return iq, t

def rrc_taps(beta, sps, span):
    N = span * sps + 1
    t = (np.arange(N) - (N-1)/2) / sps
    h = np.zeros_like(t, dtype=float)
    for i, tt in enumerate(t):
        if abs(tt) < 1e-8:
            h[i] = 1.0 - beta + (4*beta/np.pi)
        elif abs(abs(4*beta*tt) - 1.0) < 1e-8:
            h[i] = (beta/np.sqrt(2)) * (
                (1+2/np.pi)*np.sin(np.pi/(4*beta)) +
                (1-2/np.pi)*np.cos(np.pi/(4*beta))
            )
        else:
            h[i] = (np.sin(np.pi*tt*(1-beta)) +
                    4*beta*tt*np.cos(np.pi*tt*(1+beta))) / \
                   (np.pi*tt*(1-(4*beta*tt)**2))
    return t, h / np.sum(h)   # return both time axis and normalized taps

# -------------------------------
# Main test
# -------------------------------
fs = 10000         # sampling rate (Hz)
f_signal = 1000    # tone freq (Hz)
duration = 0.01    # seconds
iq, t = generate_iq(fs, f_signal, duration)

# Create RRC filter
beta = 0.35
sps = 8
span = 4
t_rrc, h_rrc = rrc_taps(beta=beta, sps=sps, span=span)

# Filter the IQ signal with RRC
iq_filtered = np.convolve(iq, h_rrc, mode="same")


# -------------------------------
# Plots
# -------------------------------

# Plot RRC impulse response
plt.figure(figsize=(6,3))
plt.plot(t_rrc, h_rrc, marker="o")
plt.title(f"RRC impulse: beta={beta}, span={span}, sps={sps}, taps={len(h_rrc)}")
plt.xlabel("Time (symbols)")
plt.grid(True)
plt.show()

# Plot real & imag of original vs filtered IQ
plt.figure(figsize=(10,4))
plt.subplot(2,1,1)
plt.plot(t, np.real(iq), label="Original I", alpha=0.7)
plt.plot(t, np.real(iq_filtered), label="Filtered I", alpha=0.7)
plt.legend(); plt.grid(True); plt.title("I channel")

plt.subplot(2,1,2)
plt.plot(t, np.imag(iq), label="Original Q", alpha=0.7)
plt.plot(t, np.imag(iq_filtered), label="Filtered Q", alpha=0.7)
plt.legend(); plt.grid(True); plt.title("Q channel")
plt.tight_layout()
plt.show()