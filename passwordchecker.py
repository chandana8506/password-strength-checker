import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    else:
        print("Password should be at least 8 characters")

    if re.search("[a-z]", password):
        strength += 1
    else:
        print("Add lowercase letters")

    if re.search("[A-Z]", password):
        strength += 1
    else:
        print("Add uppercase letters")

    if re.search("[0-9]", password):
        strength += 1
    else:
        print("Add numbers")

    if re.search("[@#$%^&*]", password):
        strength += 1
    else:
        print("Add special characters")

    if strength == 5:
        print("Strong Password")
    elif strength >= 3:
        print("Medium Password")
    else:
        print("Weak Password")


password = input("Enter your password: ")
check_password_strength(password)