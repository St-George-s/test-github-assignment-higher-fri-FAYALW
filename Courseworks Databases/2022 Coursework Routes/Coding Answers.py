#1b)
def upperCase(userInputTown, userInputMammal):
    if userInputTown[0] != userInputTown[0].upper or userInputMammal[0] != userInputMammal[0].upper:
        userInputTown[0] = userInputTown[0].upper
        userInputMammal[0] = userInputMammal[0].upper
    return userInputTown, userInputMammal

#1c)
import csv

class sighting:
    def __init__(self, town, mammal, date, age):
    self.town = towm
    self.mammal = mammal
    self.date = date
    self.age = age

def readData():
    with open('Courseworks Databases/2022 Coursework Routes/setup/mammals.txt', 'r'')
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            newSighting = sighting(
                row[0],           
                row[1],            
                row[2],            
                int(row[3]),                   
            )
            sightings.append(newSighting)
    return sighting

def age(inputs):
    oldestWalker = inputs[0]
    for input in inputs:
        if 

def date():


def sightings():



def upperCase(userInputTown, userInputMammal):
    firstCharTown = ord(userInputTown[0]) 
    firstCharMammal = ord(userInputMammal[0])
    if firstCharTown >= 97 and firstCharTown =< 122 or firstCharMammal >= 97 and firstCharMammal =< 122:
        firstCharTown = firstCharTown - 32
        firstCharMammal = firstCharMammal -32
        town = (firstCharTown + userInputTown[1:])
        mammal = (firstCharMammal + userInputMammal[1:])
    








userInputTown = input('Enter the name of a town')
upperCase(userInputTown, userInputMammal)
userInputMammal = input('Enter the name of a mammal')
upperCase(userInputTown, userInputMammal)

for sighting in sightings:
    if userInputTown == sightings.town and userInputMammal == sightings.mammal
    print(sighting.date)

