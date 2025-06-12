# Function to calculate total rainfall in districts
def calculateTotalRainfall(rainfallData):
    # Initialize total rainfall to 0
    totalRainfall = 0
    
    # Loop through each district's rainfall data
    for district in rainfallData:
        # Add the current district's rainfall to the total
        totalRainfall = totalRainfall + district
    
    # Return the total rainfall calculated
    return totalRainfall

# Function to check if the total rainfall exceeds a certain threshold
def checkRainfallThreshold(rainfallData):
    # Calculate total rainfall using the previous function
    totalRainfall = calculateTotalRainfall(rainfallData)
    
    # Check if total rainfall exceeds, meets, or is below the threshold of 100
    if totalRainfall > 100:
        print("Rainfall is above threshold")
    elif totalRainfall == 100:
        print("Rainfall is at threshold")
    else:
        print("Rainfall is below threshold")

# Initialize an empty list to hold rainfall data
rainfallData = []

# Prompt the user to input the number of districts
districtNumber = int(input("How many districts? "))

# Loop through the number of districts to collect rainfall data
for x in range(districtNumber):
    # Append user input for rainfall values into the list
    rainfallData.append(int(input("Input a value for rainfall ")))

# Call the function to check if the total rainfall exceeds the threshold
checkRainfallThreshold(rainfallData)
