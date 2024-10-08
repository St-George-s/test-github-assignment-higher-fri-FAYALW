import csv

class Country:
    def __init__(self,rank,countryName,countryCode, gold, silver, bronze, total):
        self.rank = rank
        self.countryName = countryName
        self.countryCode = countryCode
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        self.total = total

def dataLoading():
    fileName = "Olympic Starter/Olympics.csv"
    with open(fileName, 'r') as file: #Opens the file and reads it
        reader = csv.reader(file) #Premade function that takes each line at a time
        header = next(reader)  # Skips the header
        countries = [] #Makes an array called countries
        for row in reader:
            newRecord = Country(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                int(row[6])
            )
            countries.append(newRecord) #Adds countries to variable called newRecord
            
            #print(row)

    # Reads data from CSV into array of records
    
    return countries

def medalCalculation(countries):
     medalCalculation = 0
     for country in countries:
         medalCalculation = medalCalculation + country.total
    
     return medalCalculation

# Create a file of top countries
def topCountry(countries):
    pass
    
def goldMedalReport(countries):
    pass
   
# Main program
countries = dataLoading()
#print(countries)
# medalCalculation(countries)
topCountry(countries)
goldMedalReport(countries)

countries = dataLoading()
total = medalCalculation(countries)
print(total)