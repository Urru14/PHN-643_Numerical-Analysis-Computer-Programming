import numpy as np

L=1
def Func(x, L):
    return np.sin(np.pi*x/L)**2
def montecarlo(a, b, f, m):
    L=1
    x = np.random.uniform(a,b,m)
    return (b-a)*np.mean(f(x,L))

I= montecarlo(0,L,Func,10000)
print ("Let the integral sin^2(πx/L) be calculated first by Montecarlo method as A^2 is constant.")
print (f"Now on calculating integral value is {I}.")
print (f"Thus A^2*sin^2(πx/L) is equal to {I}.")
P= 1/np.sqrt(I)
print (f"Therefor value of A is {P}.")
E= abs(np.sqrt(2)-P)
print ("Error in given value of A and calculted equal to", E)
