# A program to demonstrate a linear search

found = False  # Initialize a boolean variable to track whether the name has been found
name = ["Bob", "James", "Sue", "Sally", "Kevin", "Louise", "Cameron", "Caroline"]  # Create a list of names
get_name = 0  # Initialize a variable to store the user's input (initially set to 0, though this will be overwritten)
pos = 0  # Initialize a variable to keep track of the current position in the list

# Ask the user to enter the name they are looking for
print("Please enter the name you are looking for:")  # Prompt the user for input
get_name = str(input())  # Store the user's input in the variable get_name

# Start a loop that continues until the name is found or we have checked all names
while found == False and pos != len(name):  # Loop as long as 'found' is False and 'pos' is less than the length of the list
    if name[pos] == get_name:  # Check if the current name at position 'pos' matches the user's input
        found = True  # If a match is found, set 'found' to True
    else: 
        pos = pos + 1  # If not found, increment 'pos' to check the next name

# Check if the name was found and print the appropriate message
if found == True:  # If the name was found...
    print("The name was found")  # ... print that it was found
else:
    print("The name was not found")  # If not found, print that it was not found
