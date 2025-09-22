#Time Period
import math
def Time_period (L):
    g = 9.8
    w = math.sqrt (L/g)
    return (2 * math.pi)*w
l= float(input("Enter the length of Pendulum in meters:"))
T= Time_period (l)
print ("the time period of simple pendulum is %9.2f sec." % T )

