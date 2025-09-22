import numpy as np
import matplotlib.pyplot as plt

N0 = 10
L = 0.8

def Euler(f, x0, xn, y0):
    h = 0.01
    x = np.arange(x0, xn + h, h)
    y = [y0]
    for i in range(1, len(x)):
        yi = y[i - 1] + h * f(y[i - 1])
        y.append(yi)
    return x, y

def f(x):
    return -L * x

t, N = Euler(f, 0, 1, N0)
N_analytical = N0 * np.exp(-L * t)
absolute_error = np.abs(np.array(N) - N_analytical)
#print (t,N)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, N, 'r', label='Euler Method')
plt.plot(t, N_analytical, 'k--', label='Analytical Solution')
plt.xlabel('Time')
plt.ylabel('Amount of Substance')
plt.title('Radioactive Decay: Euler vs Analytical Solution')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, absolute_error, 'b', label='Absolute Error')
plt.xlabel('Time')
plt.ylabel('Absolute Error')
plt.title('Absolute Error Between Euler and Analytical Solution')
plt.legend()

plt.tight_layout()
plt.show()

