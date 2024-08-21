n = int(input("Enter the number: "))

def decimalToBinary(n):
    if(n > 1):
        decimalToBinary(n // 2)
    print(n % 2, end = " ")

def decimalToOctal(n):
    if(n > 1):
        decimalToOctal(n // 8)
    print(n % 8, end = " ")

decimalToBinary(n)
print()
decimalToOctal(n)
