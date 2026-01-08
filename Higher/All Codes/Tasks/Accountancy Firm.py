# Prompt the user for their middle name and store the input in the variable 'middleName'
middleName = input("What is your middle name? ")

# Prompt the user for their favorite type of pasta and store the input in the variable 'favePasta'
favePasta = input("What is your favourite type of pasta? ")

# Prompt the user for a random number and store the input in the variable 'ranNum'
ranNum = input("Enter a number ")

# Prompt the user for a symbol character and store the input in the variable 'symChar'
symChar = input("Enter a symbol character ")

# Create a password by concatenating the user's middle name, favorite pasta, random number, and symbol character
password = (middleName + favePasta + ranNum + symChar)

# Print the suggested password to the user
print("Your suggested password is", password)
