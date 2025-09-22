import numpy as np
import matplotlib.pyplot as plt

L = 1.0             # Length of the rod (m)
N = 10              # Number of segments
dx = L / N          # Spatial step (m)
dt = 0.01           # Time step (s)
time_steps = 100000  # Number of time steps
k = 200             # Thermal conductivity (W/m·K)
A = 0.01            # Cross-sectional area (m²)
rho = 7800          # Density (kg/m³)
cp = 500            # Specific heat capacity (J/kg·K)

alpha = k / (rho * cp)  # Thermal diffusivity (m²/s)

# Initial conditions
T0 = 20  # Initial temperature of the rod (°C)
TL = 100   # Boundary temperature at the right end (°C)
T = np.ones(N) * T0  # Temperature array for the rod
T[-1] = TL           # Set the boundary condition at the right end

'''
At each interior point 𝑖, we update the temperature based on the heat conduction equation using the finite difference approximation:
'''
for t in range(time_steps):
    T_new = T.copy()  # Create a copy to store the new temperature values
    for i in range(1, N - 1):
        T_new[i] = T[i] + alpha * dt / dx**2 * (T[i-1] - 2*T[i] + T[i+1])
    
    # Update temperatures for the next time step
    T = T_new.copy()
    
    # Apply boundary condition again
    T[-1] = TL

# Calculate heat transfer rate Q
Q = []
for i in range(N-1):
    t = k * A * (T[i+1] - T[i]) / dx
    Q.append(round(t, 2))

# Print final temperature distribution and heat transfer rates
print("Final Temperature Distribution:", T)
print("Heat Transfer Rates:", Q)

# Plot the final temperature distribution
x = np.linspace(0, L, N)
plt.subplot(1,2,1)
plt.plot(x, T, label='Temperature distribution')
plt.xlabel('Position along the rod (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution in the\n Rod after Heat Transfer')
plt.legend()
plt.grid(True)

# Plot the heat transfer rates Q (use midpoints of segments)
x_mid = np.linspace(dx/2, L - dx/2, N-1)  # Midpoints between segments
plt.subplot(1,2,2)
plt.plot(x_mid, Q, label='Heat Transfer Rate Q')
plt.xlabel('Position along the rod (m)')
plt.ylabel('Heat Transfer Rate (W)')
plt.title('Heat Transfer Rate Along \nthe Rod')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

