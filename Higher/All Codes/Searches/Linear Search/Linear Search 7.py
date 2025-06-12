# A linear search with parallel arrays
# This program searches for an age in a list and prints out the corresponding name and color of the person.

# Initialize parallel arrays for names, ages, and colors
name = ["A", "B", "C", "D", "E"]  # Creates an array called 'name' with 5 elements
age = [32, 43, 12, 87, 9]          # Creates an array called 'age' with corresponding ages
colour = ["green", "brown", "red", "pink", "yellow"]  # Creates an array called 'colour'

# Loop through each index of the name array to print corresponding details
for x in range(len(name)):  # Iterate over all indices of the 'name' array
    # Output the name, age, and color corresponding to the current index
    print(name[x] + " " + str(age[x]) + " " + colour[x])

# Initialize variables for searching
found = False  # Boolean variable to indicate if the age has been found
counter = 0    # Counter to track the current index during the search
get_age = 0    # Variable to store user input for the age to search

# Prompt the user to enter the age they are looking for
get_age = int(input("Enter the age you are looking for: "))  # Store user input as an integer

# While loop to search through the 'age' array
while found == False and counter != len(age):  # Continue looping until the age is found or the end of the array is reached
    if get_age == age[counter]:  # Check if the user's input matches the current age
        found = True  # Set 'found' to True if a match is found
    else:  # If no match is found
        counter += 1  # Increment the counter to check the next element

# Output the result based on whether the age was found
if found == True:  # If the age was found
    # Print the corresponding name and color for the found age
    print(name[counter], colour[counter])
else:  # If the age was not found
    print("No one is that age")  # Inform the user that no one has the entered age
