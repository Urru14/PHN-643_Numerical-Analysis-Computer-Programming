import matplotlib.pyplot as plt
import numpy as np
import math

def hermite_polynomial(n, x):
    H_n = 0
    for s in range(n // 2 + 1):  # Sum from s = 0 to floor(n/2)
        term = ((-1)**s * (2*x)**(n - 2*s) * math.factorial(n)) / (math.factorial(n - 2*s) * math.factorial(s))
        H_n += term
    return H_n

x_values = np.linspace(-5, 5, 400)

H1_values = [hermite_polynomial(1, x) for x in x_values]
H2_values = [hermite_polynomial(2, x) for x in x_values]
H3_values = [hermite_polynomial(3, x) for x in x_values]

plt.figure(figsize=(10, 6))

plt.plot(x_values, H1_values, label=r'$H_1(x)$', color='blue')
plt.plot(x_values, H2_values, label=r'$H_2(x)$', color='green')
plt.plot(x_values, H3_values, label=r'$H_3(x)$', color='red')

plt.title('Hermite Polynomials $H_n(x)$ for $n=1, 2, 3$')
plt.xlabel('$x$')
plt.ylabel('$H_n(x)$')
plt.grid(True)
plt.legend()
plt.show()
