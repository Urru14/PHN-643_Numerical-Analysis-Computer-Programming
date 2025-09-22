import numpy as np
import matplotlib.pyplot as plt

def snells_law(n1, theta1_deg, n2):
    # Convert angle from degrees to radians
    theta1_rad = np.radians(theta1_deg)
    
    # Calculate the sine of the angle of refraction
    sin_theta2 = (n1 / n2) * np.sin(theta1_rad)
    
    # Check for total internal reflection
    if abs(sin_theta2) > 1:
        return None
    
    # Compute the angle of refraction in radians
    theta2_rad = np.arcsin(sin_theta2)
    
    # Convert back to degrees
    theta2_deg = np.degrees(theta2_rad)
    return theta2_deg

def simulate_light_path(initial_angle, n1, n2, num_interfaces):
    
    # Initialize lists to store the coordinates and angles
    x = [0]
    y = [0]
    angles = [initial_angle]
    current_angle = initial_angle
    current_n = n1
    interface_xs = [0]
   
    for i in range(num_interfaces):
        # Update coordinates based on current angle
        print(f"Interface {i+1}:")
        print(f"  Medium with n={current_n}")
        print(f"  Angle of incidence: {current_angle:.2f} degrees")
        
        
            # Light ray is moving in the medium
        x.append(x[-1] + np.cos(np.radians(current_angle)))
        y.append(y[-1] + np.sin(np.radians(current_angle)))
        
        # Compute the angle of refraction
        next_n = n2 if current_n == n1 else n1  # Swap the refractive indices
        refraction_angle = snells_law(current_n, current_angle, next_n)
        
        if refraction_angle is None:
            print("Total internal reflection occurs. The ray does not pass into the next medium.")
            break
        print(f"  Angle of refraction: {refraction_angle:.2f} degrees")
        
        # Update for the next iteration
        current_angle = refraction_angle
        current_n = next_n
        angles.append(current_angle)
        interface_xs.append(x[-1])
        print()  
       
    # Plot the path of the light ray
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    for xi in interface_xs:
        plt.axvline(x=xi, linestyle='--', color='red')
    
    plt.title('Path of Light Ray Through Multiple Mediums')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.show()
initial_angle = float(input("Enter the initial angle in degrees: "))
n1 = 1.5  
n2 = 1.0  
num_interfaces = 5  # Number of interfaces to simulate

simulate_light_path(initial_angle, n1, n2, num_interfaces)

