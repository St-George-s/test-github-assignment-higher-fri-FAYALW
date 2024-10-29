import random  # Import the random module to generate random numbers
import os      # Import the os module for operating system dependent functionality

count = 0  # Initialize a counter for the number of guesses
number = random.randint(1, 100)  # Generate a random number between 1 and 100
countUser = 0  # Initialize the count for user wins
countComputer = 0  # Initialize the count for computer wins

userScore = []  # Initialize a list to store user scores
# Open the score file in read mode to load previous scores
with open("../Other Text Files/Score.txt", "r") as file:
    scores = file.readline()  # Read the first line of the file
    for score in scores:  # Iterate through each character in the scores string
        if score != ",":  # Check if the character is not a comma
            userScore.append(score)  # Append the score to the userScore list

## Uncomment these lines to debug and check scores
## print("Scores is", scores)
## print(userScore)
## print(len(userScore))

# Count the number of user and computer wins based on the scores
for x in range(len(userScore)):
    if x <= 6:  # First 7 entries are considered user wins
        countUser += 1  # Increment user win count
    else:  # Entries after the first 7 are considered computer wins
        countComputer += 1  # Increment computer win count
## print("The user has won", countUser, "amount of times and the computer has won", countComputer, "amount of times")       

# Start a loop to allow the user to guess the number
while True:
    count += 1  # Increment the guess counter
    userGuess = int(input("Guess the number between 1 and 100: "))  # Get user input and convert it to an integer
    if userGuess == number:  # Check if the user's guess is correct
        print("Correct!")  # Inform the user of the correct guess
        break  # Exit the loop
    elif number > userGuess:  # Check if the guessed number is lower than the actual number
        print("Higher")  # Prompt the user to guess higher
    else:  # If the guess is higher than the actual number
        print("Lower")  # Prompt the user to guess lower

# Determine the outcome based on the number of guesses
if count <= 6:  # If the user took 6 or fewer guesses
    print("You took", count, "turns. You won!")  # Inform the user they won
else:  # If the user took more than 6 guesses
    print("You took", count, "turns. You lost!")  # Inform the user they lost

# This code writes the game score to the score file
with open("../Other Text Files/Score.txt", "a") as file:  # Open the score file in append mode
    file.write(str(count))  # Write the count of guesses as a string to the file
    file.write(",")  # Append a comma to separate scores
