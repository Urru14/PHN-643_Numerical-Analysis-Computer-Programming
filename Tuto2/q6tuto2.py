import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 0.1  
omega = 2 * np.pi  

# Time settings
t_start = 0  
t_end = 2  
dt = 0.01  

times = np.arange(t_start, t_end + dt, dt)

positions = A * np.cos(omega * times)
plt.figure(figsize=(10, 6))
plt.plot(times, positions, label='x(t) = A * cos(ω * t)')
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Simple Harmonic Motion of a Mass on a Spring')
plt.grid(True)
plt.legend()
plt.show()
