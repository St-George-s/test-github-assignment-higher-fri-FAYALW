## Generate a random four-digit number
## Ask the user to guess a number
## Add 1 to guess count
## Check if input matches exactly generated number, and if it does, output: Congratulations + guess count
## If the numbers aren’t an exact match, check how many numbers are the same
## Output how many numbers are the same

import random  # Importing the random module to generate a random number
from collections import OrderedDict  # Importing OrderedDict to remove duplicates from a string

ran_num = 0  # Initializing a variable ran_num to 0 to hold the random number
user_guess = 0  # Initializing a variable user_guess to 0 to hold the user's guess
count = 0  # Initializing a variable count to 0 to keep track of the number of guesses

# Generating a random four-digit number and assigning it to ran_num
ran_num = (random.randint(1000, 9999))  
print(ran_num)  # Printing the generated random number (for testing purposes)

while True:  # Start an infinite loop to continually prompt the user for a guess
    # Asking the user to input a number and converting it to an integer
    user_guess = int(input("Please guess the 4-digit number. If you are stuck, enter 0: "))  
    if user_guess == 0:  # Check if the user enters 0...
        print(ran_num)  # ...if so, print the generated random number
    count += 1  # Increment the guess count by 1 for each attempt

    if (user_guess == ran_num):  # Check if the user's guess matches the random number
        print("Congratulations, you guessed correctly in", count, "rounds")  # Inform the user they guessed correctly and display the guess count
        break  # Exit the loop since the user has guessed correctly

    else:  # If the guess is incorrect...
        arr_counter = [0] * (10)  # Initialize an array called arr_counter with 10 cells, each set to 0

        if user_guess > 9999:  # Check if the user's guess exceeds the maximum 4-digit number
            print("Invalid number. Please enter a 4-digit number")  # Inform the user that the input is invalid

        # Remove duplicates from the generated random number to avoid double counting
        ran_num_nd = "".join(OrderedDict.fromkeys(str(ran_num)))  
        # Remove duplicates from the user's guess for the same reason
        user_guess_nd = "".join(OrderedDict.fromkeys(str(user_guess)))  

        for digit in ran_num_nd:  # Iterate over each unique digit in the random number
            digit = int(digit)  # Convert the digit from string to integer
            arr_counter[digit] += 1  # Increment the count at the index corresponding to the digit

        for digit in user_guess_nd:  # Iterate over each unique digit in the user's guess
            digit = int(digit)  # Convert the digit from string to integer
            arr_counter[digit] += 1  # Increment the count at the index corresponding to the digit

        i = 0  # Initialize a variable i to 0 for iterating through the arr_counter
        count2 = 0  # Initialize a variable count2 to 0 to count how many digits are common

        while (i < 10):  # Loop through the arr_counter from 0 to 9
            if (arr_counter[i] == 2):  # Check if the count at index i is equal to 2 (indicating the digit is present in both numbers)
                count2 += 1  # Increment the count of common digits
                i += 1  # Move to the next index

            else:  # If the count is not 2...
                i += 1  # ...simply move to the next index

    print("You have", count2, "numbers in common")  # Output how many digits the user's guess shares with the random number
