import numpy as np
import cmath
import matplotlib.pyplot as plt
N = 4
x_n = np.array([1, 0, 0, 1])

k = [0, 1 , 2, 3]

n = [0, 1, 2, 3]

DFT_list = [None] * N
for k_indx in k:
    X = 0
    for n_indx in n:
        X += x_n[n_indx]*cmath.exp(-2*np.pi*n_indx*k_indx/N)
    DFT_list[k_indx] = X 
print(DFT_list)       
