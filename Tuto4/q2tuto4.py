import time
import numpy as np 
def montecarlo1(funx,xmin,xmax,ymin,ymax,m):
    x=np.random.random(m)
    y=np.random.random(m)
    x=x*(xmax-xmin)+xmin
    y=y*(ymax-ymin)+ymin
    n=0
    for i in range(m):
        t = funx(x[i])
        if t>=y[i] and t>0:
            n+=1
        elif t<=y[i] and t<0:
            n-=1
    return (xmax-xmin)*(ymax-ymin)*n/m
#Vectorized
def montecarlo2(funx,xmin,xmax,ymin,ymax,m):
    x=np.random.random(m)
    y=np.random.random(m)
    x=x*(xmax-xmin)+xmin
    y=y*(ymax-ymin)+ymin
    t = funx(x)
    n1=np.sum(np.logical_and(t>=y,y>0))
    n2=np.sum(np.logical_and(t<=y,y<0))
    n=n1-n2
    return (xmax-xmin)*(ymax-ymin)*n/m
start_time1 = time.time()
print(montecarlo1(lambda x: 3*x**2- 5*x+ 7, 0,2,0,10,10000))
end_time1 = time.time()
time_taken1 = end_time1 - start_time1
start_time2 = time.time()
print(montecarlo2(lambda x: 3*x**2- 5*x+ 7 ,0,2, 0,10,10000))
end_time2 = time.time()
time_taken2 = end_time2 - start_time2
print ("Time taken in normal code: ",time_taken1 )
print ("Time taken in vectorized code: ",time_taken2 )
print ("\nBy above values we can conclude that the value of integration on average are same but the time execution is better of Vectorized method.")

