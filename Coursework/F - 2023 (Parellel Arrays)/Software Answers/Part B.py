# Import the csv module to handle reading and writing CSV files
import csv

# Function to read data from the CSV file into parallel arrays
def readDataFromFile():
    # Open the CSV file containing attractions data
    with open('Mock Coursework/2023/Attractions.csv', 'r') as file:
        reader = csv.reader(file)  # Create a CSV reader to process each row

        # Set up parallel arrays for each attribute of attraction data
        attraction = []  # Array to store attraction names
        category = []    # Array to store attraction categories
        visitors = []    # Array to store the number of visitors
        daysOpen = []    # Array to store the number of days attractions are open
        height = []      # Array to store the height requirement for each attraction

        # Loop over each row in the CSV file and append data to respective arrays
        for row in reader:
            attraction.append(row[0])  # First column is the attraction name
            category.append(row[1])    # Second column is the category
            visitors.append(int(row[2]))  # Third column is visitor count (convert to integer)
            daysOpen.append(int(row[3]))  # Fourth column is days open (convert to integer)
            height.append(row[4])       # Fifth column is height requirement

        # Return all parallel arrays for use in the main program
        return attraction, category, visitors, daysOpen, height

# Function to display the attraction with the maximum number of visitors
def displayNamesMax(visitors, attraction):
    maximumValue = visitors[0]  # Assume the first visitor count is the maximum initially
    max_index = 0  # Index to track the position of the maximum value

    # Loop over visitor counts to find the maximum
    for counter in range(1, len(visitors)): 
        if visitors[counter] > maximumValue:  # Check if current visitor count is higher than max
            maximumValue = visitors[counter]
            max_index = counter  # Update index of the maximum visitor count

    # Display the attraction with the maximum number of visitors
    print("The largest value was", str(maximumValue), "for attraction", attraction[max_index])

# Function to display the attraction with the minimum number of visitors
def displayNamesMin(visitors, attraction):
    minimumValue = visitors[0]  # Assume the first visitor count is the minimum initially
    min_index = 0  # Index to track the position of the minimum value

    # Loop over visitor counts to find the minimum
    for counter in range(1, len(visitors)): 
        if visitors[counter] < minimumValue:  # Check if current visitor count is lower than min
            minimumValue = visitors[counter]
            min_index = counter  # Update index of the minimum visitor count

    # Display the attraction with the minimum number of visitors
    print("The smallest value was", str(minimumValue), "for attraction", attraction[min_index])

# Function to write roller coaster attractions that meet specific criteria to a new CSV file
def writeDataToFile(daysOpen, attraction, category):
    # Open the output file in write mode
    with open('Mock Coursework/2023/service.csv', 'w', newline='') as file:
        writer = csv.writer(file)  # Create a CSV writer for writing rows to the file

        # Loop over all attractions to check for roller coasters with specific criteria
        for counter in range(len(attraction)):
            if category[counter] == 'Roller Coaster':  # Check if attraction is a roller coaster
                days = daysOpen[counter] % 90  # Calculate remaining days open in the current 90-day cycle
                
                # Check if the attraction has 7 or fewer days remaining open
                if (90 - days) <= 7:
                    # Write the attraction name to the file if it meets the criteria
                    writer.writerow([attraction[counter]])

# Main program
# Call the readDataFromFile function to get parallel arrays of attraction data
attraction, category, visitors, daysOpen, height = readDataFromFile()

# Display the attraction with the maximum and minimum number of visitors
displayNamesMax(visitors, attraction)
displayNamesMin(visitors, attraction)

# Write qualifying roller coaster attractions to the output file
writeDataToFile(daysOpen, attraction, category)