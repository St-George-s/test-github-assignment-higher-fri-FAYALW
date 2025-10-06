# EXAMPLE 2: Validate the length of a name input
len_name = str(input("please enter a name: "))  # Prompt user to enter a name and convert it to a string
# Continue to prompt until the name length is between 2 and 20 characters
while (len(len_name) < 2) or (len(len_name) > 20):
    print("the name must be between 2 and 20 characters, please re-enter")  # Inform user of the valid length
    len_name = str(input("please enter a name: "))  # Prompt user to enter a new name

# EXAMPLE 3: Another method of validating name length (incorrect syntax in original)
name = input("Please enter name: ")  # Prompt user to enter a name
# Check the length of the name and prompt if it's outside the valid range
while (len(name) < 2) or (len(name) > 20):  # Use 'or' for logical operation, corrected from 'OR'
    print("Must be between 2 and 20 characters – please re-enter: ")  # Inform user of the valid length
    name = input("Please enter name: ")  # Prompt user to enter a new name

# EXAMPLE 4: Password confirmation
password = input("Please enter password: ")  # Prompt user to create a password
storedPassword = password  # Store the entered password for confirmation
password = input("Confirm password: ")  # Prompt user to confirm their password
# Check if the confirmed password matches the stored password
if password == storedPassword:  # If the passwords match
    print("Password accepted")  # Inform user that the password is accepted
else:  # If the passwords do not match
    print("Invalid - Passwords don't match")  # Inform user of the mismatch

# EXAMPLE 2 (again): Another validation for name length
name = ""  # Initialize the name variable

name = input("please enter your name")  # Prompt user to enter their name
# Continue to prompt until the name length is between 2 and 20 characters
while len(name) < 2 or len(name) > 20:  # Check for valid name length
    print("your name must be between 2 and 20 characters, please try again")  # Inform user of valid length
    name = input("please enter your name")  # Prompt user to enter a new name

print("thank you")  # Thank the user after valid input

# EXAMPLE 3: (This section is empty in the original code)

# EXAMPLE 4: (This section is already included above)
