import numpy as np
def calculate_power(vs, rs, RL):
    
    # Calculate the power using the formula
    P = (vs ** 2) * RL / ((RL + rs) ** 2)
    return P


# Constants
vs = 12.0  # Voltage source in volts
rs = 2.5   # Internal resistance in ohms

# Range of load resistance RL from 1 to 10 ohms
RL_values = np.arange(1, 11)  # Array with values from 1 to 10 ohms
power_values = []

# Print the results in tabular form
print(f"{'RL (Ohms)':<10} | {'Power (Watts)':<10}")
print("--------------------------")
for RL in range (1,11):
    P = calculate_power(vs, rs, RL)
    power_values.append(P)
    print(f"{RL:<10} | {P:.2f}")
