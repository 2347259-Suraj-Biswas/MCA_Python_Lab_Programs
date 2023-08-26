# Q1. Write a program using the Regular Exception and create a function that accepts a string and searches it for a valid phone number.
# Return the phone number if found.
# A valid phone number may be one of the following:
# (xxx)-xxx-xxxx
# xxx-xxx-xxxx


import re

def search_string(str_number):
    phone_regex = "(\(\d\d\d\)|\d\d\d)\-\d\d\d\-\d\d\d$"
    match = re.search(phone_regex, str_number)
    return match

str1 = "My phone number is (234)-456-879"
str2 = "My phone number is 234-456-879"

result1 = search_string(str1)
result2 = search_string(str2)

print("Output:")
print(result1)
print(result2)


# Q2. Write a function that employs regular expressions to ensure the password given to the function is strong.
# A strong password is defined as follows:
# ·       at least eight characters long
# ·       contains one uppercase character
# ·       contains one lowercase character
# ·       has at least one digit
# ·       has at least one special character

import re

def is_strong_pass(password):
    # At least eight characters long
    if len(password) < 8:
        return False
    
    # Contains one uppercase character
    if not re.search(r'[A-Z]', password):
        return False
    
    # Contains one lowercase character
    if not re.search(r'[a-z]', password):
        return False
    
    # Contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Contains at least one special character
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?\\\'"~-]', password):
        return False
    
    return True


password = input("Enter a password: ")
if is_strong_pass(password):
    print("Password is strong!")
else:
    print("Password is not strong.")

