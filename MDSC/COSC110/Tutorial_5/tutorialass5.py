def factorial(n):
    result = 1
    while n != 0:
        result = result * n
        n = n - 1 
    return result
# Calculate factorial for the first four integers
for i in range(5):
  print(f'Factorial of {i} is {factorial(i)}')

