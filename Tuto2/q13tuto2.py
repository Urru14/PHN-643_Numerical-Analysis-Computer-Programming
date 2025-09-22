import numpy as np
import matplotlib.pyplot as plt

# Constants for Isotope 1
lambda1 = 0.01  
N1_0 = 1000     

# Constants for Isotope 2
lambda2 = 0.02  
N2_0 = 500      

# Time parameters
total_time = 24  
time_steps = np.arange(0, total_time + 1, 1)  


N1 = np.zeros(len(time_steps))
N2 = np.zeros(len(time_steps))

# Calculate populations at each time step
for t in time_steps:
    N1[t] = N1_0 * np.exp(-lambda1 * t)
    N2[t] = N2_0 * np.exp(-lambda2 * t)
print(f"{'Time (hours)':<15} {'Isotope 1 Population':<22} {'Isotope 2 Population':<15}")
for t in time_steps:
    print(f"{t:<15} {N1[t]:<22.2f} {N2[t]:<15.2f}")    

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_steps, N1, label='Isotope 1 (λ=0.01)', color='blue')
plt.plot(time_steps, N2, label='Isotope 2 (λ=0.02)', color='red')
plt.xlabel('Time (hours)')
plt.ylabel('Population')
plt.title('Radioactive Decay of Isotopes Over Time')
plt.legend()
plt.grid(True)
plt.show()

