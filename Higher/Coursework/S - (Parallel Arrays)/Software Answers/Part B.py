import csv  # Import the CSV module to handle reading data from CSV files

# Defining parallel arrays to store game data
gameTitles = []   # List to hold game titles
genres = []       # List to hold game genres
ageRatings = []   # List to hold age ratings of games
platform = []     # List to hold the platforms on which games are available
genre_to_check = ""  # Variable to specify the genre to check

# Function to read game data from a CSV file and store it in parallel arrays
def readGameDataFromCSV():
    # Open the CSV file containing game platform data
    with open('Class Test/game_platform_data.csv', 'r') as file:
        reader = csv.reader(file)  # Create a CSV reader to process each row

        # Define local parallel arrays to hold data for this function
        gameTitles = []
        genres = []
        ageRatings = []
        platform = []
        
        # Setting genre_to_check to "Fantasy"
        genre_to_check = "Fantasy"

        # Looping over each row in the CSV and appending data to parallel arrays
        for row in reader:
            gameTitles.append(row[0])  # Append game title from the first column
            genres.append(row[1])       # Append genre from the second column
            ageRatings.append(row[2])   # Append age rating from the third column
            platform.append(row[3])     # Append platform from the fourth column

    # Returning the arrays of game titles, genres, age ratings, and platforms
    return gameTitles, genres, ageRatings, platform

# Function to count suitable games in the genre "Fantasy" with an age rating of less than 18
def countSuitableGames(genre_to_check, gameTitles, genres, ageRatings):
    # Setting count to 0 to track the number of suitable games
    count = 0
    
    # Loop through each index in gameTitles
    for i in range(len(gameTitles)):
        # Check if the current genre is "Fantasy" and if the age rating is less than 18
        if genres[i] == genre_to_check and int(ageRatings[i]) < 18:  # Convert age rating to int for comparison
            print(gameTitles[i])  # Print the title of the suitable game
            count += 1  # Increment the count of suitable games

    # Print the total count of suitable games found
    print(count)

# Function to check if the game is available on a given platform
def availableOnPlatform(gameTitles, platforms, genre_to_check):
    # Opens a file to write suitable game information
    with open('platform_suitable_games.txt', 'w') as file:
        # Loop through each game to check the conditions
        for i in range(len(gameTitles)):
            # Checks the conditions for genre and platform suitability
            if genres[i] == genre_to_check and int(ageRatings[i]) < 18 and platform[i] == "PC":
                # If the conditions are met, write the game title and platform to the file
                file.write(f"{gameTitles[i]} - {platform[i]}\n")
            else:
                # If the conditions are not met, no action is taken (writing an empty string is unnecessary)
                pass

# Main function to orchestrate reading game data and counting suitable games
def main():
    # Read game data and store it in parallel arrays
    gameTitles, genres, ageRatings, platform = readGameDataFromCSV()
    
    # Count and display suitable games based on the specified genre and age rating
    countSuitableGames(genre_to_check, gameTitles, genres, ageRatings)

    # Check for suitable games on the specified platform and write to the file
    availableOnPlatform(gameTitles, platform, genre_to_check)

# Calling the main function to execute the program
main()