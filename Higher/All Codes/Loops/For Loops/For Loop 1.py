# Lists of personal information for each individual
firstNames = ['Abi', 'Mia', 'Tom', 'Rose', 'Mike', 'Sophie', 'Miles', 'Will', 'Hayden', 'Fae']
lastNames = ['Smith', 'Parks', 'Kim', 'Walk', 'Ryle', 'Fitz', 'Port', 'Lin', 'Webb', 'Monty']
ages = [24, 45, 16, 37, 72, 31, 60, 43, 46, 48]
favouriteProduct = ['Bread', 'Coffee', 'Gum', 'Eggs', 'Flour', 'Chocolate', 'Yoghurt', 'Juice', 'Tomatoes', 'Cheese']

# Looping through each person based on the length of the firstNames list
for count in range(len(firstNames)):
  # Print a summary for each person with their first name, last name, age, and favourite product
  print(firstNames[count] + " " + lastNames[count] + " is " + str(ages[count]) + "." + 
        " Their favourite product is " + favouriteProduct[count])
