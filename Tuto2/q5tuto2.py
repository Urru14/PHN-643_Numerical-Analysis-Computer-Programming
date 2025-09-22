import numpy as np
import matplotlib.pyplot as plt


# Constants
A = 1         
wavelength = 2  
frequency = 5  
k = 2 * np.pi / wavelength  
omega = 2 * np.pi * frequency  
L = 10  
num_points = 100  
Nt=100
dt = 0.2         

x = np.linspace(0, L, num_points)
t = np.linspace(0, Nt * dt, Nt)

y= A*np.sin(k*x-omega*t)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.plot(t,y*omega, label='x(t) = Acos(kx - ωt)' )
plt.xlabel('Time*Omega (Radian)')
plt.ylabel('Displacement (m)')
plt.title('Wave Motion')
plt.legend(loc='upper right')

plt.show()
