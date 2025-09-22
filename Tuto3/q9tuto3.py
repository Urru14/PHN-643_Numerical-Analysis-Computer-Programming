import numpy as np

#Function defination
def f(x):
    return 3 * x**2 + 2 * x

#Trapezoidal integation
def Trap(func, a, b, n):
  h = (b - a) / n
  sum=0
  for i in range(n):
    sum += (h/2)*(func(a+i*h)+func(a+(i+1)*h))

  return sum

#Simpson integration
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

#5-point Gauss quadrature
def Gauss_quad5(a,b,f):
  x=np.array([0,(1/3)*np.sqrt(5-2*np.sqrt(10/7)),-(1/3)*np.sqrt(5-2*np.sqrt(10/7)),(1/3)*np.sqrt(5+2*np.sqrt(10/7)),-(1/3)*np.sqrt(5+2*np.sqrt(10/7))])
  w=np.array([128/225,(322+13*np.sqrt(70))/900,(322+13*np.sqrt(70))/900,(322-13*np.sqrt(70))/900,(322-13*np.sqrt(70))/900])
  return 0.5*(b-a)*np.sum(w*f(0.5*(b-a)*x+0.5*(b+a)))

T= Trap(f,-1,1,20)
S= simpson(f,-1,1,20)
Q= Gauss_quad5(-1,1,f)
print("Comparing the results of trapizoidal rule (n = 20), Simpson’s rule (n = 20)\nand 5-point Gauss quadrature.\n")
print(f"{'Trapazoidal method':<19} | {'Simpson method':<16} | {'Gauss quadrature method'} ")
print("-" * 64)
print(f"{T:<19.2} | {S:<16.2f} | {Q:<16.2f}")
print("-" * 64)


