def replace_word(rep):
    with open("practice.txt","r") as f:
        data = f.read()
    new_data = data.replace("Java",rep)
    print(new_data)
    with open("practice.txt","w") as f:
        f.write(new_data)

def find_word(word):
    with open("practice.txt","r") as f:
        data = f.read()
        # if(data.find(word) != -1): same as word in data
        if(word in data):
            print("Found")
        else:
            print("not found")

def check_line(word):
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("Line number:",line_no) 
            line_no += 1

def number():
    with open("numbers.txt","w") as f:
       f.write("0,1,2,3,4,5,6,7,8,9")
    count = 0
    with open("numbers.txt","r") as f:
       data = f.read()
    print(data)
    nums = data.split(",")
    for val in nums:
        if(int(val) != 0 and int(val) % 2 == 0):
            count += 1
    print("No. of Even numbers:",count)

word = "learning"
rep="Python"
replace_word(rep)
find_word(word)
check_line(word)
number()