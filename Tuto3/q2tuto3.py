import numpy as np

# Given values
g = 9.8  # gravitational acceleration in m/s^2
tolerance = 1e-5  # tolerance for the secant method


def position_func(omega, t, s):
    return (g / (2 * omega**2)) * (np.sinh(omega * t) - np.sin(omega * t)) - s

def secant_method(f, t, s, x0, x1, tol=1e-6, max_iter=100):
   fx0 = f(x0,t,s)
   for i in range(max_iter):
      fx1 = f(x1,t,s)
      x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
      if abs(x2 - x1) < tol:
        return x2
      x0, x1 = x1, x2
      fx0 = fx1
   raise Exception("No convergence in 100 iterations.")


s = 1  # distance in meters
t = 1  # time in seconds

# Initial guesses for ω
omega0 = 0.1  # Initial guess
omega1 = 1.0  # Second guess

omega_solution = secant_method(position_func, t, s, omega0, omega1, tolerance)


print(f"The value of ω that satisfies the equation is: {omega_solution:.5f}")
