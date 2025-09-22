def distance (v,t,a):
    d = v*t + 0.5*a* t**2
    return d
u= float(input("Enter initial velocity (m/s): "))
t= float(input("Enter time (s): "))
a= float(input("Enter acceleration (m/s^2): "))
d1= distance (u,t,a)
print ("The distance travelled is %9.2f  meters. " %d1)

