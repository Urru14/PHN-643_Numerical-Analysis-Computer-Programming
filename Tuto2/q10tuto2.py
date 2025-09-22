import numpy as np
import matplotlib.pyplot as plt

def ideal_gas_law(P0, V0, T0, R, n, variable='T', start=0, end=500, step=50):
    
    x = np.arange(start, end + step, step)
    y = []

    for value in x:
        if variable == 'T':
            # Varying temperature
            T = value
            P = (n * R * T) / V0
            V = V0
        elif variable == 'P':
            # Varying pressure
            P = value
            T = (P * V0) / (n * R)
            V = V0
        elif variable == 'V':
            # Varying volume
            V = value
            P = (n * R * T0) / V
            T = T0
        else:
            raise ValueError("Variable must be 'P', 'V', or 'T'")
        
        y.append(P if variable != 'P' else V if variable != 'V' else T)

    return x, y

# Constants and initial conditions
R = 8.314  # J/(mol·K)
P0 = 100 * 1000  # Convert kPa to Pa
V0 = 1  # m³
T0 = 300  # K
n = 1  # Number of moles

# Simulate varying temperature

x, y = ideal_gas_law(P0, V0, T0, R, n, variable='T', start=250, end=350, step=10)
plt.figure(figsize=(10, 6))
plt.subplot(1, 3, 1)
plt.plot(x, y, label='Pressure vs Temperature')
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (Pa)')
plt.title('Pressure vs Temperature')
plt.grid(True)
plt.legend()


# Simulate varying pressure
x, y = ideal_gas_law(P0, V0, T0, R, n, variable='P', start=50 * 1000, end=150 * 1000, step=10 * 1000)

plt.subplot(1, 3, 2)
plt.plot(x, y, label='Volume vs Pressure')
plt.xlabel('Pressure (Pa)')
plt.ylabel('Volume (m³)')
plt.title('Volume vs Pressure')
plt.grid(True)
plt.legend()


# Simulate varying volume

x, y = ideal_gas_law(P0, V0, T0, R, n, variable='V', start=0.5, end=1.5, step=0.1)

plt.subplot(1, 3, 3)
plt.plot(x, y, label='Temperature vs Volume')
plt.xlabel('Volume (m³)')
plt.ylabel('Temperature (K)')
plt.title('Temperature vs Volume')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

