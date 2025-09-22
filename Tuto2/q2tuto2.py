import numpy as np
import matplotlib.pyplot as plt

# Constants all for Earth as planet and star for Sun
G = 6.67430e-11  
M = 2e30         
m = 5.972e24     
r0 = 1.496e11    

v0 = np.sqrt(G * M / r0)  

# Time settings
dt = 3600         
T = 3.154e7       
num_steps = int(T / dt)
theta = 0

x_positions = []
y_positions = []

# Simulation loop
for _ in range(num_steps):
    
    x = r0 * np.cos(theta)
    y = r0 * np.sin(theta)
    x = x/10e11
    y= y/10e11 
    x_positions.append(x)
    y_positions.append(y)
     
    theta += v0 * dt / r0 # theta= omega*t
 
# Plotting the orbit
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, label='Orbit')
plt.scatter(0, 0, color='red', label='Star')  # Star at origin
plt.xlabel('x (billion meters)')
plt.ylabel('y (billion meters)')
plt.title('Planet Orbit Simulation')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

