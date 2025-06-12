# Import the csv module to handle CSV file operations
import csv

# Define the Country class to represent each country's medal data
class Country:
    # Constructor to initialize country attributes
    # This function is called when creating a new Country object
    def __init__(self, rank, country, code, gold, silver, bronze, total):
        self.rank = rank            # Rank of the country in the medal standings
        self.country = country      # Name of the country
        self.code = code            # Country code (abbreviation)
        self.gold = gold            # Number of gold medals won
        self.silver = silver        # Number of silver medals won
        self.bronze = bronze        # Number of bronze medals won
        self.total = total          # Total number of medals won (gold + silver + bronze)

# Function to read data from a CSV file and create Country objects
def readDataFromFile():
    # Set the path to the CSV file containing the medal data
    fileName = "./File Handling/olympics2024.csv"
    countries = []  # Initialize an empty list to store Country objects

    # Open the CSV file in read mode
    with open(fileName, "r") as file:
        reader = csv.reader(file)  # Create a CSV reader object to parse the file
        next(reader)  # Skip the header row (first row) in the CSV file

        # Iterate through each row in the CSV file
        for line in reader:
            # Extract data from each column and assign it to variables
            rank = line[0]
            country = line[1]
            code = line[2]
            gold = int(line[3])    # Convert gold medal count to integer
            silver = int(line[4])  # Convert silver medal count to integer
            bronze = int(line[5])  # Convert bronze medal count to integer
            total = int(line[6])   # Convert total medal count to integer

            # Create a new Country object and add it to the countries list
            countries.append(Country(rank, country, code, gold, silver, bronze, total))

    return countries  # Return the list of Country objects

# Function to calculate the total number of medals across all countries
def totalMedals(countries):
    total = 0  # Initialize the total count of medals

    # Loop through each country and add its total medals to the cumulative total
    for country in countries:
        total += country.total

    # Print the final total number of medals awarded across all countries
    print("Total Medals:", total)

# Function to identify and print the country with the highest number of medals
def topCountry(countries):
    top = countries[0]  # Assume the first country has the most medals initially

    # Loop through each country to find the one with the highest total medals
    for country in countries:
        if country.total > top.total:
            top = country  # Update top country if a higher medal count is found

    # Print the name of the country with the highest number of medals
    print("Top Country:", top.country)

# Function to generate a report of countries with more than 30 gold medals
def goldMedalReport(countries):
    # Open (or create) a text file to write the report
    with open("topCountries.txt", "w") as file:
        # Loop through each country to check for gold medal count above 30
        for country in countries:
            if country.gold > 30:
                # Write the country name and gold medal count to the file
                file.write(f"{country.country}: {country.gold}\n")

# Main function to call the required functions and execute the program
def main():
    # Read the data from the CSV file into a list of Country objects
    countries = readDataFromFile()

    # Calculate and print the total number of medals awarded
    totalMedals(countries)

    # Identify and print the country with the most medals
    topCountry(countries)

    # Generate a report of countries with more than 30 gold medals
    goldMedalReport(countries)

# Execute the main function to run the program
main()