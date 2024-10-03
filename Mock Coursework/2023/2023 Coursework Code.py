import csv

# Read data from attractions CSV into parallel arrays
def readDataFromFile():
    with open('Mock Coursework/2023/Attractions.csv', 'r') as file:
        reader = csv.reader(file)

        # Set up parallel arrays
        attraction = []
        category = []
        visitors = []
        daysOpen = []
        height = []

        # Loop over each row and append data to parallel arrays
        for row in reader:
            attraction.append(row[0])
            category.append(row[1])
            visitors.append(int(row[2]))
            daysOpen.append(int(row[3]))
            height.append(row[4])

        return attraction, category, visitors, daysOpen, height

# 
def displayNamesMax(visitors, attraction):
    maximumValue = visitors[0] 
    max_index = 0
    for counter in range(1, len(visitors)): 
        if visitors[counter] > maximumValue: 
            maximumValue = visitors[counter]
            max_index = counter 
    print("The largest value was", str(maximumValue), "for attraction", (attraction[index])) 
    
# 
def displayNamesMin(visitors, attraction):
    minimumValue = visitors[0]
    min_index = 0
    for counter in range(1, len(visitors)): 
        if visitors[counter] < minimumValue: 
            minimumValue = visitors[counter]
            min_index = counter
    print("The smallest value was", str(minimumValue), "for attraction", (attraction[index]))

# 
def writeDataToFile(daysOpen, attraction, category):
    with open('Mock Coursework/2023/service.csv', 'w', newline='') as file: 
        writer = csv.writer(file) 
        for counter in range (len(attraction)):
            if category[counter] == 'Roller Coaster':
                days = daysOpen[counter] % 90
                if (90 - days) <= 7:
                    # Write array with one element to each row
                    writer.writerow([attraction[counter]]) 

# Main program
attraction, category, visitors, daysOpen, height = readDataFromFile()
displayNamesMax(visitors, attraction)
displayNamesMin(visitors, attraction)
writeDataToFile(daysOpen, attraction, category)