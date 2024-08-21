def is_armstrong(n):
    sum, count = 0, 0
    temp = n
    while temp > 0:
        digit = temp % 10
        count += 1
        temp //= 10
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp //= 10
    return sum == n

def print_armstrong_in_range(start, end):
    for num in range(start, end + 1):
        if is_armstrong(num):
            print(num, end=" ")
    print()

n = int(input("Enter the number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"{n} is {'a Armstrong number' if is_armstrong(n) else 'Not a Armstrong number'}")
print(f"Armstrong numbers between {start} and {end}:")
print_armstrong_in_range(start, end)
