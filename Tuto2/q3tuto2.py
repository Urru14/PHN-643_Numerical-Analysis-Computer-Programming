def celsius_to_fahrenheit(C):
    return (9 / 5) * C + 32

def fahrenheit_to_celsius(F):
    return (5 / 9) * (F - 32)


print("Celsius to Fahrenheit")
print(f"{'Celsius':<10} {'Fahrenheit':<10}")
print("-" * 20)
for celsius in range(0, 101, 5):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:<10.2f} {fahrenheit:<10.2f}")
print("-" * 20)
print("\nFahrenheit to Celsius")
print(f"{'Fahrenheit':<10} {'Celsius':<10}")
print("-" * 20)
for fahrenheit in range(0, 101, 5):
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit:<10.2f} {celsius:<10.2f}")
print("-" * 20)
