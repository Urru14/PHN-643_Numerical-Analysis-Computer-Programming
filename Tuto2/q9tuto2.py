import numpy as np
import matplotlib.pyplot as plt

# Constants
theta0 = 0.1  
g = 9.81      
L = 1.0       

# Time parameters
t_max = 10    
dt = 0.01     
times = np.arange(0, t_max, dt)

angular_displacement = theta0 * np.cos(np.sqrt(g / L) * times)

x_positions = L * np.sin(angular_displacement)
y_positions = -L * np.cos(angular_displacement)

plt.figure(figsize=(10, 5))

# Plot angular displacement
plt.subplot(1, 2, 1)
plt.plot(times, angular_displacement)
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (radians)')
plt.title('Angular Displacement vs. Time')

# Plot position
plt.subplot(1, 2, 2)
plt.plot(x_positions, y_positions)
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Pendulum Position')

plt.tight_layout()
plt.show()

