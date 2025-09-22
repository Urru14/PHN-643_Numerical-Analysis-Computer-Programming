import numpy as np

def calculate_angles(a, b, c):
    """Calculate the angles of a triangle given sides a, b, and c."""
    # Ensure sides are positive and form a valid triangle
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")

    # Using the Law of Cosines to find angles in radians
    angle_A = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))
    angle_B = np.arccos((a**2 + c**2 - b**2) / (2 * a * c))
    angle_C = np.arccos((a**2 + b**2 - c**2) / (2 * a * b))

    # Convert angles from radians to degrees
    angle_A_deg = np.degrees(angle_A)
    angle_B_deg = np.degrees(angle_B)
    angle_C_deg = np.degrees(angle_C)

    return angle_A_deg, angle_B_deg, angle_C_deg

# Input lengths of the sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
angles = calculate_angles(a, b, c)
print("The angles of the triangle are:")
print(f"Angle A: {angles[0]:.2f} degrees")
print(f"Angle B: {angles[1]:.2f} degrees")
print(f"Angle C: {angles[2]:.2f} degrees")
