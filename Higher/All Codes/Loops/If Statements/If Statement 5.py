# Password checker

print("welcome to PGO security systems")  # Print welcome message to the user
print("*******************************")  # Print a decorative line for emphasis
password = input("enter your password: ")  # Prompt the user to enter their password

# Check if the entered password matches the predefined password
if password == "abcd1234":  # If the password is 'abcd1234'...
    print("access granted")  # ...print 'access granted' to indicate successful access
else:  # If the password is anything else...
    print("access denied")  # ...print 'access denied' to indicate failed access

print("press ENTER to exit the program")  # Print instruction for the user to exit the program
