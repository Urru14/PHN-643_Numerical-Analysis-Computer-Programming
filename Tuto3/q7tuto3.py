import numpy as np
import matplotlib.pyplot as plt

kB = 1.38e-23  # Boltzmann constant in J/K
Tc = float(input("Enter Critical Temperature in Kelvin: "))

# Function to calculate the energy gap E(T)
def energy_gap(T, Tc):
    return 3.52 * kB * Tc * np.sqrt(1 - (T / Tc))

# Temperature range from 0 to Tc
T_values = np.linspace(0, Tc, 100)
E_values = energy_gap(T_values, Tc)

plt.figure(figsize=(10, 6))
plt.plot(T_values, E_values, label='E(T) = 3.52kB Tc √(1 - T/Tc)', color='blue')
plt.title('Energy Gap E(T) vs Temperature T')
plt.xlabel('Temperature (K)')
plt.ylabel('Energy Gap E(T) (J)')
plt.ylim(0, np.max(E_values) * 1.1)
plt.xlim(0, Tc+1)
plt.legend()
plt.grid()
plt.show()
