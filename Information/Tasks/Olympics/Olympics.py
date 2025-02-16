# Import the csv module to work with CSV files
import csv

# Define the Country class to represent each country's medal data
class Country:
    def __init__(self, rank, countryName, countryCode, gold, silver, bronze, total):
        # Initialize attributes for the country's rank, name, code, and medal counts
        self.rank = rank                # Country's rank in the medal standings
        self.countryName = countryName  # Full name of the country
        self.countryCode = countryCode  # Country code abbreviation
        self.gold = gold                # Number of gold medals
        self.silver = silver            # Number of silver medals
        self.bronze = bronze            # Number of bronze medals
        self.total = total              # Total medals won by the country

# Function to load data from the CSV file into a list of Country objects
def dataLoading():
    fileName = "Olympic Starter/Olympics.csv"  # Path to the CSV file

    # Open the CSV file in read mode
    with open(fileName, 'r') as file:
        reader = csv.reader(file)      # Create a CSV reader to read each line
        header = next(reader)          # Skip the header row

        countries = []                 # Initialize an empty list to store Country objects

        # Loop through each row in the CSV file
        for row in reader:
            # Create a new Country object with data from the current row
            newRecord = Country(
                row[0],                # Rank
                row[1],                # Country name
                row[2],                # Country code
                row[3],                # Gold medal count
                row[4],                # Silver medal count
                row[5],                # Bronze medal count
                int(row[6])            # Total medal count (converted to integer)
            )

            # Append the new Country object to the countries list
            countries.append(newRecord)

            # Optional: Uncomment to print each row for debugging
            # print(row)

    # Return the list of Country objects after loading data
    return countries

# Function to calculate the total number of medals across all countries
def medalCalculation(countries):
    medalCalculation = 0  # Initialize a counter for the total medals

    # Loop through each Country object in the countries list
    for country in countries:
        # Add the country's total medals to the cumulative count
        medalCalculation = medalCalculation + country.total

    # Return the final total number of medals
    return medalCalculation

# Placeholder function to identify the top country based on specific criteria
def topCountry(countries):
    pass  # Currently does nothing

# Placeholder function to generate a report of countries with high gold medal counts
def goldMedalReport(countries):
    pass  # Currently does nothing

# Main program
# Load data from the CSV file into a list of Country objects
countries = dataLoading()

# Calculate and print the total number of medals awarded across all countries
total = medalCalculation(countries)
print(total)

# Call placeholder functions (if implemented) to generate additional reports
topCountry(countries)
goldMedalReport(countries)