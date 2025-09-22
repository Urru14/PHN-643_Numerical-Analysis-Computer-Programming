import numpy as np
import matplotlib.pyplot as plt
import time

def f(t, x):
    return -3 * x * np.cos(t)

def exact_solution(t):
    return np.exp(-3 * np.sin(t))

def Euler(f, x0, xn, y0,n):
    h=(xn-x0)/float(n)
    x = np.arange(x0, xn + h, h)
    y = [y0]
    for i in range(1,n+1):
        yi = y[i - 1] + h * f(x[i-1],y[i - 1])
        y.append(yi)
    return x, y

def vectorized_euler_method(f,x0,y0,xn,n):
    h=(xn-x0)/float(n)
    x=np.arange(x0,xn+h,h)
    y0=np.array(y0)
    y=y0.reshape(1,len(y0))
    for i in range(1, n + 1):
         y=np.append(y,[y[i-1] + h*f(x[i-1],y[i-1])]).reshape(i+1,len(y0))
    return x,y

start_time = time.time()
t_euler, x_euler = Euler(f, 0, 10, 1,1000)
euler_time = time.time() - start_time

start_time = time.time()
t_vectorized, x_vectorized = vectorized_euler_method(f,0,[1.0],10,1000)
vectorized_time = time.time() - start_time

t_exact = np.linspace(0, 10, 1000)
x_exact = exact_solution(t_exact)

plt.figure(figsize=(12, 6))
plt.plot(t_exact, x_exact, label='Exact Solution', color='red', linestyle='--')
plt.plot(t_euler, x_euler, label='Euler Method', color='blue', alpha=0.5)
plt.plot(t_vectorized, x_vectorized, label='Vectorized Euler Method', color='green', alpha=0.5)
plt.xlabel('Time (t)')
plt.ylabel('x(t)')
plt.title('Comparison of Euler Methods with Exact Solution')
plt.legend()
plt.grid()
plt.show()

print(f"Computation time for standard Euler's method: {euler_time:.6f} seconds")
print(f"Computation time for vectorized Euler's method: {vectorized_time:.6f} seconds")

