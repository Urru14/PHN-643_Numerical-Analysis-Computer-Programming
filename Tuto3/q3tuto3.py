# Given values
a=0
n1= 800000  # height of the satellite in meters
h=100
step= int((n1-a)/h)

def change_U (y):
    m = 500  # mass of the satellite in kg
    g0 = 9.81  # gravitational acceleration at sea level in m/s^2
    R = 6371000  # radius of Earth in meters
    U= m*g0*(R**2)/((R+y)**2)
    return (U)
def simpson(f, a, b, n):
  if n % 2:
   raise ValueError("n must be even (received n=%d)" % n)
  h = (b - a) / n
  s = f(a) + f(b)
  for i in range(1, n, 2):
    s += 4 * f(a + i * h)
  for i in range(2, n-1, 2):
    s += 2 * f(a + i * h)
  return s * h / 3    

delta_U = simpson(change_U,a,n1, step)


print(f"The change in gravitational potential energy (ΔU) is {delta_U:.2e} joules.")

