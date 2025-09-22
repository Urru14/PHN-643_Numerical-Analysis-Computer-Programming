import numpy as np
import matplotlib.pyplot as plt

def montecarlo(a, b, f, m):
    x = np.random.uniform(a, b, m)
    return (b - a) * np.mean(f(x))

v1 = montecarlo(0, 2, lambda x: x**3 + x, 10000)
v2 = montecarlo(0, 2, lambda x: x**3 + x, 10000)
v3 = montecarlo(0, 2, lambda x: x**3 + x, 10000)
v4 = montecarlo(0, 2, lambda x: x**3 + x, 10000)
v5 = montecarlo(0, 2, lambda x: x**3 + x, 10000)
v6 = montecarlo(0, 2, lambda x: x**3 + x, 10000)
v7 = montecarlo(0, 2, lambda x: x**3 + x, 10000)
v8 = montecarlo(0, 2, lambda x: x**3 + x, 10000)

v = np.array([v1, v2, v3, v4, v5, v6, v7, v8])
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
final_v = np.mean(v)

print(f"1st time integral value calculated by Montecarlo method: {v1}")
print(f"2nd time integral value calculated by Montecarlo method: {v2}")
print(f"3rd time integral value calculated by Montecarlo method: {v3}")
print(f"4th time integral value calculated by Montecarlo method: {v4}")
print(f"5th time integral value calculated by Montecarlo method: {v5}")
print(f"6th time integral value calculated by Montecarlo method: {v6}")
print(f"7th time integral value calculated by Montecarlo method: {v7}")
print(f"8th time integral value calculated by Montecarlo method: {v8}")
print(f"Average of integral value calculated by Montecarlo method: {final_v}")

error = abs(final_v - v)
print(f"The error in values are respectively {error}")

# Plotting with red error bars
plt.plot()
plt.errorbar(x, v, yerr=error, fmt='bo', ecolor='red', capsize=5, label='Error')
plt.xlabel('n')
plt.ylabel('Integral values')
plt.title('n vs Integral values', fontsize=16)
plt.legend(fontsize=16)
plt.show()

