from scipy.signal import firwin, freqz

def get_coef(numtaps, cutoff_hz, fs):
    """Return FIR low-pass filter coefficients"""
    return firwin(numtaps, cutoff_hz, fs=fs)

def get_freqz(h_hz, worN=4096, fs=1.0):
    """Return frequency response of filter"""
    w, H = freqz(h_hz, worN=worN, fs=fs)
    return w, H

def rrc_taps(beta, sps, span):
    """Return Root Raised Cosine filter taps"""
    import numpy as np
    N = span * sps + 1
    t = (np.arange(N) - (N-1)/2) / sps
    h = np.zeros_like(t)
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
    return h / np.sum(h)
