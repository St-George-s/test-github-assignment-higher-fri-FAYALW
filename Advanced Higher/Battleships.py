grid = [[".", ".", "s", "s", "s"], 
        [".", ".", ".", ".", "."], 
        [".", ".", ".", ".", "."], 
        [".", ".", ".", ".", "."], 
        [".", ".", ".", ".", "."]]

# print(grid[0][2])

hits = 0
while hits < 3:
    userGuessRow = int(input("Please guess a row from 1-5: "))
    userGuessColumn = int(input("Please guess a column from 1-5: "))
    if grid[userGuessRow][userGuessColumn] == "s":
        print("You hit the ship")
        hits += 1

    elif grid[userGuessRow][userGuessColumn] == ".":
        print("You missed the ship!")
        grid[userGuessRow][userGuessColumn] = "m"



