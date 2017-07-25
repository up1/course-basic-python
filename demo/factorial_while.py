def factorial(n, sum = 1):
    while True:
        if n <= 1:
            return sum
        n, sum = n - 1, sum * n


print(factorial(5000))
