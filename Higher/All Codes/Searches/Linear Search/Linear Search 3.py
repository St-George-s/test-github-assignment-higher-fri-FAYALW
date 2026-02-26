# A program to demonstrate a linear search

# Create a list of names to search from
get_name = ['Gabriella', 'Ariana', 'Jenna']  
# Create a corresponding list of phone numbers associated with the names
get_number = ['5506783472', '9182936574', '3091836273']  
get_name = 0  # Initialize a variable to hold user input; this variable will be overwritten
pos = 0  # Initialize a variable to track the current position in the lists (currently unused)

# Prompt the user to enter the name they are looking for
print("Please enter the name you are looking for")  
get_name = str(input())  # Store the user's input as a string in the variable get_name

# Print the entered name and the list of numbers (the current code does not perform a search)
print(get_name, get_number)  
