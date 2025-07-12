signal = [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0]
c_pulses = 0
c_gaps = 0
b_0 = 0           
b_1 = 0
for i in range(0, len(signal)):
    if (i - 1 >= 0 and signal[i-1]==0 and signal[i]==1):
        b_1 += 1
    elif (i - 1 >= 0 and signal[i-1]==1 and signal[i]==0):
        b_0 += 1
    elif(i==0 and signal[i]==1):
        b_1 += 1
    elif(i==0 and signal[i]==0):
        b_0 += 1
print(f"Pulses = {b_1} and Silence = {b_0}")