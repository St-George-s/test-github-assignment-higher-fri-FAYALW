# Start an infinite loop to continuously prompt the user for input until valid entries are provided
while True:
    # Prompt the user to enter a word with exactly seven letters
    sevenLetters = input("Please enter a word with seven letters: ")
    
    # Check if the length of the entered word is exactly 7
    if len(sevenLetters) == 7:
        print("True")  # Indicate that the seven-letter word is valid
        
        # Prompt the user to enter a word with exactly four letters
        fourLetters = input("Please enter a word with four letters: ")

        # Check if the length of the entered word is exactly 4
        if len(fourLetters) == 4:
            print("True")  # Indicate that the four-letter word is valid
            break  # Exit the loop if both inputs are valid

        else:
            print("False")  # Indicate that the four-letter word is invalid

    else:
        print("False")  # Indicate that the seven-letter word is invalid
