import re
name= input("enter your name")
if re.fullmatch(r"[ A-Za-z\.]+",name):
    print("valid name using first name")
else :
    print("it is not valid name")

email = input("Enter your email: ")
if re.fullmatch('[A-Za-z0-9{10}]*@(gmail|yahoo|outlook){1}.com{1}',email):
    print("Valid email")
else:
    print("Invalid email")

phone = input("Enter your phone number: ")
if re.fullmatch(r"[6-9][0-9]{9}", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
password = input("Enter password: ")
if re.fullmatch(r"[A-Za-z0-9 \.W]{6}", password):
    print(" Valid password (letters and numbers only)")
else:
    print("Use only letters and numbers (min 6 characters)")

    
