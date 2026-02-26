#Making a grid with a ship in a location
grid = [[".", ".", "s", "s", "s"], 
        [".", ".", ".", ".", "."], 
        [".", ".", ".", ".", "."], 
        [".", ".", ".", ".", "."], 
        [".", ".", ".", ".", "."]]

# print(grid[0][2])

#If they have hit less than 3 times then this loop runs
hits = 0 #Initialises a counter called hits and sets it to 0
while hits < 3: #While  
    userGuessRow = int(input("Please guess a row from 1-5: "))-1
    userGuessColumn = int(input("Please guess a column from 1-5: "))-1
    if grid[userGuessRow][userGuessColumn] == "s":
        print("You hit the ship")
        hits += 1

    elif grid[userGuessRow][userGuessColumn] == ".":
        print("You missed the ship!")
        grid[userGuessRow][userGuessColumn] = "m"