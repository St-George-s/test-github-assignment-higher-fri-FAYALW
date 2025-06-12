# Define a list of letters that will be used to prompt the user for item names
letters = ['a', 'b', 'c', 'd', 'e']  
list = ""  # Initialize an empty string to store the user's input items

print("I went to the market and bought...")  # Initial prompt to introduce the user input process

# Loop through the length of the letters list
for x in range(len(letters)):
    # Prompt the user to enter an item starting with the current letter
    userInput = input("Enter an item starting with " + letters[x] + " ")

    # Check if the first letter of the user's input matches the current letter
    while (userInput[0] != letters[x]):
        # If it doesn't match, prompt the user to enter a valid item
        userInput = input("Enter valid item ")

    else:
        # If the input is valid, append the userInput to the list string
        list = list + " " + userInput  # Concatenate the valid item to the list
        # Print the current items in the market list
        print("I went to the market and bought a" + list)
