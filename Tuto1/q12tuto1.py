import numpy as np

def compute_statistics(arr):
    
    
    arr = np.array(arr)
    
    
    maximum = np.max(arr)
    minimum = np.min(arr)
    average = np.mean(arr)
    std_deviation = np.std(arr)
    median = np.median(arr)
    total_sum = np.sum(arr)
    product = np.prod(arr)

    # Return results as a dictionary
    return {
        'maximum': maximum,
        'minimum': minimum,
        'average': average,
        'std_deviation': std_deviation,
        'median': median,
        'sum': total_sum,
        'product': product
    }


# Input: Read the number of elements and the array
n = int(input("Enter the number of elements: "))
print(f"Enter {n} numbers separated by spaces:")
arr = list(map(float, input().split()))

# Validate input length
if len(arr) != n:
   print("The number of entered elements does not match the specified count.")


# Compute and display statistics
stats = compute_statistics(arr)
print("\nComputed Statistics:")
print(f"Maximum: {stats['maximum']:.2f}")
print(f"Minimum: {stats['minimum']:.2f}")
print(f"Average: {stats['average']:.2f}")
print(f"Standard Deviation: {stats['std_deviation']:.2f}")
print(f"Median: {stats['median']:.2f}")
print(f"Sum: {stats['sum']:.2f}")
print(f"Product: {stats['product']:.2f}")

