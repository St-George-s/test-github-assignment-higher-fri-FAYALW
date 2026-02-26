# Function to get two numbers from user input
def get_numbers():
    # Prompt the user to enter the first number and store it
    print("Please enter the first number:")
    number1 = input()
    
    # Prompt the user to enter the second number and store it
    print("Please enter the second number:")
    number2 = input()
    
    # Return both numbers
    return number1, number2

# Call `get_numbers` function and store the returned values in separate variables
first_number, second_number = get_numbers()

# Print both returned numbers
print("First number:", first_number)
print("Second number:", second_number)

print("End of program")  # Indicate end of the program