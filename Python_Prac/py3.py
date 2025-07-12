signal = [0, 0, 1, 1, 0, 1, 0]
#print(len(signal)) --- 7
for j in range(1, len(signal)):
  if signal[j-1] == 0 and signal[j] == 1:
        print(f"Rising edge at index {j-1}")