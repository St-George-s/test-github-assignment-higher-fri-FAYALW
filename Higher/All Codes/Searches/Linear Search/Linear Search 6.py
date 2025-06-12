# Linear search with parallel arrays
# This program identifies the name and shoe size of a person by their age,
# finds the shoe size and age of a person by their name, and finds the name
# and age of a person based on their shoe size.

# Initialize parallel arrays for names, shoe sizes, and ages
name = ["A", "B", "C", "D", "E", "F", "G"]  # Array of names
shoesize = [3, 12, 8, 4, 10, 1, 9]           # Corresponding array of shoe sizes
age = [23, 56, 12, 99, 10, 13, 61]           # Corresponding array of ages

# Search for the name and shoe size of the person who is 99 years old
found = False  # Boolean variable to track if the age has been found
counter = 0    # Initialize counter to iterate through the age array
get_age = int(input("Enter the age you are looking for: "))  # User input for age to search

# Loop through the age array until the age is found or end of array is reached
while found == False and counter != len(age):
    if get_age == age[counter]:  # Check if the input age matches the current age in the array
        found = True  # Set found to True if the age matches
    else:
        counter += 1  # Increment counter to check the next element

# Output the corresponding shoe size and name for the found age
print("The person who is " + str(get_age) + " has a shoe size of " + str(shoesize[counter]) + " and their name is " + name[counter])

# Search for the shoe size and age of person "F"
found = False  # Reset found variable for the next search
counter = 0    # Reset counter for name search
get_name = input("Enter the name you are looking for: ")  # User input for name to search

# Loop through the name array until the name is found or end of array is reached
while found == False and counter != len(name):
    if get_name == name[counter]:  # Check if the input name matches the current name in the array
        found = True  # Set found to True if the name matches
    else:
        counter += 1  # Increment counter to check the next element

# Output the corresponding shoe size and age for the found name
print("The person who is called " + get_name + " has a shoe size of " + str(shoesize[counter]) + " and their age is " + str(age[counter]))

# Search for the name and age of the person with size 8 feet
found = False  # Reset found variable for the next search
counter = 0    # Reset counter for shoe size search
get_shoesize = int(input("Enter the shoe size you are looking for: "))  # User input for shoe size to search

# Loop through the shoe size array until the shoe size is found or end of array is reached
while found == False and counter != len(shoesize):
    if get_shoesize == shoesize[counter]:  # Check if the input shoe size matches the current size in the array
        found = True  # Set found to True if the shoe size matches
    else:
        counter += 1  # Increment counter to check the next element

# Check if the shoe size was found and output the corresponding name and age
if found == True:
    print("The person who has a shoe size of " + str(get_shoesize) + " is called " + name[counter] + " and their age is " + str(age[counter]))
else:
    print("Not found")  # Output if the shoe size was not found
