import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

R = 10      
V = 5       
L = 2       

def Mod_euler_method(f, x0, y0, xn, n):
    h = (xn - x0) / float(n)            
    x = np.arange(x0, xn + h, h)        
    y = np.array(y0).reshape(1, len(y0))
    
    for i in range(1, n + 1):
        k1 = h * f(x[i-1], y[i-1][0])   
        k2 = h * f(x[i-1] + h/2, y[i-1][0] + k1/2)  
        y_next = y[i-1][0] + k2         
        y = np.vstack((y, [y_next]))    
    
    return x, y.flatten()               

def LR_circuit(i, t):
    return (V - R * i) / L

def exact_solution(t):
    return (V / R) * (1 - np.exp(-R * t / L))

t_exact = np.linspace(0, 10, 1000)
t_values_odeint = np.linspace(0, 10, 100)
i_exact = exact_solution(t_exact)
i_odeint = odeint(LR_circuit, 0, t_values_odeint).flatten()
T, I = Mod_euler_method(lambda t, i: LR_circuit(i, t), 0, [0.0], 10, 1000)
i_error = np.abs(np.interp(T, t_values_odeint, i_odeint) - I)
print("The Error in Modified Euler Method and odeint function is:\n", i_error)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(T, I, label='Modified Euler Method', color='blue', alpha=0.7)
plt.plot(t_exact, i_exact, label='Exact Solution', color='red', linestyle='--')
plt.plot(t_values_odeint, i_odeint, label='odeint Solution', color='green', alpha=0.7)
plt.xlabel('Time (t)')
plt.ylabel('Current (i)')
plt.title('Current in LR Circuit: Modified Euler \nand Exact Solution')
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(T, i_error, label='Error: Modified Euler vs odeint', color='purple', alpha=0.7)
plt.xlabel('Time (t)')
plt.ylabel('Absolute Error')
plt.title('Absolute Error Comparison')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

