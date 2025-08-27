import numpy as np

def compute_spectrum(iq, fs, center_freq=0):
    """
    Compute the frequency spectrum of IQ data.

    Parameters
    ----------
    iq : np.ndarray
        Complex IQ samples
    fs : float
        Sampling frequency in Hz
    center_freq : float, optional
        Center frequency in Hz (default = 0 for baseband)

    Returns
    -------
    freq_axis : np.ndarray
        Frequency axis in Hz (shifted by center_freq)
    power_spectrum : np.ndarray
        Power spectrum in dB
    """
    # Temporary placeholder until computation is done
    #Bin Spectrum Centering through FFT Shift
    freqbin = np.fft.fft(iq)
    freqbin_centering = np.fft.fftshift(freqbin)

    power_spectrum = 20 * np.log10(np.abs(freqbin_centering))

    N = len(iq) # No of samples in the file
    freq_axis_hz = np.fft.fftshift(np.fft.fftfreq(N, 1/fs)) + center_freq
    return freq_axis_hz, power_spectrum
