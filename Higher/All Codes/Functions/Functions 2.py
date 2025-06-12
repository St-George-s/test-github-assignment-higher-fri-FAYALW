# Function to get the user's name and call the age function

def get_name():
    # Prompt the user to enter their name and store it in myName
    myName = input("Enter your name: ")
    # Call get_age function and assign its return value to myAge
    myAge = get_age()
    # Print the user's age
    print(myAge)
    # Return the user's name for further use
    return myName

# Function to get the user's age
def get_age():
    # Prompt the user to enter their age and store it in myAge
    myAge = input("Enter your age: ")
    # Return the user's age to the calling function
    return myAge
  
# Call get_name function and store the returned name in myName
myName = get_name()
# Print the user's name
print(myName)
