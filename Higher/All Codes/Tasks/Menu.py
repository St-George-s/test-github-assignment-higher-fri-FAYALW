# Define a menu as a dictionary, where each item has a price and a vegetarian/non-vegetarian indicator
menu = {
    "Stir Fry": [7.55, "V"],          # Price is 7.55, vegetarian
    "Fajitas": [6.85, "NV"],         # Price is 6.85, non-vegetarian
    "Halloumi Fries": [3.55, "V"],   # Price is 3.55, vegetarian
    "T-Bone Steak": [19.99, "NV"],   # Price is 19.99, non-vegetarian
    "Toad In The Hole": [8.99, "NV"], # Price is 8.99, non-vegetarian
    "Veg Lasagne": [7.25, "V"],      # Price is 7.25, vegetarian
    "Borscht": [5.99, "NV"]          # Price is 5.99, non-vegetarian
}

# Print the full menu with prices
for key, value in menu.items():  # Iterate over each item in the menu dictionary
    # Print the menu item name and its price
    print(key, "£" + str(value[0]))  # Access the price from the value list and convert it to string for display

# Ask the user if they want to see vegetarian options
vegOrNo = input("Would you like to see the vegetarian options? Y or N: ")

if vegOrNo == "Y":  # If user inputs 'Y', show vegetarian options
    for key, value in menu.items():  # Iterate over each item in the menu
        if value[1] == "V":  # Check if the item is vegetarian
            print(key, "£" + str(value[0]))  # Print the vegetarian item and its price
else:  # If user does not want vegetarian options
    for key, value in menu.items():  # Iterate over each item in the menu
        if value[1] == "NV":  # Check if the item is non-vegetarian
            print(key, "£" + str(value[0]))  # Print the non-vegetarian item and its price

# Ask the user if they want to set a price limit
priceFilter = input("Would you like to set a price limit? Y or N: ")
if priceFilter == "Y":  # If user inputs 'Y', ask for price limit
    priceLimit = float(input("Enter your price limit: "))  # Get the price limit from the user
    for key, value in menu.items():  # Iterate over each item in the menu
        if value[0] <= priceLimit:  # Check if the item's price is within the limit
            print(key, "£" + str(value[0]))  # Print the item name and price if it meets the limit
else:  # If user does not want to set a price limit
    print("Ok")  # Inform the user that no price limit will be applied
