#List Slicing & Interleaving Test
import numpy as np
#You have two lists:
I = np.array([0, 1, 2, 3])
Q = np.array([9, 8, 7, 6])
#create a non zero array of twice the size of I or Q to store the IQ Data
iq_array = np.zeros(2*len(I)) 
#print(len(I), len(iq_array))
iq_array[0::2] = I
iq_array[1::2] = Q
print(iq_array)
I_extracted = iq_array[0::2]
Q_extracted = iq_array[1::2]
print('I recovered', I_extracted)
print('Q recovered', Q_extracted)