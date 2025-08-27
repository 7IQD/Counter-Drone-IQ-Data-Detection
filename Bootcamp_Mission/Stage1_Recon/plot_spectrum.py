import numpy as np
import matplotlib.pyplot as plt

def plot_spectrum(freq_axis_hz, power_spectrum, title="Power-Spectrum Plot", xlabel="Frequency (Hz)", ylabel="Power (dB)", freq_in_mhz=False):
    """
    Plot the power spectrum.

    Parameters
    ----------
    freq_axis_hz : np.ndarray
        Frequency axis in Hz
    power_spectrum : np.ndarray
        Power spectrum in dB
    title : str
        Plot title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    freq_in_mhz : bool
        If True, convert X-axis to MHz
    """

    x_axis = freq_axis_hz / 1e6 if freq_in_mhz else freq_axis_hz
    xlabel = xlabel if not freq_in_mhz else "Frequency (MHz)"
    # Plot
    plt.figure(figsize=(10,4))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # Use spec_centering (frequency axis) and power_spectrum (y axis)
    plt.plot(x_axis, power_spectrum)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    