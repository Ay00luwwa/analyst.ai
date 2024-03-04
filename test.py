USERS_NAME = ''
USERS_MAT_NO = ''

name = input("What is your name? ")
print(f"Your name is {name}")

matric_number = input("What is your matric number? ")

if matric_number:
    print(f"Your matric number is {matric_number}")

lastdgits = matric_number[-3:]

first_three_letters = name[:3] 

password = lastdgits + first_three_letters.lower()

print(f"your password is {password}")