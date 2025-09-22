import math

def calculate_modes(n1, n2, D, wavelength):
    
    NA = math.sqrt(n1**2 - n2**2)
    
    # Calculate the number of modes
    Nm = 0.5 * (math.pi * D * NA / wavelength) 
    
    return Nm

# Example values

n1 = float(input("Enter the refractive index of the core: "))
n2 = float(input("Enter the refractive index of the cladding: "))
D =float(input("Enter the core diameter in micrometers: "))
wavelength = float(input("Enter the wavelength of ligth in mircometers: "))
if n1<= n2 :
    raise ValueError("n1 should be large than n2 (n1>n2).")


modes = calculate_modes(n1, n2, D, wavelength)


print(f"Number of modes: {modes:.2f}")

