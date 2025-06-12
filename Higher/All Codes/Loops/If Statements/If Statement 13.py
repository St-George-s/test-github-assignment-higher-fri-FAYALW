# Initialize variables for minutes played and the limit
minutesPlayed = 0
minutesLimit = 120

# Prompt the user to enter the number of minutes played
minutesPlayed = input("Please enter the number of minutes you played for ")

# Check if the entered minutes played exceeds the limit
if int(minutesPlayed) > minutesLimit:  # Convert the input to an integer for comparison
    print("You played games too long!")  # Print a warning message if the limit is exceeded

else:
    print("You are under your time limit!")  # Print a message if the played time is within the limit
