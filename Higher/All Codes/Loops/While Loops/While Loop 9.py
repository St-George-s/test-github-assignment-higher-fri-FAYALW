array_names = []  # Initialize an empty list to store names
array_numbers = []  # Initialize an empty list to store numbers

string_name = ''  # Variable to store the user input for name
string_number = ''  # Variable to store the user input for number
int_number = 0  # Variable to store the user input as an integer

# Loop until a valid name is entered
while len(string_name) == 0:  # Check if the name string is empty
    string_name = input("Enter a valid name: ")  # Prompt the user to enter a name
else:
    array_names.append(string_name)  # Append the valid name to the names array

# Infinite loop to continuously ask for a number
while True:  # This creates an infinite loop
    int_number = input("Enter a valid number: ")  # Prompt the user to enter a number
    string_number = str(int_number)  # Convert the input number to a string
    if len(string_number) == 10:  # Check if the length of the string is 10
        array_numbers.append(int_number)  # Append the valid number to the numbers array
        break  # Exit the loop after a valid number is added

# Print the results
print("The Names Array is: ", array_names)  # Display the list of names
print("The Numbers Array is: ", array_numbers)  # Display the list of numbers
