import matplotlib.pyplot as plt
import numpy as np

def sinc(x):
    #np.where(condition, true_value, false_value)
    return np.where(x != 0, np.sin(np.pi * x) / (np.pi * x), 1)

# Parameters
I0 = float(input("Enter the value of I0: "))  # Input for I0
lambda_ = float(input("Enter the value of λ (in meters): "))  # Input for λ
d = float(input("Enter the value of d (slit width, in meters): "))  # Input for d
theta_values = np.linspace(-np.pi / 2, np.pi / 2, 1000)  # Range of θ from -90° to 90°

# Calculate intensity values
sinc_argument = (d / lambda_) * np.sin(theta_values)
I_values = I0 * sinc(sinc_argument)**2

output_data = np.column_stack((theta_values, I_values))

with open('intensity_profile.txt', 'w') as f:
    f.write(f"{'-' * 24}\n")
    f.write(f"{'θ (radians)':^14} | {'I(θ)'}\n")
    f.write(f"{'-' * 24}\n")
    for row in output_data:
        f.write(f"{row[0]:14.6f} | {row[1]:.6f}\n")

print("Intensity profile written to 'intensity_profile.txt'")
plt.plot(theta_values,I_values)
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel('Intensity')
plt.title(r'$\theta$ V/s Intensity Plot')
plt.show()
