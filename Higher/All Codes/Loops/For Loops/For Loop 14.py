# Define an array of scores
score = [12, 45, 32]  # List of scores corresponding to each name
name = ["A", "B", "C"]  # List of names corresponding to each score
total = 0  # Initialize a variable to hold the total score

# Loop to print each name in the name array
for x in range(3):  # Loop runs for the length of the name array
    print(name[x])  # Print the name at the current index

# Loop to calculate the total score
for y in range(3):  # Loop runs for the length of the score array
    total = total + score[y]  # Add the score at the current index to the total

# Print the final total score
print(total)  # Output the total score calculated from the score array