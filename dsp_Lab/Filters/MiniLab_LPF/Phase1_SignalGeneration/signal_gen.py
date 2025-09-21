# Phase 1: Signal Generation - generate and visualize IQ signals
import numpy as np
import matplotlib.pyplot as plt
import os

def generate_iq(fs=10000, f_signal=1000, duration = 0.01):
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
    
if __name__ == '__main__':
    iq_signal, t = generate_iq()
    print(iq_signal)

    # Create IQ signal with Noise for PSD Analysis
    #Compute signal power (RMS²)
    signal_power = np.mean(np.abs(iq_signal)**2)


    SNR_dB = 20
    snr_linear = 10**(SNR_dB/10)
    # Remember: snr_db = signal_power/noise_power
    noise_power = signal_power/snr_linear

    # Now create a Gaussian Noise Array of Length N = len(iq_signal)
    N = len(iq_signal)
    noise = np.sqrt(noise_power/2) * (np.random.randn(N) + 1j*np.random.randn(N))

    # Now create a IQ signal with Gaussian Noise Array of Length N = len(iq_signal)
    iq_noisy = iq_signal + noise

    # Optional: plot IQ with Noise
    fs = 10000

    # creating the FFT Bins - Migrating to Frequence Domain from Time Domain
    iq_noisy_fft =  np.fft.fft(iq_noisy)
    # Shifting the bins- Realigning to Zero axis
    iq_noisy_fft_shifted =  np.fft.fftshift(iq_noisy_fft)

    # Creating the Freq Vector for X axis
    iq_noisy_freq = np.fft.fftfreq(N, 1/fs)
    # Shifting the Freq bins
    iq_noisy_freq_shifted =  np.fft.fftshift(iq_noisy_freq)

    # Creating the Magnitude Vector for Y axis
    psd = np.abs(iq_noisy_fft_shifted)**2 / N    
    magnitude = 10 * np.log10(psd)


    # ----------- Plotting -----------
    plt.figure(figsize=(10, 10))

    # Plot the Clean IQ signal
    plt.subplot(3, 1, 1)
    plt.plot(t, iq_signal.real, label='I (in-phase)')
    plt.plot(t, iq_signal.imag, label='Q (quadrature)')
    plt.title("Time-domain IQ Signal (Time Domain)")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)

    # Plot the Noisy IQ signal
    plt.subplot(3, 1, 2)
    plt.plot(t, iq_noisy.real, label='I noisy')
    plt.plot(t, iq_noisy.imag, label='Q noisy')
    plt.title("Noisy IQ Signal (Time Domain)")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)

    # PSD of IQ + Noise
    plt.subplot(3, 1, 3)
    plt.plot(iq_noisy_freq_shifted, magnitude, label="PSD")
    plt.title("PSD Plot - IQ + Gaussian Noise Signal")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Power [dB]")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Current script directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print("Current directory:", current_directory)

    # Path to the plots folder
    image_plot_folder = os.path.join(current_directory, "plots")
    print("Image folder:", image_plot_folder)

    # Create folder if it doesn't exist
    os.makedirs(image_plot_folder, exist_ok=True)

    # Example: save the current figure
    plot_filename = os.path.join(image_plot_folder, "Phase1_IQ_PSD.png")
    plt.savefig(plot_filename)
    print(f"Plot saved as: {plot_filename}")