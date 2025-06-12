import random  # Import the random module for generating random numbers
import os  # Import the os module (not used in this code)
import time  # Import the time module for time-related functions

# Initialize counters for correct answers and lists for questions and incorrect answers
countCorrect = 0
questions = []  # List to store questions and correct answers
incorrectAnswers = []  # List to store incorrect answers and related data

# Parse the data from the file into a 2D list
with open("../Other Text Files/CSQuestions&CorrectAnswers.txt", "r") as file:
    for line in file:
        line = line.strip()  # Remove leading and trailing whitespace
        temp = line.split("--")  # Split the line into question and answer
        print("temp is", temp)  # Print the temporary list for debugging purposes
        questions.append(temp)  # Append the question and answer to the questions list

# Print the list of questions for debugging
print(questions)        

# Ask 5 random questions
for x in range(5):
    # Picks one of the questions in the list randomly
    choice = random.randint(0, len(questions) - 1)

    # Ask the user the question and convert the answer to lowercase for comparison
    answer = input(questions[choice][0]).lower()

    # Check if the user's answer matches the correct answer (case insensitive)
    if answer == questions[choice][1].lower():
        countCorrect += 1  # Increment the correct answer counter
        print("Correct")  # Inform the user their answer is correct
    else:
        print("Incorrect. The correct answer is", questions[choice][1])  # Inform the user of the correct answer

        # Create a temporary list with the question, the user's wrong answer, and the timestamp
        incorrectAnswer = [questions[choice][0], answer, time.ctime()]
        incorrectAnswers.append(incorrectAnswer)  # Append this data to the incorrect answers list

    # Delete the question from the list to prevent it from being chosen again
    del questions[choice]

# Print the user's final score
print("Your final score was", countCorrect)

# Use the incorrect answers list to append any wrong answers to the wrong answers text file
with open("../Other Text Files/WrongAnswers.csv", "a") as file:
    for i in range(len(incorrectAnswers)):
        line = ",".join(incorrectAnswers[i]) + "\n"  # Create a CSV formatted string from the incorrect answers
        file.write(line)  # Write the line to the wrong answers file
