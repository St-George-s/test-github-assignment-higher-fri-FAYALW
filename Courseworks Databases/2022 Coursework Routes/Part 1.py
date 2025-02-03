#1b)
def upperCase(userInputTown, userInputMammal):
    if userInputTown[0] != userInputTown[0].upper or userInputMammal[0] != userInputMammal[0].upper:
        userInputTown[0] = userInputTown[0].upper
        userInputMammal[0] = userInputMammal[0].upper
    return userInputTown, userInputMammal