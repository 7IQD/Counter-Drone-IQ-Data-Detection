from rtlsdr import RtlSdr

# Try opening SDR
sdr = RtlSdr()

print("Dongle detected successfully!")
print(f"Sample rate: {sdr.sample_rate/1e6} MHz")
print(f"Center frequency: {sdr.center_freq/1e6} MHz")
print(f"Gain: {sdr.gain} dB")

sdr.close()

