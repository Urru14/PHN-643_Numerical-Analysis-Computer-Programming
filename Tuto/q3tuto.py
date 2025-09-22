def gravitational_force (m1 ,m2, r):
    G= 6.674e-11
    return (( G*m1*m2)/r**2)
m1 = float(input("Enter mass of the body 1 in kg: "))
m2 = float (input("Enter mass of the boady 2 in kg: "))
r = float (input("Enter distance between two bodies: "))
F = gravitational_force (m1,m2,r)
print ("The Gravitational force acting between two bodies in  kg m/s^2 is ", F)


