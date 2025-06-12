# List of user names, PINs, and balances
user_names = ['John', 'Alice', 'Bob', 'Emily', 'Michael', 'Sarah', 'David', 'Laura', 'James', 'Emma']  
user_pins = [1234, 5678, 9101, 1121, 3141, 5161, 7181, 9202, 1222, 3242]  
user_balances = [100, 350, 500, 420, 600, 230, 390, 120, 310, 470]  

# Prompt user to enter their name
print("Please enter your name: ")  

# Check if the entered name matches any in the user_names list
if input == user_names:  # This condition is incorrect; it should compare the input with each element
    print("Please enter your pin")  # If the name is found, ask for the PIN
else:
    print("Try again")  # If not found, prompt to try again

# Check if the entered PIN matches any in the user_pins list
if input == user_pins:  # This condition is incorrect; it should compare the input with each element
    print("Please enter your balance")  # If the PIN is correct, ask for the balance
else:
    print("Try again")  # If not, prompt to try again

# Check if the entered balance matches any in the user_balances list
if input == user_balances:  # This condition is incorrect; it should compare the input with each element
    print("Access granted")  # If the balance is correct, grant access
else:
    print("Try again")  # If not, prompt to try again
