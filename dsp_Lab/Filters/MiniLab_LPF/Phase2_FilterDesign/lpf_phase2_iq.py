import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz
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
    N =  fs*duration # No of samples
    N = int(fs*duration) # No of samples
    t =  np.linspace(0, duration, N, endpoint=False)
    I = np.cos(2*np.pi*f_signal*t)
    Q = np.sin(2*np.pi*f_signal*t)
    iq = I +1j*Q
    return iq, t

def get_coef(numtaps, cutoff_hz, fs):
    """
    Design an FIR low-pass filter using firwin.

    Parameters:
    ----------
    numtaps : int
        Number of filter taps (length of filter).
    cutoff_hz : float
        Cutoff frequency in Hz.
    fs : float
        Sampling frequency in Hz.

    Returns:
    -------
    h_hz : ndarray
        Array of filter coefficients.
    """
    return firwin(numtaps, cutoff_hz, fs=fs)

def get_freqz(h_hz, worN, fs):
    return freqz(h_hz, worN, fs)

def apply_lfilter(b, a, x):
    return lfilter(b, a, x)