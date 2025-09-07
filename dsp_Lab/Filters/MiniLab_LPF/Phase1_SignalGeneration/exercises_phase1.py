# Phase1_SignalGeneration/exercises_phase1.py
import numpy as np
import matplotlib.pyplot as plt


def generate_iq(f, fs, duration, snr_db=None, seed=42):
    """
    Generate a synthetic complex IQ signal, optionally with Gaussian noise.
    """
    N = int(fs * duration)  # number of samples in Seconds 
    t = np.linspace(0, duration, N, endpoint=False)
    I  = np.cos(2*np.pi*f*t)
    Q  = np.sin(2*np.pi*f*t)
    iq = I + 1j*Q
    return t, iq

def generate_fft_bin(iq, fs):
    """
    Generate fft bins for the IQ signal, optionally with Gaussian noise.
    """
    N = len(iq)  # number of samples  
    
    # FFT and shift
    fft_iq = np.fft.fft(iq) 
    fft_iq_shifted = np.fft.fftshift(fft_iq)

    # Create frequency vector
    freq_bin = np.fft.fftfreq(N, d=1/fs)
    freq_bin_shifted  = np.fft.fftshift(freq_bin)
       
    # PSD and magnitude in dB
    psd = np.abs(fft_iq_shifted)**2 / N    # Normalized power per bin/freq as signal scales with
    psd_db = 10 * np.log10(psd)    
    return freq_bin_shifted, psd, psd_db

def generate_noisy_iq(iq_signal, snr_db):
    """
    Add complex Gaussian noise to an IQ signal for a given SNR (in dB).
    
    Parameters:
    -----------
    iq_signal : np.ndarray
        Input complex baseband IQ signal.
    snr_db : float
        Desired signal-to-noise ratio in db.
    
    Returns:
    --------
    noisy_iq : np.ndarray
        IQ signal corrupted with complex Gaussian noise.
    """
    N = len(iq_signal)
    
    # Signal power (average over samples)
    signal_power = np.mean(np.abs(iq_signal)**2)
    
    # Convert SNR from dB to linear scale
    snr_linear = 10**(snr_db/10)

    # Noise power per complex sample
    noise_power = signal_power/snr_linear

    # Generate complex Gaussian noise
    complex_noise = np.sqrt(noise_power/2)*(np.random.randn(N) + 1j*np.random.randn(N))
    
    # Add noise to the signal
    noisy_iq = iq_signal + complex_noise
    return noisy_iq