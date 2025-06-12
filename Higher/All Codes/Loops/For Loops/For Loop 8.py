# Guess heads or tails 3 times and see how many times you guessed right out of 3

import random  # Import the random module to generate random numbers

coin_side = ""  # Initializes the variable to hold the side of the coin
total = 0  # Initializes the variable to count the total correct guesses
rand_num = 0  # Initializes the variable to store the random number
guess = ""  # Initializes the variable to store the user's guess

# Loop that runs 3 times for the user to make their guesses
for x in range(3):  
    rand_num = random.randint(0, 1)  # Generates a random number: 0 (tails) or 1 (heads)
    
    # Determine the coin side based on the random number
    if rand_num == 1:  # If the random number is 1...
        coinside = "heads"  # ...then set coinside to "heads"
    else: 
        coinside = "tails"  # Otherwise, set coinside to "tails"

    # Prompt the user to make a guess
    guess = input("Choose heads or tails: ")
    
    # Check if the user's guess matches the coin side
    if guess == coinside:  # If the guess is the same as coinside...
        total = total + 1  # ...then increment the total correct guesses by 1

# Print the total number of correct guesses out of 3 attempts
print("You guessed it right " + str(total) + " times out of 3")  # Outputs the result to the user
