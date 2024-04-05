def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Taking input from the user
number = int(input("Enter an integer: "))

# Checking if the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculating factorial
    result = factorial(number)
    print("The factorial of", number, "is:", result)