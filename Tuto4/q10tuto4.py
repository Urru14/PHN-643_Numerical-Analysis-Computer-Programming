import numpy as np
import matplotlib.pyplot as plt

def RK2_method(f,x0,y0,xn,n,c):
    h=(xn-x0)/float(n)
    x=np.arange(x0,xn+h,h)
    y0=np.array(y0)
    y=y0.reshape(1,len(y0))
    for i in range(1, len(x)):
         k1= h*f(x[i-1],y[i-1],c)
         k2= h*f(x[i-1] + h/2,y[i-1] + k1/2,c)
         k3= h*f(x[i-1] + h/2,y[i-1] + k2/2,c)
         k4= h*f(x[i-1] + h,y[i-1] + k3,c)
         y=np.append(y,[y[i-1] + k1/6 +k2/3 + k3/3+ k4/6]).reshape(i+1,len(y0))
    return x,y
def forcing_func(t):
    return 0

def f(t,x,c):
    m = 1
    k=10
    f0= x[1]
    f1= (forcing_func(t)- c*x[1]-k*x[0])/m
    return np.array([f0,f1])

T1,X1 = RK2_method(f,0,[1.0,0.0],20,100,0)
T2,X2 = RK2_method(f,0,[1.0,0.0],20,100,1)
T3,X3 = RK2_method(f,0,[1.0,0.0],20,100,10)
X1= np.swapaxes(X1,0,-1)
X2= np.swapaxes(X2,0,-1)
X3= np.swapaxes(X3,0,-1)
plt.subplot(2, 2, 1)
plt.plot(T1,X1[0], label='c=0')
plt.xlabel('Time (t)')
plt.ylabel('Displacement (x)')
plt.legend()
plt.subplot(2, 2, 2)
plt.plot(T2,X2[0],label='c=1')
plt.xlabel('Time (t)')
plt.ylabel('Displacement (x)')
plt.legend()
plt.subplot(2, 2, 3)
plt.plot(T3,X3[0],label='c=10')
plt.xlabel('Time (t)')
plt.ylabel('Displacement (x)')
plt.legend()
plt.suptitle("Displacement vs. Time for Different Damping Coefficients", fontsize=16)
plt.tight_layout()

plt.show()
