import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function for i in range(n)]
# password = "".join([random.choice(charValues) for i in range(pass_len)])
password = ""
for i in range(pass_len):
     password += random.choice(charValues)

print("Random Password: ",password)
