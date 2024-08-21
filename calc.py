def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1/num2

def main():
   while True:    
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print("Enter your choice:\n1. Addition\n2. Subtraction\n3. Mulultiplication\n4. Division \n5. Exit\n")
        choice = int(input())
        if choice == 1:
            Result = add(num1,num2)
            print("Result: ", Result)
        elif choice == 2:
            Result = sub(num1,num2)
            print("Result: ", Result)
        elif choice == 3:
            Result = mul(num1,num2)
            print("Result: ", Result)
        elif choice == 4:
            Result = div(num1,num2)
            print("Result: ", Result)
        elif choice == 5:
            print("Exiting...")
            exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
