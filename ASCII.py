ch = input("Enter a character: ")

for i in range(0, 128):
    if ord(ch) == i:
        print(f"The ASCII value of '{ch}' is {i}")
        break 
