# A program to demonstrate a linear search

found = False  # Initialize a boolean variable to track whether the score has been found
score = [45, 76, 12, 65, 99, 21, 35, 61, 95]  # Create a list of scores
get_score = 0  # Initialize a variable to store the user's input (initially set to 0, but will be overwritten)
pos = 0  # Initialize a variable to keep track of the current position in the list

# Ask the user to enter the score they are looking for
print("Please enter the score you are looking for:")  # Prompt the user for input
get_score = int(input())  # Store the user's input as an integer in the variable get_score

# Start a loop that continues until the score is found or all scores have been checked
while found == False and pos != len(score):  # Loop as long as 'found' is False and 'pos' is less than the length of the list
    if score[pos] == get_score:  # Check if the current score at position 'pos' matches the user's input
        found = True  # If a match is found, set 'found' to True
    else: 
        pos = pos + 1  # If not found, increment 'pos' to check the next score

# Check if the score was found and print the appropriate message
if found == True:  # If the score was found...
    print("The score was found")  # ... print that it was found
else:
    print("The score was not found")  # If not found, print that it was not found
