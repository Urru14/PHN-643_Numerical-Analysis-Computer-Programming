
import math
def factorial (n):
    
    fact = 1
    for i in range (1,n+1):
       fact = fact *i
    return (fact)

def cos (x):
    sum_1=0
    for m in range (51):
        f= factorial (2*m)
        p= x**(2*m)
        s= (-1)**m
        sum_1  = sum_1 +  (s*p)/f
    return sum_1

def sin (x):
    sum_2=0
    for m in range (51):
      f = factorial ((2*m)+1)
      p= x**((2*m)+1)
      s= (-1)**m
      sum_2 = sum_2 + (s*p)/f
    return sum_2

print ("Let's see what will be value by function defining of cosx and sinx and by importing it.")
print ("Let the value of x be pi/2")
a = math.pi/2
b = cos (a)
c= sin(a)
d= math.sin(a)
e= math.cos(a)
print ("The value of cosx by function defition is: ", b)
print ("The value of cosx by import math is: ", e)
print ("The value of sinx by function definition is: ", c)
print ("The value of sinx by import math is: ", d)

print ("The relative error in cosx is: ", e-b)
print ("The relative error in sinx is: ", d-c)



