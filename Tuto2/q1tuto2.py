import math
import matplotlib.pyplot as plt 
# Constants
v0 = 20  
theta = 30  
g = 9.81  


theta_rad = math.radians(theta)


v0_x = v0 * math.cos(theta_rad)
v0_y = v0 * math.sin(theta_rad)
x1=[]
y1=[]
delta_t = 0.1


t = 0
print ("-"*45)
print(f"{'Time in sec':<15} {'X in m':<15} {'Y in m':<15}" )
print ("-"*45)

while True:
    
    x = v0_x * t
    y = v0_y * t - 0.5 * g * t**2
    
    
    if y < 0:
        break
    x1.append(x)
    y1.append(y)
   
    print(f"{t:<14.2f}   {x:<14.2f}   {y:<14.2f} ")
    
    t += delta_t

print ("-"*45)
plt.plot(x1,y1,ls=':',label='Projectile motion' , color = 'magenta',linewidth= 2)
plt.xlabel('Range')
plt.ylabel('Height')
plt.legend()
plt.show()
