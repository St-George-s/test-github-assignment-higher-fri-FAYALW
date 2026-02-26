# List of first names corresponding to the scores
firstNames = ['John', 'Sarah', 'Bob', 'Mark', 'Hazel']
# List of scores associated with each name
scores = [13, 32, 43, 23, 10]
# Variable to hold the total score
totalScore = 0

# Loop through each index in the range of the number of first names
for count in range(len(firstNames)):
    # Add the score at the current index to the totalScore
    totalScore = totalScore + scores[count]

# Calculate the average score by dividing the totalScore by the number of scores
avg = totalScore / len(scores)

# Print the average score with a message
print("Average score is " + str(avg))  # Convert avg to string for concatenation