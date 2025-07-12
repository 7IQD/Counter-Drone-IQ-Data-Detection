signal = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
# rising_idx = []
# falling_idx = []
pattern_start_idx=[]
pattern_end_idx=[]
for i in range(len(signal)-2):
    if signal[i]==0 and signal[i+1]==1 and signal[i+2]==0:
        pattern_start_idx.append(i)
        pattern_end_idx.append(i+2)
#         rising_idx.append(i+1)
#     elif signal[i]==1 and signal[i+1]==0:
#         falling_idx.append(i+1)
#print(f"Rising Edge at:{rising_idx} and Falling Edge at {falling_idx}")
print(f"Pattern identified at index strating from {pattern_start_idx} and ending at index:{pattern_end_idx}")