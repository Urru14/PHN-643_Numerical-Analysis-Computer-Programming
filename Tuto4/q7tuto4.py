import numpy as np
import matplotlib.pyplot as plt

def RK2_method(f,x0,y0,xn,n):
    h=(xn-x0)/float(n)
    x=np.arange(x0,xn+h,h)
    y0=np.array(y0)
    y=y0.reshape(1,len(y0))
    for i in range(1, n + 1):
         k1= h*f(x[i-1],y[i-1])
         k2= h*f(x[i-1] + h/2,y[i-1] + k1/2)
         y=np.append(y,[y[i-1] + k2]).reshape(i+1,len(y0))
    return x,y
def f(t,x):
    omega = 1
    f0= x[1]
    f1= -omega**2 * x[0]
    return np.array([f0,f1])
T,I = RK2_method(f,0,[0.0,1],10,1000)
plt.plot(T, I, label='RK-2', color='red', linestyle='--')
plt.xlabel('Time (t)')
plt.ylabel('Value')
plt.title('Simple Harmonic Oscillator: Position and Velocity vs. Time')
plt.grid()
plt.tight_layout()
plt.show()

