grid = [[".", ".", "s", "s", "s"], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."]]

hits = 0
while hits < 3:
    userGuess = int(input("Please guess a number from 1-5: "))
    if grid[userGuess] == "s":
        print("You hit the ship!")
        hits += 1

    elif grid[userGuess] == ".":
        print("You missed the ship!")
        grid[userGuess] = "m"

