import numpy as np
import matplotlib.pyplot as plt

# Runge's function
def runge_function(x):
    return 1 / (1 + 25 * x**2)

# Lagrange interpolation function
def lagrange_interpolation(xi, yi, x):
    total = 0
    n = len(xi)
    for i in range(n):
        term = yi[i]
        for j in range(n):
            if j != i:
                term *= (x - xi[j]) / (xi[i] - xi[j])
        total += term
    return total
# Linear interpolation function
def linear_interpolation(xi, yi, x):
    for i in range(len(xi) - 1):
        if xi[i] <= x <= xi[i + 1]:
            return yi[i] + (yi[i + 1] - yi[i]) * (x - xi[i]) / (xi[i + 1] - xi[i])
    return None
# Given xi points (11 points from -1 to 1)
xi = np.linspace(-1, 1, 11)
yi = runge_function(xi)

# Fine grid for plotting the original function and the interpolations
x_fine = np.linspace(-1, 1, 500)
y_true = runge_function(x_fine)

# Interpolated values using Lagrange interpolation for 3rd and 7th order, note the point you choose according to it plots will be modified
y_p3 = np.array([lagrange_interpolation(xi[[2,4,6,8]], yi[[2,4,6,8]], x) for x in x_fine])   # 3rd-order interpolation
y_p7 = np.array([lagrange_interpolation(xi[[0,1,2,4,5,6,8,10]], yi[[0,1,2,4,5,6,8,10]], x) for x in x_fine])   # 7th-order interpolation (8 points)

# Interpolated values using linear interpolation
y_linear = np.array([linear_interpolation(xi, yi, x) for x in x_fine])  

plt.figure(figsize=(10, 8))

# Subplot 1: Original Runge's function
plt.subplot(2, 3, 1)
plt.plot(x_fine, y_true, color='black', linewidth=2)
plt.title("Runge's Function")
plt.xlabel('x')
plt.ylabel('f(x)')

# Subplot 2: 3rd Order Lagrange Interpolation
plt.subplot(2, 3, 2)
plt.plot(x_fine, y_p3, linestyle='--', color='green')
plt.title("3rd Order Lagrange Interpolation")
plt.xlabel('x')
plt.ylabel('f(x)')

# Subplot 3: 7th Order Lagrange Interpolation
plt.subplot(2, 3, 3)
plt.plot(x_fine, y_p7, linestyle='--', color='red')
plt.title("7th Order Lagrange Interpolation")
plt.xlabel('x')
plt.ylabel('f(x)')

# Subplot 4: Data points
plt.subplot(2, 3, 4)
plt.scatter(xi, yi, color='black', zorder=5)
plt.title("Data Points")
plt.xlabel('x')
plt.ylabel('f(x)')

# Subplot 5: Linear Interpolation
plt.subplot(2, 3, 5)
plt.plot(x_fine, y_linear, linestyle='--', color='blue')
plt.title("Linear Interpolation")
plt.xlabel('x')
plt.ylabel('f(x)')

plt.suptitle("Interpolation of Runge's Function Using Lagrange Interpolation", fontsize=16)

plt.tight_layout()
plt.grid(True)
plt.show()

