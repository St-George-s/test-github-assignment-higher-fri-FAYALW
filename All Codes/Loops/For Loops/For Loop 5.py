# Prints the user's name as many times as the number of letters in the name

myName = ""  # Initializes myName as a variable, starting with an empty string
myAge = 0  # Initializes myAge as a variable, starting with a value of 0
string_len = 0  # Initializes string_len as a variable to hold the length of the name

# Prompt the user to enter their name
myName = input("enter your name")  # Asks user for their name and stores it in myName

# Prompt the user to enter their age
myAge = int(input("enter your age "))  # Asks user for their age and converts it to an integer

# Calculate the length of the user's name
string_len = len(myName)  # Assigns the length of myName to the variable string_len

# Loop that runs for each character in the user's name
for x in range(string_len):  # Creates a loop that iterates string_len times
    print(myName)  # Prints the user's name each time the loop runs