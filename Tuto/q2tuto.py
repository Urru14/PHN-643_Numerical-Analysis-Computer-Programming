def kinetic_energy (m,v):
    return ( 0.5*m*v )
m= float (input("Enter masss of the object (kg): "))
v= float (input ("Enter velocity of the object (m/s): "))
k= kinetic_energy (m,v)
print ("The K.E of the object is %9.2f (kgm^2/s^2)" % k)

