# Makes user guess a number between 0 and 100 that is randomly picked by the code
# Sets the correct number to an integer between 0 and 100 and provides unlimited feedback
# to the user about whether their guess is too high/low until they get it right 

import random  # Imports the random library to use its functions for generating random numbers

# Generates a random integer between 0 and 100 (inclusive)
gen_number = random.randint(0, 100)  
#print(gen_number)  # Optional: Uncomment to see the generated number (for debugging purposes)

user_guess = 0  # Initialize user_guess to 0

print("Guess the number between 0 and 100")  # Prompt the user to guess a number
user_guess = int(input())  # Read the user's guess and convert it to an integer

# Loop that continues until the user guesses the correct number
while user_guess != gen_number:  # Check if the guess is not equal to the generated number
    if user_guess > gen_number:  # If the user's guess is higher than the correct number
        print("Your guess is too high")  # Inform the user that their guess is too high
        print("Enter another guess")  # Prompt the user to enter a new guess
        user_guess = int(input())  # Read the new guess

    else:  # If the guess is lower than the number
        print("Your guess is too low")  # Inform the user that their guess is too low
        print("Enter another guess")  # Prompt the user to enter a new guess
        user_guess = int(input())  # Read the new guess

print("Well done")  # When the correct number is guessed, print a success message
