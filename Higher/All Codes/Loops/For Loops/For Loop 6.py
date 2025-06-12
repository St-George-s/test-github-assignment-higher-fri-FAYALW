# Initialize two empty lists to store names and mobile numbers
name = []  # List to hold names
number = []  # List to hold mobile numbers

# Loop to collect names and mobile numbers from the user
for x in range(3):  # Repeat the following block of code 3 times
    get_name = input("Please enter your name: ")  # Prompt user to enter their name
    
    # Validate that the user has entered a name
    while len(get_name) == 0:  # Check if the length of the entered name is 0 (i.e., it's empty)
        print("Name missing, please re-enter")  # Inform the user that the name is missing
        get_name = input("Please enter your name: ")  # Prompt the user to enter their name again
    
    name.append(get_name)  # Add the valid name to the 'name' list
    
    get_number = input("Please enter your mobile number: ")  # Prompt user to enter their mobile number
    
    # Validate that the mobile number is exactly 11 digits long
    while len(get_number) != 11:  # Check if the length of the entered number is not equal to 11
        print("Number not valid - please re-enter")  # Inform the user that the number is not valid
        get_number = input("Please enter your number: ")  # Prompt the user to enter their number again
    
    number.append(get_number)  # Add the valid mobile number to the 'number' list

# Print the list of names collected from the user
print(name)  # Output the names entered by the user