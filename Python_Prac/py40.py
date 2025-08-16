import math
import cmath
x = [1, 0, -1, 0]
N = 4 # Samples DFT (N=4)
# Bin Calculation
X = [0 + 0j]*N
k = list(range(len(x))) 
#print("K value:", k)
for kdx in k:
    #print("kdx:", kdx)
    for idx in range(len(x)):
        #print("idx:", idx)
        exp = cmath.exp(-1j*2*math.pi*idx*kdx/N)
        X[kdx] += x[idx]*exp
    print(X[kdx], X)