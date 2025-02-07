import csv  # Import the CSV module to handle reading data from CSV files

# Function to read game data from a CSV file and store it in parallel arrays
def readGameDataFromCSV():
    # Open the CSV file containing game data
    with open('Class Test/game_data.csv', 'r') as file:
        reader = csv.reader(file)  # Create a CSV reader to process each row

        # Defining parallel arrays to hold game titles, genres, and age ratings
        gameTitles = []
        genres = []
        ageRatings = []
        
        # Setting genre_to_check to "Fantasy"
        genre_to_check = "Fantasy"

        # Looping over each row and appending the data to parallel arrays
        for row in reader:
            gameTitles.append(row[0])  # Append game title from the first column
            genres.append(row[1])       # Append genre from the second column
            ageRatings.append(row[2])   # Append age rating from the third column

    # Returning the arrays of game titles, genres, and age ratings
    return gameTitles, genres, ageRatings

# Function to count suitable games in the "Fantasy" genre with an age rating of less than 18
def countSuitableGames(genre_to_check, gameTitles, genres, ageRatings):
    # Setting count to 0 to track the number of suitable games
    count = 0

    # Loop through each index in gameTitles
    for i in range(len(gameTitles)):
        # Check if the current genre is "Fantasy" and if the age rating is less than 18
        if genres[i] == genre_to_check and int(ageRatings[i]) < 18:  # Convert age rating to int for comparison
            print(gameTitles[i])  # Print the suitable game title
            # If the condition is true, increment count by 1
            count += 1

    # Print the total count of suitable games found
    print(count)

# Main function to orchestrate reading game data and counting suitable games
def main():
    # Read game data and store it in parallel arrays
    gameTitles, genres, ageRatings = readGameDataFromCSV()
    # Count and display suitable games based on the specified genre and age rating
    countSuitableGames("Fantasy", gameTitles, genres, ageRatings)

# Calling the main function to execute the program
main()