import numpy as np
import matplotlib.pyplot as plt

def RK2_method(f,x0,y0,xn,n):
    h=(xn-x0)/float(n)
    x=np.arange(x0,xn+h,h)
    y0=np.array(y0)
    y=y0.reshape(1,len(y0))
    for i in range(1, n + 1):
         k1= h*f(x[i-1],y[i-1])
         k2= h*f(x[i-1] + h/2,y[i-1] + k1/2)
         y=np.append(y,[y[i-1] + k2]).reshape(i+1,len(y0))
    return x,y
def f(t,x):
    mu = 1
    f0= x[1]
    f1= mu*(1-x[0]**2)*x[1]- x[0]
    return np.array([f0,f1])
T,X = RK2_method(f,0,[0.5,0],2,20)

#print (X)
X= np.swapaxes(X,0,-1)
#print (X)
plt.plot(X[0], X[1], label='RK-2', color='red', linestyle='--')
