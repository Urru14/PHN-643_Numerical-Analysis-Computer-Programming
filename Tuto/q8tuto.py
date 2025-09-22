#Escape velocity
import math
def Escape_velocity (M,R):
    G= 6.674e-11
    u= (2*G*M)/R
    v= math.sqrt(u)
    return v
m = float(input("Enter the mass of planet in Kg: "))
r= float (input ("Enetr the radius of planet in meter: "))
vel = Escape_velocity (m,r)
print ("The escape velocity of planet is %9.2f m/s." % vel)

