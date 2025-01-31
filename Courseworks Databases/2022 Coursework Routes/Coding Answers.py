#1b)
def upperCase(userInputTown, userInputMammal):
    if userInputTown[0] != userInputTown[0].upper or userInputMammal[0] != userInputMammal[0].upper:
        userInputTown[0] = userInputTown[0].upper
        userInputMammal[0] = userInputMammal[0].upper
    return userInputTown, userInputMammal

#1c)
def readData(inputs):
    with open(sightings.txt, 'r') as file:
        content = file.read()
    return inputs

def age(inputs):
    oldestWalker = inputs[0]
    for input in inputs:
        if 

def dates():

def sightings():

def upperCase(userInputTown, userInputMammal):
    if userInputTown[0] != userInputTown[0].upper or userInputMammal[0] != userInputMammal[0].upper:
        userInputTown[0] = userInputTown[0].upper
        userInputMammal[0] = userInputMammal[0].upper
    return userInputTown, userInputMammal

userInputTown = input('Enter the name of a town')
upperCase(userInputTown, userInputMammal)
userInputMammal = input('Enter the name of a mammal')
upperCase(userInputTown, userInputMammal)

for sighting in sightings:
    if userInputTown = sightings.town and userInputMammal = sightings.mammal:
    print(sighting.date)
