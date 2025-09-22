import numpy as np
import matplotlib.pyplot as plt

g = 9.8  # m/s^2 (gravitational acceleration)
u = 2000  # m/s (velocity of expelled fuel)
q = 2100  # kg/s (fuel consumption rate)
t0 = 0  # initial time
t1 = 30  # final time

# Function f(t) that gives the velocity at time t
def f(t, m0):
    return u * np.log(m0 / (m0 - q * t)) - g * t

# Trapezoidal rule for numerical integration
def trapezoidal_integration(f, a, b, n, m0):
    h = (b - a) / n
    integral = 0
    for i in range(1, n):
        integral += (h/2)*(f(a+i*h,m0)+f(a+(i+1)*h,m0))
    return integral 

#Simpson integration
def simpson(f, a, b, n,m0):
  if n % 2:
   raise ValueError("n must be even (received n=%d)" % n)
  h = (b - a) / n
  s = f(a,m0) + f(b,m0)
  for i in range(1, n, 2):
    s += 4 * f(a + i * h, m0)
  for i in range(2, n-1, 2):
    s += 2 * f(a + i * h, m0)
  return s * h / 3

def Gauss_quad5(f,a,b,n, m0):
  x=np.array([0,(1/3)*np.sqrt(5-2*np.sqrt(10/7)),-(1/3)*np.sqrt(5-2*np.sqrt(10/7)),(1/3)*np.sqrt(5+2*np.sqrt(10/7)),-(1/3)*np.sqrt(5+2*np.sqrt(10/7))])
  w=np.array([128/225,(322+13*np.sqrt(70))/900,(322+13*np.sqrt(70))/900,(322-13*np.sqrt(70))/900,(322-13*np.sqrt(70))/900])
  return 0.5*(b-a)*np.sum(w*f(0.5*(b-a)*x+0.5*(b+a),m0))


def distance_traveled(m0, method='trapezoidal'):
    n=100
    if method == 'trapezoidal':
        return trapezoidal_integration(f, t0, t1, n, m0)
    if method == 'simpson':
        return simpson (f, t0, t1, n, m0)
    elif method == 'Gauss_quad5':
        return Gauss_quad5 (f, t0, t1, n, m0)
    
masses = np.linspace(100000, 200000, 100)  # range of initial mass from 100,000 to 200,000 kg
distances1 = [distance_traveled(m) for m in masses]
distances2 = [distance_traveled(m, method='simpson') for m in masses]
distances3 = [distance_traveled(m, method='Gauss_quad5') for m in masses]

#print(distances1)
#print(distances2)
#print(distances3)

# Plot the result
plt.subplot(2, 2, 1)
plt.plot(masses, distances1, label="Distance traveled")
plt.title("Trapezoidal method")
plt.xlabel('Initial Mass of the Rocket (kg)')
plt.ylabel('Distance Traveled (m)')
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(masses, distances2,'r',label="Distance traveled")
plt.title("Simpson method")
plt.xlabel('Initial Mass of the Rocket (kg)')
plt.ylabel('Distance Traveled (m)')
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(masses, distances3, 'c', label="Distance traveled")
plt.title("Gauss quadrature method n = 5")
plt.xlabel('Initial Mass of the Rocket (kg)')
plt.ylabel('Distance Traveled (m)')
plt.grid(True)
plt.legend()
plt.suptitle("Distance Traveled by the Rocket in First 30 Seconds", fontsize=16)
plt.tight_layout()
plt.show()

