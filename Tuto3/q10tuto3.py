import numpy as np
#Function defination
def f(x):
    return 3 * x**5 + 2 * x**3
exact = 0.00

#Trapezoidal integation
def Trap(func, a, b,n):
  h = (b - a) / n
  sum=0
  for i in range(n):
    sum += (h/2)*(func(a+i*h)+func(a+(i+1)*h))
  return sum,n
    

#Simpson integration
def simpson(f, a, b,n):
  if n % 2:
   raise ValueError("n must be even (received n=%d)" % n)
  h = (b - a) / n
  s = f(a) + f(b)
  for i in range(1, n, 2):
    s += 4 * f(a + i * h)
  for i in range(2, n-1, 2):
    s += 2 * f(a + i * h)
  return s * h / 3,n
  
  
n = range (1,50,1)
p = range (2,50,2)
T= [Trap(f,-1,1,n1) for n1 in n]
S= [simpson(f,-1,1,n1) for n1 in p]
T = np.round(T, 2)
S = np.round(S, 2)

T = np.swapaxes(T,0,-1)
tx, ty = T
l1= len(tx)
S = np.swapaxes(S,0,-1)
sx, sy = S
l2= len(sx)
print ("\nThe values for Trapezoidal method are as follow, first row in integration value\nand second row is no. of n.")
print (T)
print ("\nThe values for Simpson method are as follow, first row in integration value\nand second row is no. of n.")
print (S)
print ("\nExact value for given integration is 0.00")
print ("\nFor trapezoidal Method:")
for i in range (l1):    
    if (tx[i]== exact):
        print ("The value matched is",tx[i])
        print ("With n = ",ty[i])
        break
    else :    
        print ("No value matched with the exact value in 100th itteration.")
        break
for i in range (l1):    
    if (abs(tx[i]-exact) == 0.1):
        print ("But approximately value near to the exact value is", tx[i], "for n ", i)
        break
print ("\nFor Simpson Method:")    
for i in range (l2):    
    if (sx[i]== exact):
        print ("The value matched is",sx[i])
        print ("With n = ",sy[i])
        break
    else :    
        print ("No value matched with the exact value in 50 itteration")
        break


