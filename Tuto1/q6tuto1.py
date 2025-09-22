"""
     To show 
       1. lim           summation ((-1)^n/n)= -ln2
          N-> infinite
          
       2.  1. lim       summation (1/(n(n+1)))= 2
           N-> infinite
        """
sum1=0
for i in range (1,200):
    a=(-1)**i
    sum1 = sum1 + a/i
    
sum2=0
for i in range (1, 200):
    b= i*(i+1)
    sum2 = sum2 + 1/b
    
print("To Show")    
print ("""lim         summation ((-1)^n/n)= -ln2
N-> infinite
   """)

print ("The calculated value of L.H.S by code is: ", sum1, " which is approximately equal to -ln2")   
print("To Show")    
print ("""lim         summation (1/(n(n+1)))= 2
N-> infinite
   """)

print ("The calculated value of L.H.S by code is: ", sum2, " which is approximately equal to 2")   
