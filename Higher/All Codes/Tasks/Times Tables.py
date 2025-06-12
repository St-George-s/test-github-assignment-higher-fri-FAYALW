# Initialize counters for correct and incorrect answers
rightCount = 0
wrongCount = 0
x = 0  # Initialize the multiplier

# Prompt the user to choose a times table
timesTable = int(input("Choose a times table: "))

# Start an infinite loop to ask multiplication questions
while True:
    # Ask the user for the answer to the current multiplication question
    userAnswer = input(str(timesTable) + " * " + str(x) + " = ")

    # Check if the user input is neither "Done" nor "Finished"
    if userAnswer != "Done" and userAnswer != "Finished":
        # Check if the user's answer is correct
        if int(userAnswer) == timesTable * x:
            rightCount += 1  # Increment correct answer count
        else:
            wrongCount += 1  # Increment incorrect answer count
        x += 1  # Move to the next multiplier

    # If the user types "Done", move to the next times table
    elif userAnswer == "Done":
        timesTable += 1  # Increment the times table
        x = 0  # Reset the multiplier to 0

    # If the user types "Finished", display the results and exit the loop
    elif userAnswer == "Finished":
        print("You got", rightCount, "correct and", wrongCount, "incorrect")  # Show the results
        break  # Exit the loop
