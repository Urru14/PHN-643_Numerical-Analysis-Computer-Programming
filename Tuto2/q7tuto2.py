import math

def magnetic_field(mu0, I, r):
    
    if r == 0:
        raise ValueError("Distance r cannot be zero.")
    B = (mu0 * I) / (2 * math.pi * r)
    return B


mu0 = 4 * math.pi * 10**-7  
I = 5  # Current (A)

# Distances from the wire
distances = [0.1, 0.5, 1.0, 1.5]  # in meters
print ("-"*30)
print (f"{'Distance (m)':<15} {'Magnetic field (T)':<15}")
print ("-"*30)
for r in distances:
    B = magnetic_field(mu0, I, r)
    print (f"{r:<15} {B:<15.2e}")
print ("-"*30)    

