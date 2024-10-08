import csv

#Reading the game data from the CSV file
def readGameDataFromCSV():
    with open('Class Test/game_data.csv', 'r') as file:
        reader = csv.reader(file)

        #Defining parallel arrays
        gameTitles = []
        genres = []
        ageRatings = []
        #Setting genre_to_check to "Fantasy"
        genre_to_check = "Fantasy"

        #Looping over each row and appending the data to parallel arrays
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(row[2])

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

#Calling the subroutines
def main():
    readGameDataFromCSV()
    countSuitableGames(genre_to_check, gameTitles, genres, ageRatings)

#Calling the subroutine which calls the subroutines
main()