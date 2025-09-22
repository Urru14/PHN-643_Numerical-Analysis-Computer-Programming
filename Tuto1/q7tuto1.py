def cons_sum(n):
    # Using integer division to ensure the result is an integer
    return (n * (n + 1)) / 2

sum1 = 0
n = int(input("Enter the value of n up to which you want the consecutive sum: "))

# Calculating the sum of the first n positive integers using a loop
for i in range(1, n + 1):
    sum1 += i

# Calculating the sum using the formula
sum2 = cons_sum(n)

# Printing the results
print("Sum calculated using the loop: ", sum1)
print("Sum calculated using the formula: ", sum2)

