# Import the random module to generate random numbers
import random

# Define a function to generate a username based on a first and last name
def generateUsername(firstName, lastName):
    # Extract the first three letters of the first name
    firstName = firstName[:3]
    # Extract the first three letters of the last name
    lastName = lastName[:3]
    # Generate a random number between 100 and 999
    randomNumber = random.randint(100, 999)
    # Concatenate the parts to form the username and return it
    return firstName + lastName + str(randomNumber)

# Main program
# Prompt the user to enter their first name
firstName = input("What is your first name? ")
# Prompt the user to enter their last name
lastName = input("What is your last name? ")

# Call the function to generate a username using the provided names
username = generateUsername(firstName, lastName)

# Print the generated username
print(username)