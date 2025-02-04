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
    townInput = input('Please enter a town')
    upperCase(townInput)
    mammalInput = ('Please enter a mammal')
    upperCase(mammalInput)
    for sighting in sightings:
        if townInput == sighting.town and mammalInput == sighting.mammal:
            print('The dates of the sightings were:', sighting.date)

def upperCase(word):
    firstChar = ord(word[0])
    if firstChar >=97 and firstChar <= 122:
        firstChar = firstChar - 32
        firstChar = chr(firstChar)
        word = (firstChar + word[1:])
    return word

def numberOfSightings(sightings):
# 4.1 Set dayToCount to first date in sightings array
    dayToCount = sightings.date[0]
# 4.2 Set count to 1
    count = 1
# 4.3 Start loop from second record to end of sightings array
    for x in range (1, len(sightings)):
# 4.4 If date in current record is the same as dayToCount then
        if x == dayToCount:
# 4.5 Add 1 to count
            count = count + 1
# 4.6 Else
        else:
# 4.7 Display dayToCount and count
            print(dayToCount, count)
# 4.8 Set dayToCount to date in current record
            dayToCount = x
# 4.9 Set count to 1
            count = 1

#main program
sightings = readData()
print(sightings[0].town)

oldestWalker = findMaxAge(sightings)
print(oldestWalker)

date(sightings)

numberOfSightings(sightings)