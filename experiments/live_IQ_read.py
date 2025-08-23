from rtlsdr import RtlSdr

# Initialize SDR
sdr = RtlSdr()

# Configure device
sdr.sample_rate = 2.4e6  # Hz
sdr.center_freq = 104.8e6  # Hz (FM broadcast test)
sdr.gain = 'auto'

# Capture 1024 samples
samples = sdr.read_samples(1024)

print(f"Captured {len(samples)} IQ samples")
print(f"First 5 samples: {samples[:5]}")

# Cleanup
sdr.close()
