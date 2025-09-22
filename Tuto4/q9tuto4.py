import matplotlib.pyplot as plt
import numpy as np
import time

N0 = 10
L = 0.8

def Euler(f, x0, xn, y0):
    h=0.01
    x = np.arange(x0, xn + h, h)
    y = [y0]
    for i in range(1,len(x)):
        yi = y[i - 1] + h * f(x[i-1],y[i - 1])
        y.append(yi)
    return x, y

def RK2_method(f,x0,y0,xn):
    h=0.01
    x=np.arange(x0,xn+h,h)
    y0=np.array(y0)
    y=y0.reshape(1,len(y0))
    for i in range(1, len(x)):
         k1= h*f(x[i-1],y[i-1])
         k2= h*f(x[i-1] + h/2,y[i-1] + k1/2)
         y=np.append(y,[y[i-1] + k2]).reshape(i+1,len(y0))
    return x,y

def f(t,x):
    return -L * x

start_time = time.time()
t_euler, x_euler = Euler(f, 0, 1, 10)
euler_time = time.time() - start_time

start_time = time.time()
t_vec_RK2, x_vec_RK2 = RK2_method(f,0,[10],1)
vectorized_time = time.time() - start_time
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t_euler, x_euler, 'r', label='Euler Method')
plt.legend()
plt.title('Radioactive Decay: Euler Method')
plt.xlabel('Time')
plt.ylabel('Amount of Substance')
plt.subplot(1, 2, 2)
plt.plot(t_vec_RK2, x_vec_RK2, 'b', label='RK2 Method')
plt.title('Radioactive Decay: RK2 Method')
plt.xlabel('Time')
plt.ylabel('Amount of Substance')
plt.legend()
plt.tight_layout()
plt.show()

print(f"Computation time for standard Euler's method: {euler_time:.6f} seconds")
print(f"Computation time for vectorized RK2 method: {vectorized_time:.6f} seconds")
