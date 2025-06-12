# Lists to store user names, pins, and balances
user_names = ['John', 'Alice', 'Bob', 'Emily', 'Michael', 'Sarah', 'David', 'Laura', 'James', 'Emma']
user_pins = [1234, 5678, 9101, 1121, 3141, 5161, 7181, 9202, 1222, 3242]
user_balances = [100, 350, 500, 420, 600, 230, 390, 120, 310, 470]

# Initialize a counter to track the index of the user being checked
counter = 0
# A flag to indicate whether the user has been found
Found = False

# Prompt the user to enter their first name and PIN
get_name = input("Enter First Name: ")
get_pin = int(input("Enter pin: "))

# Loop until the user is found or all users have been checked
while Found == False and counter != len(user_names):
    # Check if the current user name matches the entered name
    if user_names[counter] == get_name:
        # If the name matches, check if the corresponding PIN is correct
        if user_pins[counter] == get_pin:
            # If both name and PIN match, set Found to True
            Found = True
        else:
            # If the PIN is incorrect, inform the user and prompt them to enter the details again
            print("Username and Pin Incorrect")
            counter = counter + 1  # Move to the next user
            get_name = input("Enter First Name: ")  # Ask for the name again
            get_pin = int(input("Enter pin: "))  # Ask for the PIN again (converted to int)
    else:
        # If the name does not match, move to the next user in the list
        counter = counter + 1

# If the loop completes with Found being True, print a welcome message
print("Welcome")
