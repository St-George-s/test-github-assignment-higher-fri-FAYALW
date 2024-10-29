# Initialize an empty list to store scores
score = []

# Initialize variables to hold the current score and number of scores
get_score = 0  # Variable to hold the individual score input by the user
no_score = 0   # This variable is defined but not used in the code

# Prompt the user for the number of scores they will enter
no_scores = int(input("how many scores are there? "))  # Convert input to an integer

# Loop through the range specified by the user input for the number of scores
for x in range(no_scores):  # Iterate from 0 to no_scores - 1
    get_score = int(input("enter a score "))  # Prompt the user to enter a score and convert it to an integer
    score.append(get_score)  # Append the entered score to the score list

# Print the list of scores entered by the user
print(score)
