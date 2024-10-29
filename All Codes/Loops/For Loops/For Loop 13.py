# Lists to hold first names, last names, ages, and favorite products
firstNames = ['Abi', 'Mia', 'Tom', 'Rose', 'Mike', 'Sophie', 'Miles', 'Will', 'Hayden', 'Fae']  # List of first names
lastNames = ['Smith', 'Parks', 'Kim', 'Walk', 'Ryle', 'Fitz', 'Port', 'Lin', 'Webb', 'Monty']  # List of last names
ages = [24, 45, 16, 37, 72, 31, 60, 43, 46, 48]  # List of corresponding ages
favouriteProduct = ['Bread', 'Coffee', 'Gum', 'Eggs', 'Flour', 'Chocolate', 'Yoghurt', 'Juice', 'Tomatoes', 'Cheese']  # List of favorite products

# Loop through the range of the length of the firstNames list
for count in range(len(firstNames)):
    # Construct a string that includes the full name, age, and favorite product for each individual
    print(firstNames[count] + lastNames[count] + " is " + str(ages[count]) + "." + " Their favourite product is " + favouriteProduct[count])
