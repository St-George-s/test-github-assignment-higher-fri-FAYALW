# Function to get the username from the user
def getUsername():  # No parameters are passed in, so the function does not require data in brackets
    # Prompt the user to input their username
    username = input("What is your username? ")  
    # Return the entered username
    return username

# Function to get the user's age, requiring the username for context
def getAge(getUsername):
    # Prompt the user for their age, including their username for personalization
    age = input(getUsername + " what is your age ")
    # Return the entered age
    return age

# Function to get a list of hobbies from the user
def getHobbies(getUsername):
    # Initialize an empty list to store hobbies
    hobbiesList = []
    # Loop to collect up to 10 hobbies from the user
    for x in range(10):
        # Append each hobby inputted by the user to the hobbies list
        hobbiesList.append(input("Input a hobby "))
    # Return the list of hobbies
    return hobbiesList

# Function to count the number of hobbies in the list
def countHobbies(hobbies):
    # Return the length of the hobbies list, representing the number of hobbies
    return len(hobbies)

# Main program execution starts here
# Get the username by calling the getUsername function
username = getUsername()
# Print the username to the console
print(username)

# Get the user's age using the username for context
age = getAge(username)
# Print a message including the username and age
print(username + " you are " + age + " years old")

# Get the list of hobbies from the user
hobbies = getHobbies(username)
# Count the number of hobbies entered by the user
count = countHobbies(hobbies)

# Print the count of hobbies
print(count)
# Print the number of hobbies and the list of hobbies
print("You have " + str(count) + " hobbies: " + str(hobbies))
