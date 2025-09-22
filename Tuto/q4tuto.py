#Function to calculate the horizontal distance travelled by projectile launched
import math
def Horizontal_d (v0, t):
    g= 9.8
    return (v0**2 * math.sin(2*t))/g
v= float(input("Enter the initial velocity (m/s): "))
d= float(input("Enter the angle in degree: "))
r= d * (math.pi/180)               # math.radians(d)
R= Horizontal_d (v,r)
print ( "The horizontal distance is %9.3f meters. " % R)



