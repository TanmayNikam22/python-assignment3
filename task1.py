def factorial():
    n = int(input("Enter a number"))
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return f"Factorial of {n} is {result}"
print(factorial())
