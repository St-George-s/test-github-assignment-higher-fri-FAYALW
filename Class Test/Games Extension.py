import csv

#Defining parallel arrays
gameTitles = []
genres = []
ageRatings = []
genre_to_check = ""
platform = []

#Reading the game data from the CSV file
def readGameDataFromCSV():
    with open('Class Test/game_platform_data.csv', 'r') as file:
        reader = csv.reader(file)

        #Defining parallel arrays
        gameTitles = []
        genres = []
        ageRatings = []
        platform = []
        #Setting genre_to_check to "Fantasy"
        genre_to_check = "Fantasy"

        #Looping over each row and appending the data to parallel arrays
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(row[2])
            platform.append(row[3])

    #Returning the arrays
    return gameTitles, genres, ageRatings

#Counting the suitable games in the genre "Fantasy" with an age rating of less than 18
def countSuitableGames(genre_to_check, gameTitles,genres,ageRatings):
    #Setting count to 0
    count = 0
    #Setting genre_to_check to "Fantasy"
    genre_to_check = "Fantasy"
    
    #Loop to loop through each index in gameTitles
    for games in gameTitles:
        #Loop which checks if the current genre is "Fantasy" and if the age rating is less than 18
        if genres == genre_to_check and ageRatings < 18:
            print(gameTitles[games])
            #If the condition is true, 1 is added to count
            count = count + 1
    print(count)

#Checks if the game is available on a given platform
def availableOnPlatform():
    #Opens a file to write to
    with open('platform_suitable_games.txt', 'w') as file:

        #Checks the conditions
        if genre_to_check == "Fantasy" and ageRatings < 18 and platform == "PC":
            #If the conditions are met, information is written to the file
            file.write(gameTitles + "-" + platform)
        else:
            #If the conditions are not met, nothing is written to the file
            file.write("")

#Calling the subroutines
def main():
    readGameDataFromCSV()
    countSuitableGames(genre_to_check, gameTitles, genres, ageRatings)

#Calling the subroutine which calls the subroutines
main()