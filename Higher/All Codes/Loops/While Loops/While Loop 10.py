import random  # Import the random module to generate random numbers

# Generate a random integer between 0 and 100 (inclusive)
randomNumber = random.randint(0, 100)
# Print the randomly generated number to the console
print(randomNumber)

# Initialize userGuess to an invalid value to start the loop
userGuess = -1

# Continue looping until the user guesses the correct number
while userGuess != randomNumber:
    # Prompt the user to input their guess and convert it to an integer
    userGuess = int(input("Guess a number between 0 and 100: "))
    
    # Check if the user's guess matches the random number
    if userGuess == randomNumber:
        # If the guess is correct, print a success message
        print("You guessed correctly!")
    elif userGuess < randomNumber:
        # If the guess is lower than the random number, print a hint
        print("You guessed too low!")
    elif userGuess > randomNumber:
        # If the guess is higher than the random number, print a hint
        print("You guessed too high!")
