import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 1000  
C = 0.001  
Qmax = 0.001  
Q0 = 0.001  

t_max = 10  
dt = 0.01  
time = np.arange(0, t_max, dt)
t0= R*C

for i in time:
     Q_charge = Qmax * (1 - np.exp(-time / (R * C)))
for i in time:
     Q_discharge = Q0 * np.exp(-time / (R * C))

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.axvline(t0, color='orange',ls ='--',linewidth=1, label = 'Relaxation time')
plt.plot(time, Q_charge, label='Charging')
plt.title('Charging of Capacitor')
plt.xlabel('Time (s)')
plt.ylabel('Charge (C)')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.axvline(t0, color='orange',ls ='--', linewidth=1, label = 'Relaxation time')
plt.plot(time, Q_discharge, label='Discharging', color='r')
plt.title('Discharging of Capacitor')
plt.xlabel('Time (s)')
plt.ylabel('Charge (C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

