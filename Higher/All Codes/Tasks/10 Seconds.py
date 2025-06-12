import time  # Import the time module to use its time-related functions

# Prompt the user to start the timer and wait for their input
userInputStart = input("Press 'Enter' when you want to start the clock")

# Record the current time when the user starts the timer
startTime = time.time()

# Prompt the user to stop the timer and wait for their input
userInputEnd = input("Press 'Enter' when you want to stop the clock")

# Record the current time when the user stops the timer
endTime = time.time()

# Calculate the elapsed time by subtracting the start time from the end time
# Round the result to 4 decimal places and print it
print("The time elapsed was", round(endTime - startTime, 4), "seconds")
