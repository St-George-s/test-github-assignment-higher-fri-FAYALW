# Prompt Player 1 to enter an animal name and store the input in the variable 'animal'
animal = input("Player 1, please enter an animal name: ")

# Prompt Player 2 with hints about the animal:
# - First letter of the animal name
# - Last letter of the animal name
# - Total number of letters in the animal name
# Then, store Player 2's guess in the variable 'userGuess'
userGuess = input("Player 2, the first letter in this word is " + str((animal[0:1])) +
                  " the last letter is " + str((animal[-1])) +
                  " and there are " + str((len(animal))) + " letters in the word. Please make a guess: ")

# Check if the user's guess matches the original animal name
if userGuess == animal:
    print("True")  # If the guess is correct, print "True"
else:
    print("False")  # If the guess is incorrect, print "False"
