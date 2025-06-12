import random  # Import the random module to generate random numbers
import time    # Import the time module to introduce delays in the program

# Define a list of movie titles
f1 = "Dune"                        # First movie title
f2 = "Dead Poets Society"          # Second movie title
f3 = "Barbie"                      # Third movie title
f4 = "Oppenheimer"                 # Fourth movie title
f5 = "Mean Girls"                  # Fifth movie title

# Define responses based on the user's rating
r1 = "Sorry to hear that."         # Response for a rating of 1 star
r2 = "Sounds like it was OK then."  # Response for a rating of 2 stars
r3 = "Great to hear, I'll check it out myself."  # Response for a rating of 3 stars
r4 = "I thought so too, I bet you can't wait to see it again!"  # Response for a rating of 4 stars

# Generate a random integer between 1 and 5 to select a movie
movie = random.randint(1, 5)

print("Rate the movie...")  # Prompt the user to rate a randomly selected movie
time.sleep(3)  # Pause for 3 seconds to create anticipation

# Determine which movie to display based on the random number generated
if movie == 1:
    print(f1)  # Print the first movie title
elif movie == 2:
    print(f2)  # Print the second movie title
elif movie == 3:
    print(f3)  # Print the third movie title
elif movie == 4:
    print(f4)  # Print the fourth movie title
elif movie == 5:
    print(f5)  # Print the fifth movie title

# Prompt the user to enter their rating for the movie
rating = int(input("Enter your star rating out of 4 here: "))  # Convert user input to an integer
time.sleep(3)  # Pause for 3 seconds before displaying the response

# Provide a response based on the rating given by the user
if rating == 1:
    print(r1)  # Print response for a rating of 1 star
elif rating == 2:
    print(r2)  # Print response for a rating of 2 stars
elif rating == 3:
    print(r3)  # Print response for a rating of 3 stars
elif rating == 4:
    print(r4)  # Print response for a rating of 4 stars
