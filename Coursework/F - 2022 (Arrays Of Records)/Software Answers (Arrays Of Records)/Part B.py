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
    with open('Coursework/Full/CW Full 2/Software Answers/Part B.py', 'r') as file: #Opens a file
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
    maximumValue = sightings[0] #Sets the maximum value to the first record in the sightings array
    for sighting in sightings: #Loops through each record in sightings 
        if sighting.age > maximumValue.age: # Checks if the current age is larger than the one stored in maximum value
            maximumValue = sighting #Sets maximumValue to the new age
    print('The oldest walker is', maximumValue.age) #Prints the age of the oldest walker

#Finds the dates of sightings
def date(sightings): #Defines function
    townInput = input('Please enter a town: ') #Gets the user to input a town and stores it in the variable townInput
    townInput = upperCase(townInput) #Passes the town input through the upperCase function
    mammalInput = input('Please enter a mammal: ') #Gets the user to input a mammal and stores it in the variable mammalInput
    mammalInput = upperCase(mammalInput) #Passes the mammal input through the upperCase function
    for sighting in sightings: #Loops through each record in the array
        if townInput == sighting.town and mammalInput == sighting.mammal: #Checks if the inputs match the data
            print('The dates of the sightings were:', sighting.date) #Prints the dates of the sightings

#Changed the first character to uppercase
def upperCase(word): #Defines function
    firstChar = ord(word[0]) #Changes the first character of the word to its ASCII value
    if firstChar >= 97 and firstChar <= 122: #Checks if the ASCII value is between 97 and 122
        firstChar = firstChar - 32 #Subtracts 32 from the ASCII value
        firstChar = chr(firstChar) #Updates the firstChar variable
        word = (firstChar + word[1:]) #Concatenation
    return word #Returns the new word

#Calculates the number of sightings for each date
def numberOfSightings(sightings): #Defines function
    dayToCount = sightings[0].date #Sets the dayToCount variable to the first date in the array
    count = 1 #Sets count to 1
    for counter in range (1, len(sightings)): #Loops through the array
        if sightings[counter].date == dayToCount: #Checks if the current date is equal to the dayToCount variable
            count = count + 1 #Adds 1 to count
        else: #Else
            print(dayToCount, count) #Prints the dayToCount and the count
            dayToCount = sightings[counter].date #Sets dayToCount to the current record
            count = 1 #Sets count to 1

#main program
sightings = readData() #Calls the function to read into the file
# print(sightings[0].town)

oldestWalker = findMaxAge(sightings) #Calls the function to find the maximum age and sets it to the variable oldestWalker
print(oldestWalker) #Prints it

date(sightings) #Calls the function to find the date of the sightings

numberOfSightings(sightings) #Calls the function to count the number of sightings

#sightings[counter].date
#sightings = array
#counter = position in array
#date = category in the record