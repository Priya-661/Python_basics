def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter an integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    print("Factorial of", num, "is", fact)
