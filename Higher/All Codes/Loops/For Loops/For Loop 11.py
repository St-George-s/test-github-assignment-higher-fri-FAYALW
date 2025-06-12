# Initial arrays to hold car makes and their corresponding colours
carmake = ["Ford", "Vauxhall", "BMW", "Mercedes", "Audi"]  # List of car makes
colour = ["Red", "Blue", "Black", "White", "Silver"]  # List of corresponding car colours

# Add a new car make and colour
new_make = input("Enter a new car make: ")  # Prompt the user to enter a new car make
new_colour = input("Enter the corresponding colour: ")  # Prompt the user to enter the colour for the new car make

# Append the new make and colour to the respective lists
carmake.append(new_make)  # Add the new car make to the carmake list
colour.append(new_colour)  # Add the corresponding colour to the colour list

# Implement linear search to find the colour of a specific car make
search_make = input("Enter a car make to search for: ")  # Ask the user for a car make to search

found = False  # Initialize a variable to track if the car make is found
for i in range(len(carmake)):  # Iterate through the list of car makes
    if carmake[i].lower() == search_make.lower():  # Check if the current car make matches the search input (case insensitive)
        found = True  # Set found to True if a match is found
        print(f"The colour of {carmake[i]} is {colour[i]}.")  # Print the corresponding colour of the found car make

# If the car make was not found, inform the user
if not found:
    print(f"Sorry, {search_make} not found in the list.")  # Inform the user if the car make was not found

# Display updated arrays of car makes and colours
print("\nUpdated Car Makes:", carmake)  # Print the updated list of car makes
print("Updated Colours:", colour)  # Print the updated list of corresponding colours
