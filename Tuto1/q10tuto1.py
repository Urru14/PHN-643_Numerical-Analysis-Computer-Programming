import numpy as np

def classify_lattice(a1, a2, gamma):
    
    # Convert gamma from degrees to radians for comparison
    gamma_rad = np.radians(gamma)
    
    # Check lattice type based on the given conditions
    if (a1 == a2) and (gamma_rad== np.pi / 2):
        return "Square"
    elif (a1 != a2) and (gamma_rad== np.pi / 2):
        return "Rectangular or centered rectangular depending on effective no. of atom"
    elif (a1 == a2) and (gamma_rad== np.pi *3/ 2):
        return "hexagonal"
    elif (a1 != a2) and (gamma_rad!= np.pi / 2):
        return "Oblique"
    else:
        return "General"

# Input values for edge lengths and angle
a1 = float(input("Enter the length of the first edge (a1): "))
a2 = float(input("Enter the length of the second edge (a2): "))
gamma = float(input("Enter the angle between the edges (γ) in degrees: "))
    
# Classify the lattice
lattice_type = classify_lattice(a1, a2, gamma)
print(f"The type of the lattice is: {lattice_type}")
