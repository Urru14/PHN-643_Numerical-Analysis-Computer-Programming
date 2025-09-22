#Q4
#Coupling of two angular momentum
import numpy as np
j1= float(input("Enter angular momentum j1: "))
j2= float(input("Enter angular momentum j2: "))
j0= abs(j1-j2)
j3= j1+j2
n= np.arange(j0, j3+1)
print ("The values of j that is |j1-j2| to (j1+j2) are ", n)

