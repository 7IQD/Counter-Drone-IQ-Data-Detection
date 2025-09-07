import numpy as np
import matplotlib.pyplot as plt
import exercises_phase1 as ex_p1
import os

if __name__ == "__main__":
    f = [1000, 2000, 3000, 4000] #in Hz
    duration = [.01, 0.1, 1, 2] # in Seconds
    freq = 1000
    fs = max(10 * freq, 2000)  # ensures at least 10 samples per period
    
    # Dealing with Time Vector and Clean IQ
    t, iq_signal  = ex_p1.generate_iq(f=1000, fs=fs, duration=0.1, snr_db=None, seed=42)
    
    # Dealing with Frequency Vector and Clean IQ
    freq_bin_shifted, psd, psd_db = ex_p1.generate_fft_bin(iq_signal, fs=fs)     
    
    # Dealing with Noisy IQ
    snr_db = [10, 20, 30, 40]  
    noisy_iq_list = []
    noisy_iq_freq_bin_shifted_list = []
    psd_noisy_iq_list = []
    psd_db_noisy_iq_list = []
 
    for snr in snr_db:
        
        # Dealing with Noisy IQ in Time Domain
        noisy_iq = ex_p1.generate_noisy_iq(iq_signal, snr) 
        noisy_iq_list.append(noisy_iq)
        
        # Dealing with Noisy IQ in Frequency Domain
        noisy_iq_freq_bin_shifted, psd_noisy_iq, psd_db_noisy_iq = ex_p1.generate_fft_bin(noisy_iq, fs=fs) 
        noisy_iq_freq_bin_shifted_list.append(noisy_iq_freq_bin_shifted)
        psd_noisy_iq_list.append(psd_noisy_iq)
        psd_db_noisy_iq_list.append(psd_db_noisy_iq)
        
    # Create 4x2 subplots (time domain left, frequency domain right)
    fig, axs = plt.subplots(4, 2, figsize=(14,12)) 
    for i in range(len(noisy_iq_list)):
        axs[i, 0].plot(t, noisy_iq_list[i].real, label="I(Noisy)")
        axs[i, 0].plot(t, noisy_iq_list[i].imag, label="Q(Noisy)")
        axs[i, 0].set_title(f"Noisy IQ Signal - SNR={snr_db[i]} dB", fontweight='bold', fontsize=12)
        axs[i, 0].set_xlabel("Time [s]",fontweight='bold')
        axs[i, 0].set_ylabel("Amplitude",fontweight='bold')
        axs[i, 0].legend()
        axs[i, 0].grid(True)

        # Frequency domain plot (right column)
        axs[i, 1].plot(noisy_iq_freq_bin_shifted_list[i], psd_noisy_iq_list[i], label="Raw_Power")
        axs[i, 1].set_title(f"Noisy IQ Signal - SNR={snr_db[i]} dB", fontweight='bold', fontsize=12)
        axs[i, 1].set_xlabel("Frequency [Hz]", fontweight='bold')
        axs[i, 1].set_ylabel("Power [db]",fontweight='bold')
        axs[i, 1].legend()
        axs[i, 1].grid(True)
    plt.tight_layout()

current_directory = os.path.dirname(os.path.abspath(__file__))
print("Current directory:", current_directory) 
# Path to the plots folder
image_plot_folder = os.path.join(current_directory, "plots")
# Create folder if it doesn't exist
os.makedirs(image_plot_folder, exist_ok=True)  
plot_filename = os.path.join(image_plot_folder, "noisy_iq_time_freq.png")
plt.savefig(plot_filename)
plt.show()

        
 
    





    # # Example: save the current figure
    # plot_filename = os.path.join(image_plot_folder, "phase1_iq_signal_time_freq_psd.png")
    # plt.savefig(plot_filename)
    
    
   