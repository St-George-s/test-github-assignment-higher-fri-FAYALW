import csv

def readDataFromFile():
    with open('Mock Coursework/Attractions.csv', 'r') as file:
        reader = csv.reader(file)
        attraction = []
        category = []
        visitors = []
        daysOpen = []
        height = []
        for row in reader:
            attraction.append(row[0])
            category.append(row[1])
            visitors.append(int(row[2]))
            daysOpen.append(int(row[3]))
            height.append(row[4])
        return attraction, category, visitors, daysOpen, height

def displayNamesMax(visitors, attraction):
    maximumValue = visitors[0] 
    index = 0
    for counter in range(1, len(visitors)): 
        if visitors[counter] > maximumValue: 
            maximumValue = visitors[counter]
            index = counter 
    print("The largest value was", str(maximumValue), "for attraction", (attraction[index])) 
    

def displayNamesMin(visitors, attraction):
    minimumValue = visitors[0]
    index = 0
    for counter in range(1, len(visitors)): 
        if visitors[counter] < minimumValue: 
            minimumValue = visitors[counter]
            index = counter
    print("The smallest value was", str(minimumValue), "for attraction", (attraction[index]))

def writeDataToFile(daysOpen, attraction, category):
    with open('Mock Coursework/service.csv', 'w', newline='') as file: 
        writer = csv.writer(file) 
        for x in range (len(attraction)):
            if category[x] == 'Roller Coaster':
                days = daysOpen[x] % 90
                if (90 - days) <= 7:
                    writer.writerow([attraction[x]]) 

attraction, category, visitors, daysOpen, height = readDataFromFile()
displayNamesMax(visitors, attraction)
displayNamesMin(visitors, attraction)
writeDataToFile(daysOpen, attraction, category)