import csv #Imports CSV

entryID = [] #Creates an empty array for each variable
location = []
forename = []
surname = []
jumps = []

#Function to read information from the athletes CSV file
def readAthletesFile():
    with open('Coursework/Full/CW Full 2024/Software Answers/athletes.csv', 'r') as file: #Opens athletes CSV file
        reader = csv.reader(file) #Turns each line into a list
        for row in reader: #Loops through each row in the file
            entryID.append(row[0]) #Populates the arrays
            location.append(row[1])
            forename.append(row[2])
            surname.append(row[3])
            jumps.append(int(row[4]))

#Function to generate the unique bib values
def generateBibValues():
    with open('Coursework/Full/CW Full 2024/Software Answers/bibValues.csv', 'w') as file: #Creates a CSV file called bibValues and writes to it
        for x in range(len(entryID)): #Loops through the file
            bibValue = forename[x][:1] + surname[x] + str(ord(location[x][:1])) #Creates the unique bib value
            line = entryID[x] + " " + bibValue + "\n" #Formats it so that each one is on a new line
            file.write(line) #Writes the line creates in the file

#Function to work out the maximum jumping jacks completed
def maxJumpingJacks():
    maxJumps = jumps[0] #Sets the variable maxJumps to the value at index 0 in the jumps list
    for x in range(len(jumps)): #Loops through each jump
        if jumps[x] > maxJumps: #Checks if the current value is greater than maxJumps
            maxJumps = jumps[x] #If the current value is greater than maxJumps then it changes maxJumps if to the new value
    return maxJumps #Returns the value

#Function to display the full name of the athlete who completed the most jumping jacks
def displayAthlete(maxJumps):
    print("The athlete(s) with the most jumps are:") #Prints this statement
    for x in range(len(jumps)): #Loops through each jump
        if jumps[x] == maxJumps: #Checks if the current value is equal to maxJumps
            print(forename[x], surname[x]) #If the current value is greater than maxJumps then it prints the corresponding forename and surname
    print("who all jumped", str(maxJumps) + " times.") #Prints this statement along with the maximum number of jumps

def hostingLocation():
    coatbridgeCount = 0 #Sets count for each location to 0
    invernessCount = 0
    kirkcaldyCount = 0
    motherwellCount = 0
    for x in range(len(entryID)): #Loops through the file
        if location[x] == "Coatbridge": #Checks if the location matches
            coatbridgeCount += 1 #Adds one to the count if the location matches
        elif location[x] == "Inverness":
            invernessCount += 1
        elif location[x] == "Kirkcaldy":
            kirkcaldyCount += 1
        elif location[x] == "Motherwell":
            motherwellCount += 1
    print("Coatbridge has", coatbridgeCount, "finalists") #Prints statement
    print("Inverness has", invernessCount, "finalists")
    print("Kirkcaldy has", kirkcaldyCount, "finalists")
    print("Motherwell has", motherwellCount, "finalists")
    
#Main program
readAthletesFile() #Calls the functions

generateBibValues()

maximumJumps = maxJumpingJacks()

displayAthlete(maximumJumps)

hostingLocation()