def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(limit):
    n = 0
    while True:
        fib = fibonacci(n)
        if fib > limit:
            break
        print(fib, end=" ")
        n += 1

limit = int(input("Enter the limit: "))
print_fibonacci_series(limit)
