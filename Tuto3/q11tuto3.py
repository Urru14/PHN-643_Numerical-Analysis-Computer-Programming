import numpy as np


data = np.loadtxt(r"/home/PHN_643/urvashi/Tuto3/expt.dat", skiprows=1)


C_microfarads = data[:, 0]  # First column as C values in µF
V = data[:, 1]              # Second column as V values

# Convert C from µF to F (Farads)
C = C_microfarads * 1e-6

# Calculate Q and E
Q = C * V         
E = 0.5 * C * V**2  

# Combining C, V, Q, and E into a 10x4 matrix
result = np.column_stack((C_microfarads, V, Q, E))  
np.savetxt('ce.out', result, header="C(µF)\t\tV\t\tQ\t\tE", fmt="%.6f", delimiter="\t")

