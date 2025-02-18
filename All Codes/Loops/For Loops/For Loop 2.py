# Asks the user to input their name
print("enter your name")  
myName = ""  # Initializes myName as an empty variable to store the user's name
myName = input()  # Stores the user's input as their name in myName

# Asks the user to input their age
print("enter your age")  
myAge = ""  # Initializes myAge as an empty variable to store the user's age
myAge = int(input())  # Converts the user's input to an integer and stores it as their age in myAge

# Loop to print the user's name as many times as their age
for deliciousbubbletea in range(myAge):  # Loops from 0 to myAge-1, repeating the block below
    print(myName)  # Prints the user's name each time the loop runs