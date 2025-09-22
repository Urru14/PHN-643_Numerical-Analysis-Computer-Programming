import numpy as np

def calculate_period(length):
   
    g = 9.81  # acceleration due to gravity in m/s²
    period = 2 * np.pi * np.sqrt(length / g)
    return period



print("-" * 30)
print(f"{'Length (m)':<15} {'Period (s)':<15}")
print("-" * 30)


for length in range(1, 11):
    period = calculate_period(length)
    print(f"{length:<15} {period:<15.2f}")
print("-" * 30)    
