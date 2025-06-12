# This program collects a user's name, age, and favorite crisps, and provides friendly responses.

myName = ""  # Initialize a variable to store the user's name

print("Enter your name:")  # Prompt the user to input their name
myName = input()  # Capture the user input and assign it to myName
print(myName + " is a nice name!")  # Output a message confirming the user's name
print("      ")  # Print blank space for better readability in the output

myAge = ""  # Initialize a variable to store the user's age

print("Enter your age:")  # Prompt the user to input their age
myAge = input()  # Capture the user input and assign it to myAge
print(myAge + " is my age as well!")  # Output a message indicating shared age
print("      ")  # Print blank space for better readability in the output

myCrisps = ""  # Initialize a variable to store the user's favorite crisps

print("Enter your favorite crisps:")  # Prompt the user to input their favorite crisps
myCrisps = input()  # Capture the user input and assign it to myCrisps
print("I love " + myCrisps + " as well!")  # Output a message confirming shared love for the crisps