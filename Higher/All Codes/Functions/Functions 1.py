# Function to get the user's name and then call the age function

def get_name():
    # Prompt the user to enter their name and store it in myName
    myName = input("Enter your name: ")
    # Display the user's name
    print(myName)
    # Call the get_age function to prompt for age
    get_age()

# Function to get the user's age
def get_age():
    # Prompt the user to enter their age and store it in myAge
    myAge = input("Enter your age: ")
    # Display the user's age
    print(myAge)

# Initial call to get_name function to start the process
get_name()
