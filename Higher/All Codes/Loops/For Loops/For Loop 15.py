# Initialize empty lists for names and sizes
names = []  # List to store names
sizes = []  # List to store shoe sizes

# Initialize variables for user input
get_names = 0  # Placeholder for the name input
no_names = 0  # Number of names to be entered
get_sizes = 0  # Placeholder for the shoe size input
no_sizes = 0  # Number of shoe sizes to be entered
total = 0  # Variable to accumulate the total of shoe sizes

# Prompt user for the number of names and shoe sizes to be entered
no_names = int(input("How many names are there? "))  # Get the count of names
no_sizes = int(input("How many shoe sizes? "))  # Get the count of shoe sizes

# Loop to collect names from user
for x in range(no_names):  # Iterate for the number of names specified
    get_names = input("Enter a name: ")  # Get a name from the user
    names.append(get_names)  # Append the name to the names list

# Loop to collect shoe sizes from user
for x in range(no_sizes):  # Iterate for the number of sizes specified
    get_sizes = int(input("Enter a shoe size: "))  # Get a shoe size from the user
    sizes.append(get_sizes)  # Append the shoe size to the sizes list

# Print the collected names and sizes
print(names)  # Output the list of names
print(sizes)  # Output the list of shoe sizes

# Calculate the average shoe size
for y in range(5):  # Loop through the first five shoe sizes
    total = total + sizes[y]  # Add each shoe size to the total

# Print the average shoe size
print(total / 5)  # Output the average by dividing the total by 5
