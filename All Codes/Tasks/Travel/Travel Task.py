# Import the sys module to enable system-specific functions
import sys

# Function to get the travel destination from the user
def get_destination():
    # Prompt user to enter a travel destination
    destination = input("Enter your travel destination: ")
    
    # Check if the user wants to end the program
    if destination == "End":
        # Print all travel details collected so far
        print_travel_details(allTravel)
        
        # Exit the program with a message
        sys.exit("You have chosen to quit this program.")
    else:
        # Return the entered destination
        return destination

# Function to get the number of people traveling
def get_number_of_people():
    return input("Enter the number of people: ")

# Function to get the travel method from the user
def get_travel_method():
    return input("Enter your travel method: ")

# Function to print all travel details
def print_travel_details(allTravel):
    # Print the list of all travel entries
    print("All travel list: ", allTravel)

## Main program

# List of local destinations
localDestinations = ["Edinburgh", "Glasgow", "Dundee", "Aberdeen"]

# Define a global list to store all travel information
global allTravel
allTravel = []

# Temporary list to hold information for the current travel entry
latestTravel = []

# Infinite loop to keep collecting travel information until the user chooses to end
while True:
    # Get the latest destination from the user and add it to the temporary list
    latestDest = get_destination()
    latestTravel.append(latestDest)

    # Check if the destination is not in the list of local destinations
    if latestDest not in localDestinations:
        # Get the number of people for a non-local destination and add it to the list
        latestPeop = get_number_of_people()
        latestTravel.append(latestPeop)

        # Get the travel method for a non-local destination and add it to the list
        latestMeth = get_travel_method()
        latestTravel.append(latestMeth)
    else:
        # For a local destination, get the number of people and add it to the list
        latestPeop = get_number_of_people()
        latestTravel.append(latestPeop)

        # Automatically set travel method to "Local transport" for local destinations
        latestMeth = "Local transport"
        latestTravel.append(latestMeth)

    # Add the current travel entry to the main list of all travel entries
    allTravel.append(latestTravel.copy())

    # Clear the temporary list for the next travel entry to avoid duplicates
    latestTravel.clear()