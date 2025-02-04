import csv

#Define a record called Sighting
class Sighting: #Creates a record
    def __init__(self, town, mammal, date, age): #Initialises the cetegories in the record
        self.town = town #Defining each category in the record
        self.mammal = mammal #Defining each category in the record
        self.date = date #Defining each category in the record
        self.age = age #Defining each category in the record

#Reads data from the file into an array (sightings) of records (Sighting)
def readData(): #Defines function
    with open('Courseworks Databases/2022 Coursework Routes/setup/mammals.txt', 'r') as file: #Opens a file
        reader = csv.reader(file) #Reads into the file
        sightings = [] #Creates an array called sightings
        for row in reader: #Loops through each row in the file
            newSighting = Sighting( #For each row in the file it makes a new record for each sighting
                row[0], #Puts town in the first row     
                row[1], #Mammal in the second row           
                row[2], #Date in the third row           
                int(row[3]), #Age in the fourth row                   
            )
            sightings.append(newSighting) #Appends each new record in the array
    return sightings #Returning the array of records to the main program

#Finds the oldest walker
def findMaxAge(sightings): #Defines function 
    maximumValue = sightings[0] #
    for sighting in sightings:
        if sighting.age > maximumValue.age:
            maximumValue = sighting
    print('The oldest walker is', maximumValue.age)  

#Finds the dates of sightings
def date(sightings):
    townInput = input('Please enter a town: ')
    townInput = upperCase(townInput)
    mammalInput = input('Please enter a mammal: ')
    mammalInput = upperCase(mammalInput)
    for sighting in sightings:
        if townInput == sighting.town and mammalInput == sighting.mammal:
            print('The dates of the sightings were:', sighting.date)

#Changed the first character to uppercase
def upperCase(word):
    firstChar = ord(word[0])
    if firstChar >=97 and firstChar <= 122:
        firstChar = firstChar - 32
        firstChar = chr(firstChar)
        word = (firstChar + word[1:])
    return word

#Calculates the number of sightings for each date
def numberOfSightings(sightings):
    dayToCount = sightings[0].date
    count = 1
    for counter in range (1, len(sightings)):
        if sightings[counter].date == dayToCount:
            count = count + 1
        else:
            print(dayToCount, count)
            dayToCount = sightings[counter].date
            count = 1

#main program
sightings = readData()
# print(sightings[0].town)

oldestWalker = findMaxAge(sightings)
print(oldestWalker)

date(sightings)

numberOfSightings(sightings)

#sightings[counter].date
#sightings = array
#counter = position in array
#date = category in the record