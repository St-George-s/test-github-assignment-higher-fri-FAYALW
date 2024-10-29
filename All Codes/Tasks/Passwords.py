# Predefined valid password for suggestions
genPas = "schmoolibooli12345tea56"  

# Prompt the user to enter a password
password1 = input("Please enter a password: ")

# Check if the password is valid:
# 1. Length should be at least 8 characters
# 2. The first character should not be a digit
if len(password1) < 8 or password1[0].isdigit():
    print("Invalid password. Try", genPas, "instead")  # Inform the user if the password is invalid and suggest a valid password
else:
    # If the password is valid, prompt the user to re-enter it
    password2 = input("Password is valid please reenter: ")

    # Check if the two entered passwords match
    if password1 == password2:
        print("Passwords match.")  # Inform the user that the passwords match
    else:
        print("Passwords do not match.")  # Inform the user that the passwords do not match
