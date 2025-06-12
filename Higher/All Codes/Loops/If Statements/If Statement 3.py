import nltk  # Import the Natural Language Toolkit (NLTK) library
from nltk.corpus import cmudict  # Import the CMU Pronouncing Dictionary
import time  # Import the time module to handle timing events

# Download popular NLTK data packages
import nltk;
nltk.download('popular')

# Load the NLTK pronunciation dictionary
nltk.download('cmudict')  # Download the CMU pronunciation dictionary
d = cmudict.dict()  # Load the dictionary into variable d

# Function to get the pronunciation of a word
def get_pronunciation(word):
    word = word.lower()  # Convert the word to lowercase for consistency
    if word in d:  # Check if the word exists in the dictionary
        return d[word][0]  # Return the first pronunciation of the word
    else:
        return None  # Return None if the word is not found

# Function to check if two words have the same pronunciation
def have_same_pronunciation(word1, word2):
    word1_pronunciation = get_pronunciation(word1)  # Get pronunciation for word1
    word2_pronunciation = get_pronunciation(word2)  # Get pronunciation for word2
    # Check if both words have valid pronunciations and compare them
    if word1_pronunciation is not None and word2_pronunciation is not None:
        return word1_pronunciation == word2_pronunciation  # Return True if they match
    else:
        return False  # Return False if either word is not found

# Function to get rhyming words
def get_rhyming_words(word, word_list):
    rhyming_words = []  # Initialize an empty list to store rhyming words
    for w in word_list:  # Iterate over each word in the provided word list
        if have_same_pronunciation(word, w):  # Check if the current word rhymes with the input word
            rhyming_words.append(w)  # Add the word to the rhyming words list
    return rhyming_words  # Return the list of rhyming words

# Game loop
def play_game():
    word = input("Enter a word: ")  # Prompt the user to enter a word
    word_list = []  # Initialize an empty list to store user input words
    print("Enter rhyming words within 30 seconds:")  # Inform the user of the time limit
    start_time = time.time()  # Record the start time
    # Loop until 30 seconds have passed
    while time.time() - start_time < 30:
        word_input = input("> ")  # Prompt for a rhyming word
        if word_input.lower() == "quit":  # Allow user to exit early by typing 'quit'
            break
        word_list.append(word_input.lower())  # Add the input word to the list
    end_time = time.time()  # Record the end time
    rhyming_words = get_rhyming_words(word, word_list)  # Find rhyming words for the original word
    print("Time's up!")  # Inform the user that time is up
    # Display the rhyming words found
    print("Rhyming words for '{}' are: {}".format(word, rhyming_words))

# Start the game
play_game()  # Call the function to initiate the game
