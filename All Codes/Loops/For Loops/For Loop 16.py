# Initialize an empty list to store names
names = []  # List to hold names entered by the user

# Initialize variables for user input
get_names = 0  # Placeholder variable for capturing each name input
no_names = 0  # Variable to store the number of names to be entered

# Prompt the user for the number of names they wish to enter
no_names = int(input("How many names are there? "))  # Convert the input to an integer

# Loop to collect names from the user
for x in range(no_names):  # Iterate based on the number of names specified
    get_names = input("Enter a name: ")  # Get a name from the user
    names.append(get_names)  # Append the entered name to the names list

# Print the list of names collected
print(names)  # Output the final list of names
