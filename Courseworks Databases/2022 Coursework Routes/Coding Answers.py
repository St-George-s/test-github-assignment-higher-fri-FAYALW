import csv

#Define a record called Sighting
class Sighting:
    def __init__(self, town, mammal, date, age):
        self.town = town
        self.mammal = mammal
        self.date = date
        self.age = age

#Reads data from the file into an array (sightings) of records (Sighting)
def readData():
    with open('Courseworks Databases/2022 Coursework Routes/setup/mammals.txt', 'r') as file:
        reader = csv.reader(file)
        sightings = []

        for row in reader:
            newSighting = Sighting(
                row[0],           
                row[1],            
                row[2],            
                int(row[3]),                   
            )
            sightings.append(newSighting)
    return sightings

def findMaxAge(sightings):
    maximumValue = sightings[0]
    for sighting in sightings:
        if sighting.age > maximumValue.age:
            maximumValue = sighting
    print('The oldest walker is', maximumValue.age)  

def date(sightings):
# 3.1 Ask user to enter town
    town = input('Please enter a town')
# 3.2 Call a function to return a string input that starts with an upper-case character
    upperCase(town)
# 3.3 Ask user to enter mammal
    mammal = ('Please enter a mammal')
# 3.4 Call a function to return a string input that starts with an upper-case character
    upperCase(mammal)
# 3.5 Display “The dates of sightings were:”
    print('The dates of the sightings were:')
# 3.6 Start loop for each sighting in array of records
    for sighting in sightings:
# 3.7 If sighting matches entered town and mammal then
        if town == sighting.town and mammal == sighting.mammal:
# 3.8 Display date
            print(sighting.date)
# 3.9 End if
# 3.10 End loop

#main program
sightings = readData()
print(sightings[0].town)

oldestWalker = findMaxAge(sightings)
print(oldestWalker)

date(sightings)

# def date():


# def sightings():



# def upperCase(userInputTown, userInputMammal):
#     firstCharTown = ord(userInputTown[0]) 
#     firstCharMammal = ord(userInputMammal[0])
#     if firstCharTown >= 97 and firstCharTown =< 122 or firstCharMammal >= 97 and firstCharMammal =< 122:
#         firstCharTown = firstCharTown - 32
#         firstCharMammal = firstCharMammal -32
#         town = (firstCharTown + userInputTown[1:])
#         mammal = (firstCharMammal + userInputMammal[1:])

# userInputTown = input('Enter the name of a town')
# upperCase(userInputTown, userInputMammal)
# userInputMammal = input('Enter the name of a mammal')
# upperCase(userInputTown, userInputMammal)

# for sighting in sightings:
#     if userInputTown == sightings.town and userInputMammal == sightings.mammal
#     print(sighting.date)

