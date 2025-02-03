# Generates 1 or 2 100 times; if it is 1, then it is heads, if it is 2, it is tails. 
# Shows you how many times out of 100 each was picked.

from random import randint  # Import the randint function from the random module

generated_num = 0  # Initialize a variable to store the generated number
num_heads = 0  # Initialize a counter for the number of heads
num_tails = 0  # Initialize a counter for the number of tails

# Start a loop that runs 100 times to simulate coin flips
for looper in range(100):  
    generated_num = randint(1, 2)  # Generate a random number: 1 (heads) or 2 (tails)

    # Check if the generated number corresponds to heads
    if generated_num == 1:  # If the generated number is 1...
        print("heads")  # ...print "heads"
        num_heads = num_heads + 1  # Increment the heads counter by 1

    else:  # If the generated number is not 1 (must be 2)
        print("tails")  # Print "tails" if it's 2
        num_tails = num_tails + 1  # Increment the tails counter by 1

# After the loop, print the total counts of heads and tails
print("The number of heads were " + str(num_heads))  # Output the number of heads generated
print("The number of tails were " + str(num_tails))  # Output the number of tails generated
