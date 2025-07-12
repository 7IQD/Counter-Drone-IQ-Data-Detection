import numpy as np
name = ["Ajay", "Pramod", "Suchitra"]
surName = ["Bharatiya", "Singh", "Shroff"]

for n_idx, s_indx in zip(name, surName):
    print(f"{n_idx} {s_indx}")